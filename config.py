import os

SAMPLE_NAME = input("Input the name of your sample \n") + ".wav"
SAMPLE_FOUND = False

while SAMPLE_FOUND == False:
    print(" ")
    if os.path.exists("./" + SAMPLE_NAME) == True:
        SAMPLE_FOUND = True
    else:
        SAMPLE_FOUND = False
        print("No such file found in the app directory, please try again!")
        SAMPLE_NAME = input("Input the name of your sample \n") + ".wav"



#print(SAMPLE_NAME)
#SAMPLE_NAME = "Synth22.wav"
#SAMPLE_NAME = input("Please input the name of your sample \n") + ".wav"

# The size of the audio buffer
BUFFER_SIZE = 32

# MIDI note playing back the original sample at the original speed
CENTRAL_NOTE = 67
