# Convolutional Neural Networks

Convolutional neural networks maybe the most popular and widely used deep learning models for broad range of applications including image classification, object detection, segmentation and medical imaging. Furthermore, BrainDecode library offers CNN models for analysis of EEG signals. Therefore, reviewing architecture of CNNs will help us to use and develop deep learning models in the future. I will try to keep this section simple as possible as I can. 

The modern deep learning architectures proved that they are capable of solving complex pattern recognition problems from different scientific domains including biomedical imaging and neuroscience.  These models minimize the effors of discovering and extracting feeatures from the raw datasets. Keep in mind that deep learning models learn certain patterns from data.

A simple CNN structure consists of two main sections: Feature Extraction and Classification. Each section has a unique architecture designed to realize specific tasks. Let's start with the first part of the CNN and discuss the details of the feature extraction architecture.

<img width="3234" height="1569" alt="image" src="https://github.com/user-attachments/assets/8f2e256b-17a5-4481-b99d-bf21028906a5" />


## Feature Extraction 
Getting meaningful patterns from complex input data and then making decisions solely based on the deep learning models seems to be magical at first sight. However, this magic relies on very simple mathematical rules which was probably invented before you born (I assume that you did not witness World War II). 

```{note}
**Convolution:**

In the context of Deep Learning, **Convolution** is a mathematical operation used to extract features from an input (like an image or EEG signal).

Imagine a small window (called a **kernel** or **filter**) sliding over your input data. At every step, the kernel performs element-wise multiplication with the part of the input it is currently covering, and then sums the results into a single number.

This process transforms the raw input into a **Feature Map**, highlighting important patterns like edges, shapes, or specific frequency bands in brain signals.
```



