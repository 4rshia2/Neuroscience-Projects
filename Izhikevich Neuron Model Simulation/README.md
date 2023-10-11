# Izhikevich Neuron Model Simulation
## Overview
The Izhikevich neuron model is a powerful and computationally efficient alternative to the Hodgkin and Huxley model for simulating neuronal behavior. It is designed to capture a wide range of neuronal firing patterns while prioritizing simulation speed. Below, I will provide you with the core equations and explanations of the key parameters of the Izhikevich neuron model:
### Core Equations
1. **Membrane Potential (V):** This is the primary variable representing the neuron's membrane potential. It evolves according to the following differential equation:
   ```
   dV/dt = 0.04V^2 + 5V + 140 - u + I
   ```
   Where:
   + V is the membrane potential.
   + u is the recovery variable.
   + I is the input current.
2. Recovery Variable (u): The recovery variable describes the membrane recovery dynamics and evolves as follows:
   ```
   du/dt = a * (b * V - u)
   ```
## Parameters:
1. a: This parameter determines the time scale of the recovery variable 'u'. A larger 'a' leads to slower recovery.
2. b: 'b' influences the sensitivity of the recovery variable 'u' to changes in the membrane potential 'V'. Higher 'b' values make 'u' respond more strongly to changes in 'V'.
3. c: 'c' is the membrane potential reset value after the neuron spikes. When 'V' reaches this threshold, it is reset to 'c'.
4. d: 'd' determines the after-spike reset of the recovery variable 'u'. It is the increment applied to 'u' after each spike.
5. I: The input current 'I' represents external stimuli applied to the neuron. It can be used to control the neuron's behavior.
And as we mentioned in parameters' description, There's a mechanism for each spike:
+ If v > 30 mV , Neuron Spikes
+ then [v = c and u = u + d]

## Key Neuronal Behavior via Izhikevich Simulation
1. **Regular Spiking:**
   **Description:** Regular spiking neurons exhibit a consistent and rhythmic firing pattern. They fire action potentials at regular intervals in response to input stimuli.
   **Configs:**
   + a = 0.02
   + b = 0.2
   + c = -65
   + d = 6
