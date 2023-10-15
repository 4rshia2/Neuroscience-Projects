# Overview:
This Python script is designed to convert an input image into a "time to first spike" representation, where each pixel in the image corresponds to the time at which a neuron first spikes in response to the pixel's intensity. This encoding is useful for visualizing how a neural network reacts to visual stimuli, with the added feature that brighter pixels lead to earlier spiking.
# Output Data Strorage:
The result is a **3D tensor** where:
  * The first dimension represents the time intervals.
  * The second and third dimensions indicate the spatial position of the pixels within the image.
  * Each element in the tensor is either 0 or 1. A value of 1 denotes that the corresponding pixel has spiked at that specific moment, while 0 signifies no spike.

Detailed information are available in report file.
