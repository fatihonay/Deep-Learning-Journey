# Convolutional Neural Networks

Convolutional neural networks maybe the most popular and widely used deep learning models for broad range of applications including image classification, object detection, segmentation and medical imaging. Furthermore, BrainDecode library offers CNN models for analysis of EEG signals. Therefore, reviewing architecture of CNNs will help us to use and develop deep learning models in the future. I will try to keep this section simple as possible as I can. 

The modern deep learning architectures proved that they are capable of solving complex pattern recognition problems from different scientific domains including biomedical imaging and neuroscience.  These models minimize the effors of discovering and extracting feeatures from the raw datasets. Keep in mind that deep learning models learn certain patterns from data.

A simple CNN structure consists of two main sections: Feature Extraction and Classification. Each section has a unique architecture designed to realize specific tasks. Let's start with the first part of the CNN and discuss the details of the feature extraction architecture.

<img width="3234" height="1569" alt="image" src="https://github.com/user-attachments/assets/8f2e256b-17a5-4481-b99d-bf21028906a5" />


## Feature Extraction 
Getting meaningful patterns from complex input data and then making decisions solely based on the deep learning models seems to be magical at first sight. However, this magic relies on very simple mathematical rules which was probably invented before you born (I assume that you did not witness World War II). 

**1. Convolution**

In the context of Deep Learning, convolution is a mathematical operation used to extract features from an input data. Imagine a small window (kernel) sliding over your input data. At every step, the kernel performs element-wise multiplication with the part of the input, and then sums the results into a single number. This process transforms the raw input into a **feature map**, highlighting important patterns like edges, shapes, or specific frequency bands in brain signals.

```{note}
Convolution is a simple dot product operation.
```
The figure below indicates the how convolution between 3x3 kernel (shaded matrix) and 5x5 input (blue matrix) is performed to obtain 3x3 output (green matrix). Note that the size of input and output is different in that case due to the edge limitation. Padding strategies (like zero padding) can be employed to preserve the spatial dimensions, but this involves adding artificial information around the borders of the input to allow the kernel to process the edges.

<img width="874" height="540" alt="image" src="https://github.com/user-attachments/assets/874ba1c1-6e6f-44a0-801d-45ac71db2b87" />

**2. Activation**

Convolution is a linear operation which simply multiplies and adds variables. However, real world data is often complex and non-linear, so we need an activation function to enable the network to learn intricate patterns. Without this non-linearity, the neural network would not be powerful enough to distinguish complex patterns. Actually, I am not sure how exactly this operation is useful but intiutively I agree with this opinion. We may discuss this point in the future but this is not in our scope for now.

The most strandard activation functions used in CNN models is ReLU which applies non-linear transform on the feature map (output of convolution operation). This operation removes negative values and replaces them with zero. The figure below descibes this operation. Please stop here and review the figure for a moment.

If we talk in math what ReLU activation does, this equation can easily explain it.

$$ f(x) = \max(0, x) $$

```{note}
Non-linear activation function allows the network to model complex, non-linear patterns.
```


<img width="871" height="424" alt="image" src="https://github.com/user-attachments/assets/71738a12-17b2-472e-a990-45e10e988c46" />



**2. Pooling**
Pooling is a standard dimension reduction technique after performing convolution operation on the input data. 









