from pylsl import StreamInlet, resolve_stream#EMG connection lsl
import os#clean screen(optional)
import serial #connect to LED
import time #time
import winsound#sound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
arduino_port = 'COM10' #connect to your aduino
baud_rate = 9600 

ser = serial.Serial(arduino_port, baud_rate, timeout=1)

artistic_letters = {
    'A': r"""
    AAAAA
   A    A
  AAAAAAA
 A        A
A          A
""",
    'B': r"""
 BBBBB
 B    B
 BBBBB
 B    B
 BBBBB
""",
    'C': r"""
  CCCCC
 C
 C
 C
  CCCCC
""",
    'D': r"""
 DDDDD
 D    D
 D    D
 D    D
 DDDDD
""",
    'E': r"""
 EEEEE
 E
 EEEE
 E
 EEEEE
""",
    'F': r"""
 FFFFF
 F
 FFFF
 F
 F
""",
    'G': r"""
  GGGGG
 G
 G  GGG
 G    G
  GGGG
""",
    'H': r"""
 H    H
 H    H
 HHHHHH
 H    H
 H    H
""",
    'I': r"""
 IIIIII
   II
   II
   II
 IIIIII
""",
    'J': r"""
     J
     J
     J
 J   J
  JJJ
""",
    'K': r"""
 K    K
 K  K
 KKK
 K  K
 K    K
""",
    'L': r"""
 L
 L
 L
 L
 LLLLL
""",
    'M': r"""
 M    M
 MM  MM
 M MM M
 M    M
 M    M
""",
    'N': r"""
 N    N
 NN   N
 N N  N
 N  N N
 N    N
""",
    'O': r"""
  OOO
 O   O
 O   O
 O   O
  OOO
""",
    'P': r"""
 PPPPP
 P    P
 PPPPP
 P
 P
""",
    'Q': r"""
  QQQ
 Q   Q
 Q   Q
 Q  QQ
  QQQ
    Q
""",
    'R': r"""
 RRRRR
 R    R
 RRRRR
 R  R
 R   RR
""",
    'S': r"""
  SSSS
 S
  SSS
     S
 SSSS
""",
    'T': r"""
 TTTTTTTT
    TT
    TT
    TT
    TT
""",
    'U': r"""
 U    U
 U    U
 U    U
 U    U
  UUUU
""",
    'V': r"""
 V     V
  V   V
   V V
    V
""",
    'W': r"""
 W     W
 W  W  W
 W  W  W
 WWWWwwW
 W     W
""",
    'X': r"""
 X     X
  X   X
    X
  X   X
 X     X
""",
    'Y': r"""
 Y     Y
  Y   Y
    Y
    Y
    Y
""",
    'Z': r"""
 ZZZZZZ
     Z
    Z
   Z
 ZZZZZZ
""",
}

def print_artistic_letter(letter):#output the Letter
    if letter.upper() in artistic_letters:
        print(artistic_letters[letter.upper()])
    else:
        print(f"Artistic representation for '{letter}' not available.")
word=[]
def main():
    stream_type="EMG" #Initialize LSL connection
    print("looking for an",stream_type, "stream...")
    streams = resolve_stream('type', stream_type) 
    print("Connecting to an", stream_type, "stream...")
    inlet = StreamInlet(streams[0])#Define structures to pull EEG(EMG) data
    
    #os.system("cls") #clean debug output
    while True:
        for letter in 'ABCDEFGHIJ': #Loop through letters for output
            
            print_artistic_letter(letter) #Output Letters
            
            winsound.Beep(frequency, duration)#Prompt the current letter through sound reminders
            time.sleep(0.1)
            winsound.Beep(frequency, duration)#End acquisition after hearing the sound for the second time
            
            valuelist=[]#Obtaining EEG data
            while len(valuelist) < 100:
                chunk, timestamps = inlet.pull_chunk()
                if timestamps:
                    valuelist.append(chunk[0][1])
            
            if sum(i >= 0.9 for i in valuelist) >= 20:#Determine whether to select the current letter just now based on the threshold value
                ser.write(letter.encode()) #output to aduino
            os.system("cls")
        break
if __name__ == '__main__':
    main()