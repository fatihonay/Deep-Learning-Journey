
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

We want to understand what features in the brain signal discriminate the investigated classes. We aim to create such models find these features and use them for the classification task. Beyond, we can also create models to extract features determined by prior domain knowledge. At this point, I would like you to notice this notation;

- Shallow: This architecture is specifically for prior domain knowledg to extract known features through single conolutional layer.
  
- Deep: This architecture is designed as a generic model to learn a wide range of features from scratch rather than being restricted to specific feature types (3-5 layers).
  
- Residual: This specific architecture is generally used to extend the capabilities of deep models (40-60 layers).

If you get familiar with the context, now we can review architecture and training strategies ShallowFBCSPNet. 

##  In the sha-ha-sha-la-la-la-llow

You probably know the famous song "Shallow" by Lady Gaga and Bradley Cooper. Yes, it is a love song, and it might seem irrelevant in the middle of a deep learning tutorial, but let me create a metaphor for our topic.

Two lovers are telling some phrases to each other to declare their emotions in this world. And finally they agreed to deep dive through the surface and being far way from the shallow. Because, they know that other will know their intentions, feelings, privates in the shallow. 
In our case, we face a similar choice with our models. We can stay with the Shallow model where the features are known and interpretable. Or, we can choose the Deep model to discover complex, hidden patterns where our understanding cannot reach.  



```{note}
I'm off the deep end, watch as I dive in
I'll never meet the ground
Crash through the surface, where they can't hurt us
We're far from the shallow now

In the sha-, shallow
In the sha-ha-sha-la-la-la-llow
In the sha-ha, sha-ha-llow
We're far from the shallow now
```



  
<img width="604" height="566" alt="image" src="https://github.com/user-attachments/assets/0f8291d8-884c-449e-ad5e-25da733443a8" />







