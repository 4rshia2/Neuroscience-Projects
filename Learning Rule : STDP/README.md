# Introduction
This program serves as a starting point for the world of spiking neural networks. It implements the Flat Spike-Timing-Dependent Plasticity (Flat-STDP) learning rule to facilitate neural learning. The program tracks how the weight matrix of neurons changes during the learning process, and you can observe the results through plots within the program.
# FLAT-STDP
Flat-STDP (Flat Spike-Timing-Dependent Plasticity) is a synaptic learning rule in neuroscience, where the strength of a synapse changes based on the timing of spikes between pre- and postsynaptic neurons. Unlike traditional STDP, it doesn't distinguish between early and late spikes, making it more flexible for various learning tasks.
Mathematical equation for Flat-STDP:
Δw = A_pre * A_post * f(t_diff)
where Δw is the change in synaptic strength, A_pre is the presynaptic activity, A_post is the postsynaptic activity, and f(t_diff) is a function of the time difference between the spikes.
# IMPLEMENTATION DETAILS:
* **Pattern:** This class generates random binary (0 or 1) numbers in a matrix using a Poisson distribution. It determines, at each time step, which neurons will spike. The first dimension of the matrix represents the current time step, while the second dimension represents the neurons under consideration.
* **Local variables:** behavior for local variables and trace computation in Flat-STDP mathematical equation


