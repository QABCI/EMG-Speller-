![flowchart](/assets/img/philly-magic-garden.jpg "flowChart")
# Ultimate Invincible Super Universe First EEG Typewriter

This project aims to create a system that allows users to type using EEG data. We’ll use Python to acquire real-time muscle EEG data via the Lab Streaming Layer (LSL) and then display the selected characters on an Arduino LCD screen.

### Requirements

| name        | function |  other  |
| :--------  | :-----  | :----:  |
| BCI | data collection|[openBCI](openBCI.com)|

Python: `pip install blablablabla`

### Algorithm implementation (flowchart)

````
print("hello world")
````

```mermaid
graph TD;
B[Brain] --> |Electric Signals| E(EEG Sensor) --> OB(Open BCI Cyton Board) --> |BlueTooth|D(OpenBCI data aquisition software) --> L(LSL data stream) --> PT{Python Terminal}-->Ds((Display Letter)) --> C(Eyes)
PT --> |Serial Port| AB[Arduino Board] -->AL[Arduino LCD] --> C --> B
```


### Effect demonstration

[video](https://www.bilibili.com)
picture here
