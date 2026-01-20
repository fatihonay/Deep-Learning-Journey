
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

Two lovers are telling some phrases to each other to declare their emotions in this world. And finally they agree to deep dive through the surface and being far away from the shallow. Because, they know that others will know their intentions, feelings and secrets in the shallow. 
In our case, we face a similar choice criteria with our models. We can stay with the Shallow model where the features are known and interpretable. Or, we can choose the Deep model to discover complex, hidden patterns where our understanding may not reach eventually.  

```text
I'm off the deep end, watch as I dive in
I'll never meet the ground
Crash through the surface, where they can't hurt us
We're far from the shallow now

In the sha-, shallow
In the sha-ha-sha-la-la-la-llow
In the sha-ha, sha-ha-llow
We're far from the shallow now
```
I offer you to continue with shallow model, namely **ShallowFBCSPNet** which is a modern filter-bank CSP (FBCSP). Since this model is shallow, it consists of one layer of concatanated convolutional layer (temporal convolution first and then spatial filtering) and one output/classification layer. After the temporal convolution and the spatial filter of the shallow model, a squaring nonlinearity, a mean pooling layer and a logarithmic activation function followed; together these steps are analogous to the log-variance computation in FBCSP. The figure below describes the internal mechanism of the model. Let's summarize each step;

- The time window of 25 sample is employed on the each EEG channel. The number of units correspond to filter bank structure (40 filters)
- Then, the spatial filter which appoints weights to each channel performs a convolution across all electrodes, combining the temporally filtered signals to learn spatial patterns.

<img width="604" height="566" alt="image" src="https://github.com/user-attachments/assets/0f8291d8-884c-449e-ad5e-25da733443a8" />

## Model Design 
The logic behid the selection of model parameters will show us to how clever tricks can create useful modern version of classical tools like FBCSP. The desing of this modely was implemented wisely rather than blind criteria. Let's review these tirkcs together;

- Instead of using common activation functions (like ReLU), the model uses a squaring function. This was done to mimic the calculation of **power**, exactly as it is done in the classic FBCSP algorithm.

- In classical convolutional networks, large filters are broken down into smaller, simpler pieces throughout the layers. This shallow model skips this step because its time filters are already long and specialized. Therefore, the model choses width (one big kernel with size of 25) over depth (many small layers) to keep the signal processing clean and accurate to the physics of brain.
  
- After averaege pooling, the signal needs to be scaled. The model uses Logarithm for the method inspired by the classic FBCSP brain decoder.

At the final stage, model employs dense layer with softmax activation function with number of unit equals to the number of classes in the decoding problem (for example MI movements of Hand (L) - Hand (R)- Feet - Rest)



