# EEG-Controlled Exoskeleton for Walking and Standing A Longitudinal Motor Imagery Study in Healthy Adults

Now, we will go through a big challenge.  We will try to understand and use BCI dataset for deploying a deep learning model. I think that you will find this dataset interesting and charming. I stumbled upon EEG-controlled exoskeleton BCI data when reviewing the OpenNEURO platform.  You can find it in the following link;

https://openneuro.org/datasets/ds006940/versions/1.0.0


```{note}
This dataset contains multimodal recordings from a brain–machine interface (BMI) training study involving seven healthy adult participants (ages 20–30, Mean = 24.3, SD = 3.8). The study focused on open-loop and closed-loop control of a lower-limb exoskeleton (Rex Bionics) using EEG and inertial sensor data. Each participant completed nine sessions over several weeks, structured into training and trial phases.
```

Actually this dataset consist of two modalities;
- **EEG:** 60 scalp channels + 4 EOG channels
- **IMU** 3-axis accelerometer, gyroscope, magnetometer, and quaternion

We will ignore IMU data and focus on EEG signals. Of course you can also benefit from IMU modality to incorporate your decoding system with more information. For now, let me to delve into EEG dataset for our journey. 

## Task Structure 

Each session includes multiple motor imagery tasks organized as follows:

**Training:** The training phase is used to calibrate the BMI decoder. Participants perform motor imagery tasks without feedback.

**Trial:** The trial phase consists of 12 closed-loop BMI trials per session, labeled trial01 to trial12. During these trials, participants use motor imagery to control the exoskeleton in real time.

Block 1: Trials 1–4

Block 2: Trials 5–8

Block 3: Trials 9–12

**walk6min / stop6min:** After completing the 12 trials, participants perform two extended motor imagery tasks:

walk6min – Imagining continuous walking for 6 minutes
stop6min – Imagining standing still for 6 minutes


As you can see, there are three main part of this BCI dataset as training, trials and walk6min/stop6min. Each participant followed this task design in each session.

```{note}
Here, a *session* refers to one complete run of the task design. Sessions could be organized in different days, weeks or months to collect data.
```

There are totally 9 sessions for each subject. Dont worry, thing will not get complicated. Each session is in same structure. Therefore, once we understand the a session from single subject, we will completely understand what is goin on in this dataset.

The succesful BCI implementation highly depends on decoder 

## Scenario 



```text

TRAIN:     [Session 1] [Session 2] ... [Session 7]
           └─────────── Past data ─────────────┘
           
VALIDATE:  [Session 8 training] [Session 9 training]
           └──── Recent calibration ────┘
           
TEST:      [Session 8 trials] [Session 9 trials]
           └───── Current usage ─────┘
```


| Event Tag                  | Likely Purpose                                                                 |
|---------------------------|----------------------------------------------------------------------------------|
| `acq-rexcommand`           | Logs the specific command sent to the exoskeleton (e.g., *Start Walking*).       |
| `acq-rexstate`             | Logs the physical state of the exoskeleton (e.g., *Left Leg Swing*, *Standing*). |
| `acq-infoclosedloop`       | contains the decoder output (BMI prediction probability)during closed-loop control.|
| `recording-beep_stim`      | Auditory cues signaling the user to start or stop motor imagery.                 |
| `recording-failcounter`   | Tracks errors or false activations during closed-loop trials (e.g., `task-trial01`). |











  
