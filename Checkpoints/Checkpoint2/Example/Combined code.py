#Import DAC  and ADC chip libraries
from webiopi.devices.analog.mcp492X import MCP492X
from webiopi.devices.analog.mcp3x0x import MCP3208
import time

# Define DAC on Chip Enable 1 (CE1/GPIO7)  Pin 26
DAC1 = MCP492X(chip=1, channelCount=2, vref=3.3)
#efine ADC on Chip Enable 0 (CE0/GPIO8)   Pin 24
ADC0 = MCP3208(chip =0)


# For a white LED the voltage may need to be as high as 2.3 volts before light can be seen coming out
#For a RED LED this will be less than 2.4V probably around 1.5

#Loop to set the driving Voltage zero to 3.3 Volts in 50mV steps
step = 50 # For step size in mV
vdrive = 0
#for x in range(33):
while vdrive  < 3.3:
    #Set the driving voltage for the LED
    DAC1.analogWriteVolt(0, vdrive)
    #Now get the voltage from the LDR
    ldrvoltage = ADC0.analogReadVolt(2)
    #Print the results table line
    #print("Driving Voltage  = ", vdrive, "LDR Voltage ", ldrvoltage)
    print('%s %.3f %s %.3f' % ("Driving Voltage  = ", vdrive, "LDR Voltage ", ldrvoltage))
    time.sleep(0.05)
    vdrive = vdrive +step/1000

# Set Drive back to zero
    DAC1.analogWriteVolt(0, 0)
# print('%d %s cost $%.2f' % (6, 'bananas', 1.74))
