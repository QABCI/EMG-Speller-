![flowchart](https://github.com/QABCI/EMG-Speller-/blob/main/EMG%20Speller%20Diagram.jpg?raw=true "flowChart")
# Ultimate Invincible Super Universe First EEG Typewriter

This project aims to create a system that allows users to type using EEG data. We’ll use Python to acquire real-time muscle EEG data via the Lab Streaming Layer (LSL) and then display the selected characters on an Arduino LCD screen.

### Requirements

| name        | function |  other  |
| :--------  | :-----  | :----:  |
| BCI | data collection|[openBCI](openBCI.com)|

Python: `pip install pylsl`
Python: `pip install Serial`

### Algorithm implementation (flowchart)

````
# main python code
valuelist = []  # Obtaining EEG data
while len(valuelist) < 100:
    chunk, timestamps = inlet.pull_chunk()
    if timestamps:
        valuelist.append(chunk[0][1])

if (
    sum(i >= 0.9 for i in valuelist) >= 20
):  # Determine whether to select the current letter just now based on the threshold value
    ser.write(letter.encode())  # output to aduino
````

```mermaid
graph TD;
B[Brain] --> |Electric Signals| E(EEG Sensor) --> OB(Open BCI Cyton Board) --> |BlueTooth|D(OpenBCI data aquisition software) --> L(LSL data stream) --> PT{Python Terminal}-->Ds((Display Letter)) --> C(Eyes)
PT --> |Serial Port| AB[Arduino Board] -->AL[Arduino LCD] --> C --> B
```


### Effect demonstration

[video](https://b23.tv/h7tQ6Z3)
picture here
