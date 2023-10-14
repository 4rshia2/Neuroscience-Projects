# Introduction
This project focuses on simulating and analyzing the interactions between two Neuron populations: excitatory (40 neurons) and inhibitory (10 neurons). This configuration mimics the typical 4:1 ratio found in the brain.
# Types of Connections
There are some types of connections for 2 neuron population. In this project we will analysys some of them. Since our neural model is Izhikevich, and we can simulate various spiking behaviors with it, we investigate different neuronal behaviors in each type of connection.Spiking behaviors of both neuronal population that are used for each type of connection to analysys, are mentioned.
1. **Fully Connected :** the EXC Population connects to itself and the INH population, and the INH population connects to itself and the EXC Population.
   
   * **EXC POP : Regular Spike , INH POP : Fast Spike**
   * **EXC POP : Regular Spike , INH POP : Regular Spike**
   * **EXC POP : Regular Spike , INH POP : Chattering**
   * **EXC POP : Chattering , INH POP : Regular Spike**
   * **EXC POP : Chattering , INH POP : Fast Spike**
2. **Partially Connected I :** the EXC Population connects to the INH Population and the INH Population connects to the EXC Population.
   * **EXC POP : Regular Spike , INH POP : Fast Spike**
   * **EXC POP : Chattering Spike , INH POP : Regular Spike**
3. **Partially Connected II :** the EXC Population connects to itself and the INH Population and the INH Population connects to the EXC Population.
   * **EXC POP : Chattering Spike , INH POP : Regular Spike**
# Connection Density:
In all the situations described earlier, we considered that, for example, if excitatory neuronal population connects to inhibitory neuronal population means every 40 neurons in the excitatory neuronal population were connected to 10 neurons in the inhibitory neuronal population. We call this parameter 'connection density.' We also adjusted this connection density for all the connections mentioned above, and the probability of connections between two neurons followed a normal distribution. We looked into how increasing or decreasing this density affected interactions between populations.
