
# ShallowFBCSPNet

One of the pioneering deep learning model for EEG signal analysis is ShallowFBCSPNet. This model mainly consists of convolutional layers which extract spatiotemporal features from multichannel EEG signals. It has been proven to be very useful in BCI classification tasks.
In this section, I want to review architecture of this model and understand how to effectively use it for our problems. For the detailed informaiton, you can read the article titled "Deep Learning With Convolutional Neural Networks for EEG Decoding and Visualization".

```{note}
 ShallowFBCSPNet decodes task-related information from the raw EEG signals.
```
ShallowFBCSPNet is a modern CNN architecture for specialing EEG decoding tasks. Apart from classical CNNs for image segmentation/classification, ShallowFBCSPNet gets dynamically evolving multi channel EEG signals as imput. The goal is to learn features which are capable of recognizing different mental states. However, adaptation of CNN structures for such a specialized taks arises two fundamental problems;

- How to design architecture of the model to meet expectations?
- Which training strategy should we use for such a model?


As a computational neuroscienist, I always questioning the what exaclty deep learning models learn from data. This is important due to the two main reasons;

- Knowing which features deep learning models learn allows us to create generalizable models independent from specific datasets.
- Understanding the internal representations learned by deep models allows architectural and training design choices

 We want to understand what features in the brain signal discriminate the investigated classes.  

  
<img width="604" height="566" alt="image" src="https://github.com/user-attachments/assets/0f8291d8-884c-449e-ad5e-25da733443a8" />


## Persuading the sources to reveal themselves (Entrance Layer)






