import torch
settings = {'device' : 'cpu' , 'def_type' : torch.float32}


INPUT_I = 15
STD = 3
THRESHOLD = 30
NUM_OF_ITERATION = 1000
NUM_OF_ITERATION_TO_REACH_I = 12

REGULAR_SPIKE = {'a' : 0.02 , 'b' : 0.2 , 'c' : -65 , 'd' : 8 , 'mode':'constant'}
REGULAR_SPIKE_NOISY = {'a' : 0.02 , 'b' : 0.2 , 'c' : -65 , 'd' : 8 , 'mode':'noisy'}

IB = {'a' : 0.02 , 'b' : 0.2 , 'c' : -55 , 'd' : 4 , 'mode':'constant'}
IB_NOISY = {'a' : 0.02 , 'b' : 0.2 , 'c' : -55 , 'd' : 4 , 'mode':'noisy'}

CHATTERING = {'a' : 0.02 , 'b' : 0.2 , 'c' : -50 , 'd' : 2 , 'mode':'constant'}
CHATTERING_NOISY = {'a' : 0.02 , 'b' : 0.2 , 'c' : -50 , 'd' : 2 , 'mode':'noisy'}

LOW_THRESHOLD_SPIKING = {'a' : 0.02 , 'b' : 0.25 , 'c' : -65 , 'd' : 2 , 'mode':'constant'}
LOW_THRESHOLD_SPIKING_NOISY = {'a' : 0.02 , 'b' : 0.25 , 'c' : -65 , 'd' : 2 , 'mode':'noisy'}

FAST_SPIKING = {'a' : 0.1 , 'b' : 0.2 , 'c' : -65 , 'd' : 2, 'mode':'constant'}
FAST_SPIKING_NOISY = {'a' : 0.1 , 'b' : 0.2 , 'c' : -65 , 'd' : 2 , 'mode':'noisy'}