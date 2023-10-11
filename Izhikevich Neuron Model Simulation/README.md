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
##
