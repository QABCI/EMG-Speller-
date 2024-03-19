from pylsl import StreamInlet, resolve_stream  # EMG connection lsl
import os  # clean screen(optional)
import serial  # connect to LED
import time  # time
import winsound  # sound
from artistic_letters import *  # artistic_letter.py

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
arduino_port = "COM10"  # connect to your aduino
# the port can be any number, check it in your aduino IDE
baud_rate = 9600

ser = serial.Serial(arduino_port, baud_rate, timeout=1)

word = []


def main():
    stream_type = "EMG"  # Initialize LSL connection
    print("looking for an", stream_type, "stream...")
    streams = resolve_stream("type", stream_type)
    print("Connecting to an", stream_type, "stream...")
    inlet = StreamInlet(streams[0])  # Define structures to pull EEG(EMG) data

    # os.system("cls") #clean debug output
    while True:
        for letter in "ABCDEFGHIJ":  # Loop through letters for output

            print_artistic_letter(letter)  # Output Letters

            winsound.Beep(
                frequency, duration
            )  # Prompt the current letter through sound reminders
            time.sleep(0.1)
            winsound.Beep(
                frequency, duration
            )  # End acquisition after hearing the sound for the second time

            valuelist = []  # Obtaining EEG data
            while len(valuelist) < 100:
                chunk, timestamps = inlet.pull_chunk()
                if timestamps:
                    valuelist.append(chunk[0][1])

            if (
                sum(i >= 0.9 for i in valuelist) >= 20
            ):  # Determine whether to select the current letter just now based on the threshold value
                ser.write(letter.encode())  # output to aduino
            os.system("cls")
        break


if __name__ == "__main__":
    main()
