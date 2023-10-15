from pymonntorch import *
from izikevich import Izikevich
from constants import *
import matplotlib.pyplot as plt
settings = {'device' : 'cpu' , 'def_type' : torch.float32}





x = []
y = []
for i in range(1 , 40):
    net = Network(behavior={} ,settings=settings)
    pop = NeuronGroup(net = net ,size=1 , behavior={
        3:Izikevich(**FAST_SPIKING, I = i),
        9:EventRecorder(tag= 'event_pop' , variables=['spike'])})
    net.initialize()
    net.simulate_iterations(NUM_OF_ITERATION)
    x.append(i)
    y.append(len(net['event_pop' , 0]['spike'][0])/NUM_OF_ITERATION)

plt.plot(x , y)
plt.title('F-I Curve' ,color ='cadetblue',size=24)
plt.xlabel('I(t)',color ='cadetblue',size=20)
plt.ylabel('f (1/T)',color ='cadetblue',size=20)
plt.show()
