# DeepSleepNet

Can deep learning models learn everything? Even the sleep stages from neurophysilogical data ? For the first question, I dont have an answer but the second question answwered by Supratak and him buddies in the article titled " DeepSleepNet: A Model for Automatic Sleep Stage Scoring Based on Raw Single-Channel EEG" [^1]. In this articlei they introduced a model which performs automatic sleep stage scoring based on raw single-channel EEG.


There are two main stages of the DeepSleepNet model;

- **Representation Learning:** Consists of 2 parallel CNN blocks (4 convolutional layers) which extract time invariant features from single-channel EEG time series. The reason behind using two branches of CNNs is to extract both time and frequency sensitive features. Small kernel sizes (Fs/2) are useful for time information while large kernel sizes (FsX4) are more appropriate for the frequency information.  Following these input layers, additional 3 convolutional layers are added with small kernel sizes. Note that using only one additional layer with larger kernel size would have been preferred but this scenario increases the number of parameters in the model. I recommedn you to keep this practical issue in your mind when trying to employ your own model.



  
- **Sequence Residual Learning** 


<img width="1800" height="1050" alt="image" src="https://github.com/user-attachments/assets/4ce4a32f-716b-436b-b7b7-5a4b6dd5db32" />















## References 
[^1]: SUPRATAK, Akara, et al. DeepSleepNet: A model for automatic sleep stage scoring based on raw single-channel EEG. IEEE transactions on neural systems and rehabilitation engineering, 2017, 25.11: 1998-2008.
