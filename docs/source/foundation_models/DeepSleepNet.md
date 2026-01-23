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


## End-to-end Pipeline

You know what? Pipelines are important for our world. Since ancient civilizations, humanity has built pipelines to create sustainable infrastructure. They are everywhere from irrigation channels to modern systems carrying natural gas, electricity, and data. Deep learning models are not so different from these systems. They also have pipelines that carry input data through layers to generate the desired output. So, wear your work gear and grab your tools—we’re heading on-site to review the pipeline of DeepSleepNet.

<img width="840" height="406" alt="image" src="https://github.com/user-attachments/assets/06e50254-f0d3-49f5-82cc-7e060509e54a" />

### 1. Part: Input Definition
Sequence of single-channel EEG epochs with a length of $N$ (represents 30 seconds);

$$\mathbf{X} = \{x_1, x_2, \dots, x_N\}$$

### 2. Part:  Feature Extraction
Two separate CNNs are used to extract features from each epoch $x_i$. One CNN uses small filters ($\theta_s$) to capture temporal detail, and the other uses large filters ($\theta_l$) to capture frequency information.

### Small Filter Stream
$$h^s_i = CNN_{\theta_s}(x_i)$$

### Large Filter Stream
$$h^l_i = CNN_{\theta_l}(x_i)$$

### Feature Concatenation
The outputs of the two streams are concatenated to form the combined feature vector $a_i$ for the $i$-th epoch.

$$a_i = h^s_i \parallel h^l_i$$

The resulting sequence of features is passed to the next stage:
$$\mathbf{A} = \{a_1, a_2, \dots, a_N\}$$

## 3. Part: Sequence Residual Learning
This stage processes the sequence of extracted features $\mathbf{A}$ to learn temporal transition rules. It utilizes Bidirectional-LSTMs and a residual shortcut connection.

### Bidirectional LSTM Processing
The model processes the sequence in both forward and backward directions to utilize past and future context.

**Forward LSTM:**
$$h^f_t, c^f_t = LSTM_{\theta_f} (h^f_{t-1}, c^f_{t-1}, a_t)$$

**Backward LSTM:**
$$h^b_t, c^b_t = LSTM_{\theta_b} (h^b_{t+1}, c^b_{t+1}, a_t)$$

*Where:*
* $h$ and $c$ represent the hidden states and cell states, respectively.
* Initial states $h^f_0, c^f_0$ and $h^b_{N+1}, c^b_{N+1}$ are set to zero vectors.

### Residual Shortcut Connection
To facilitate combination of raw temporal features obtained by CNN layers, features $a_t$ are transformed via a Fully Connected (FC) layer to match the dimensions of the LSTM output.

$$\text{Shortcut}_t = FC_\theta(a_t)$$

```{note}
The $FC$ function includes matrix multiplication, batch normalization, and ReLU activation.
```

###  Output Calculation
The final output vector $o_t$ is computed by concatenating the forward and backward hidden states and performing an element-wise addition with the shortcut connection.

$$o_t = (h^f_t \parallel h^b_t) + FC_\theta(a_t)$$


 ## Training and Handling Class Imbalance

 The lenght of sleep stages are not equal and this situaiton leads imbalanced number of classes. This is serious issue since model could tend to learn only the majority of sleep stages.
 










## References 
[^1]: SUPRATAK, Akara, et al. DeepSleepNet: A model for automatic sleep stage scoring based on raw single-channel EEG. IEEE transactions on neural systems and rehabilitation engineering, 2017, 25.11: 1998-2008.
