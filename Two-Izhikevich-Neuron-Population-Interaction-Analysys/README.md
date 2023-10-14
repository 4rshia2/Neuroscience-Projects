# Introduction
This project focuses on simulating and analyzing the interactions between two Neuron populations: excitatory (40 neurons) and inhibitory (10 neurons). This configuration mimics the typical 4:1 ratio found in the brain.
# Types of Connections
There are some types of connections for 2 neuron population. in this project we will analysys some of them. Since our neural model is Izhikevich, and we can simulate various spiking behaviors with it, we investigate different neuronal behaviors in each type of connection.
1. **Fully Connected :** the EXC Population connects to itself and the INH population, and the INH population connects to itself and the EXC Population.
   
   * **EXC POP : Regular Spike , INH POP : Fast Spike**
   * **EXC POP : Regular Spike , INH POP : Regular Spike**
   * **EXC POP : Regular Spike , INH POP : Chattering**
   * **EXC POP : Chatteing , INH POP : Regular Spike**
   * **EXC POP : Chattering , INH POP : Fast Spike**
