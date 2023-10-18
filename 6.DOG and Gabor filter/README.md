# Overview
This project focuses on applying various image filters to an input image using two different filter types: DoG (Difference of Gaussians) and Gabor filters. The filters simulate neural responses in the visual cortex. We use DOG filter for simulating ganglion cells in retina and Gabor filter for V1 cells. We also applied Time-to-First-Spike (TTFS) encoding to the images and then passed them through the filters.

# DOG Filter
The Difference of Gaussians (DoG) filter is a widely used image processing technique designed to approximate the response of neurons in the visual cortex to different visual stimuli. It is based on the concept of subtracting one Gaussian-blurred version of an image from another, creating a filtered output.
Key components of the DoG filter include:
* **Sigma Parameters:** DoG filters use two Gaussian kernels with different standard deviations (sigma values), denoted as sigma1 and sigma2. These parameters define the scale of the filter and impact the level of detail preserved or removed.
* **Kernel Size:** The size of the convolution kernel used for filtering. It is typically specified as a 2D grid, and its dimensions influence the spatial extent over which the filter operates.
* **Stride:** An optional parameter that determines the step size when applying the filter to an image. It controls the overlap or spacing between adjacent regions processed by the filter.

# Gabor Filter
The Gabor filter, named after physicist Dennis Gabor, is a powerful image processing tool used in the analysis of textures and patterns within images. It is especially relevant in understanding how the human visual system perceives and processes complex visual stimuli. The Gabor filter is designed to simulate responses in the human visual cortex(V1 area).
Key components and characteristics of the Gabor filter include:
* Kernel Size: The Gabor filter is defined by a 2D kernel, which can be square or rectangular, representing the spatial extent of the filter's operation. It is often characterized by its dimensions, such as width and height.

* **Orientation (Theta):** This parameter specifies the orientation of the filter. Gabor filters can be rotated to respond to patterns at different angles.

* **Frequency (Lambda):** The frequency parameter influences the number of oscillations in the Gabor wavelet. A higher frequency captures finer details, while a lower frequency captures broader patterns.

* **Spatial Aspect Ratio (Gamma):** This parameter controls the ellipticity of the Gabor filter, allowing it to respond differently to textures with varying aspect ratios.

* **Phase (Psi):** The phase parameter determines the phase offset of the sinusoidal component of the Gabor function. It helps control the response to the phase of textures in the image.
