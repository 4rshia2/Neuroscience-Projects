from pymonntorch import *
from izikevich import Izikevich
from constants import *


net = Network(behavior={} ,settings=settings)

pop1 = NeuronGroup(net = net ,size=1 , tag = 'population1' , behavior={
    3:Izikevich(**FAST_SPIKING), 
    8:Recorder(tag= 'pop1_rec' , variables=['v' , 'u' , 'I'])})
net.initialize()
net.simulate_iterations(NUM_OF_ITERATION)



import matplotlib.pyplot as plt
fig , ax = plt.subplots(3 ,figsize = (20, 20))
fig.suptitle('Izhikevic Model',color = 'cadetblue')
ax[0].plot(net['pop1_rec',0].variables['v'])
x = np.linspace(-20, 1020, 20)
y = np.array([THRESHOLD for _ in range(20)])
ax[0].plot(x , y , linestyle = 'dashed' , color = 'orange')
ax[0].set_ylabel('Membrane Potential' , color ='cadetblue')
ax[0].set_xlabel('Time [ms]' , color ='cadetblue')
ax[0].text(-60,  35 , 'Threshold' , color = 'orange')
ax[1].plot(net['pop1_rec' ,0].variables['u'] , color = 'midnightblue')
ax[1].set_ylabel('Recovery Potential' , color= 'cadetblue')
ax[1].set_xlabel('Time [ms]' , color ='cadetblue')
ax[2].plot(net['pop1_rec' ,0].variables['I'] , color = 'lightseagreen')
ax[2].set_ylabel('Intensity' ,color = 'cadetblue' )
ax[2].set_xlabel('Time [ms]' , color ='cadetblue')
plt.show()
