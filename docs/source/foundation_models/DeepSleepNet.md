# DeepSleepNet

Can deep learning models learn everything? Even the sleep stages from neurophysilogical data? For the first question, I dont have an answer but the second question answwered by Supratak and him buddies in the article titled "DeepSleepNet: A Model for Automatic Sleep Stage Scoring Based on Raw Single-Channel EEG" [^1]. In this article they introduced a model which performs automatic sleep stage scoring based on raw single-channel EEG.

There are two main stages of the DeepSleepNet model;

- **Representation Learning:** Consists of 2 parallel CNN blocks (4 convolutional layers) which extract features from single-channel EEG time series. The reason behind using two branches of CNNs is to extract both time and frequency sensitive features. Small kernel sizes (Fs/2) are useful for time information while large kernel sizes (FsX4) are more appropriate for the frequency information.  Following these input layers, additional 3 convolutional layers are added with smaller kernel sizes. Note that using only one additional layer with larger kernel size would have been preferred but this scenario increases the number of parameters in the model. I recommend you to keep this practical issue in your mind when trying to employ your own model. The input is designed for 30 second legth of single channel EEG because this lenght is common sense for analyzing sleep related neural data.

```{note}
Each convolutional layer performs three operations sequentially: 1D-convolution with its filters, batch normalization, and applying the rectified linear unit (ReLU) activation function.
```

  
- **Sequence Residual Learning:** This part consists of two main components as bidirectional-LSTMs and a short-cut connection.

  Bidirectional-LSTMs can be trained to encode temporal information such as sleep stage transition rules into the model.


<img width="1800" height="1050" alt="image" src="https://github.com/user-attachments/assets/4ce4a32f-716b-436b-b7b7-5a4b6dd5db32" />


| Component | Type | Kernel Size | Num Filters | Pool Size | Stride | Dropout |
|-----------|------|-------------|-------------|-----------|-------------|---------|
| Layer 1 | Conv1D | Fs/2 or 4XFs | 64 | - | Fs/16 or Fs/2 | 0.0 |
| Layer 2 | MaxPool1D | - | - | 8 | 8 | 0.5 |
| Layer 3-5 | Conv1D | 8 | 128 | - | - | 0.0 |
| Layer 6 | MaxPool1D | - | - | 4 | 4 | 0.5 |


## Pipeline for 


<img width="526" height="280" alt="image" src="https://github.com/user-attachments/assets/451554a6-caac-4194-986a-64ae85476b0a" />



 ## Training and Handling Class Imbalance

 The lenght of sleep stages are not equal and this situaiton leads imbalanced number of classes. This is serious issue since model could tend to learn only the majority of sleep stages.
 










## References 
[^1]: SUPRATAK, Akara, et al. DeepSleepNet: A model for automatic sleep stage scoring based on raw single-channel EEG. IEEE transactions on neural systems and rehabilitation engineering, 2017, 25.11: 1998-2008.
