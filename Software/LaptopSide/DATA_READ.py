##/* *********************************************************************************
## * Arduino Wifi Code (BLE side) 
##* ==================================================================================
##* Function: Stores audio samples streamed from blackfin
##  through SPI in an array for comms, also writes the
##  maximum value in the audio array to serial port of
##  Arduino UNO R4 to integrate with the FxLMS algorithm
##* ---------------------------------------------------------------------------------
##* Author: Tinker Assist: https://www.tinkerassist.com/blog/arduino-serial-port-read
##  Modified by: Dylan Mitchell, Carson Pope
##* Last Updated: 11/30/2023 
##* ----------------------------------------------------------------------------------
##* ==================================================================================
##* ***************************************************/*****************************/



import serial.tools.list_ports
import serial
import numpy as np
import sys
import tensorflow as tf
import keras

## Load trained model
model = keras.models.load_model('Capstone.keras')

# Use library to identify COM ports that are currently active on the device
ports = list(serial.tools.list_ports.comports())
portVar = None
# Define counter
count = 0;

# Generate list of ports
portsList = []
audio_samples = np.zeros(100);

audio_recieved_Arr = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

# Prompt user to select a port
val = input("Select Port: COM")

# Take user input and create a string that can be assigned to the serial object
for x in range(0, len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

# Assign serial object to the port of interest
serialInst = serial.Serial(portVar, 9600)  # Set the appropriate baud rate

try:
    # Read data from the particular port and store it in audio_samples
    while True:
        # If the serial port is currently taking in data and until 100 new elements have been populated in array 
        if (serialInst.in_waiting > 0) and (count <= 100):
            raw_data = serialInst.read(1)  # Read two bytes
            audio_samples[count] = int.from_bytes(raw_data, byteorder='little')
            # increment count
            count = count +1
        # If port is still reading and the count is 100 send array to be predicted
        if (serialInst.out_waiting == 0) and (count == 100):
            outputs = model.predict((np.array(audio_samples).reshape(100,1)).transpose());
            count = 0;
            max_Val = np.argmax(np.array(outputs),axis=None)
            print(str(max_Val))
            serialInst.write(max_Val.tobytes('C'))
    
# If a keyboard interrupt is initiated, quit and store all the data
except KeyboardInterrupt:
    print("Interrupt selected, storing data!\n")
    with open('Values.txt', 'wb') as file:
        file.write(audio_samples)
    audio_recieved_Arr = audio_samples;
    print(audio_recieved_Arr);
    serialInst.close()
    sys.exit()
