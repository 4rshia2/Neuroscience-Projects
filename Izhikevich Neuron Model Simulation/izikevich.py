from pymonntorch import *
from constants import *
class Izikevich(Behavior):
    def initialize(self , n):
        self.mode = self.parameter('mode' , 'constant')   # to choose between constant I and noisy I
        self.a = self.parameter('a' , None ,required=True)
        self.b = self.parameter('b' , None ,required=True)
        self.c = self.parameter('c' , None ,required=True)
        self.d = self.parameter('d' , None ,required=True)
        self.I = self.parameter('I' , INPUT_I)
        n.v = n.vector('uniform')
        n.u = n.vector('uniform')
        n.dt = 0.5
        n.I = n.vector('zeros')
        self.threshold = self.parameter('threshold' , THRESHOLD)
        n.spike = n.v > self.threshold
        self.I_change = True
        self.cnt_iteration = 1
    def _calc_noisy_I(self , n):
        size = n.I.size(dim=0)
        mean = torch.ones(size) * self.I
        std = torch.ones(size) * STD
        n.I = torch.normal(mean , std)
    def forward(self , n):
        if self.cnt_iteration <= NUM_OF_ITERATION_TO_REACH_I:
            n.I += self.I / NUM_OF_ITERATION_TO_REACH_I
        elif self.cnt_iteration > (NUM_OF_ITERATION - NUM_OF_ITERATION_TO_REACH_I):
            n.I -= self.I / NUM_OF_ITERATION_TO_REACH_I
            self.I_change = True
        else:
            self.I_change = False
        if (self.mode == 'noisy') and (not self.I_change):
            self._calc_noisy_I(n)
        n.v[n.spike] = self.c
        n.u[n.spike] += self.d
        dv = (0.04*(n.v**2) + 5*n.v + 140 - n.u + n.I)
        du = self.a * (self.b * n.v - n.u)
        n.v += dv*n.dt
        n.u += du*n.dt
        n.spike = n.v > self.threshold
        self.cnt_iteration += 1
        
