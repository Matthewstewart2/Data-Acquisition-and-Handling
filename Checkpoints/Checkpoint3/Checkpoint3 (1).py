# Import DAC chip libraries
from webiopi.devices.analog.mcp492X import MCP492X
from webiopi.devices.analog.mcp3x0x import MCP3208
import numpy as np
import time
import pylab

def main():
    # Define DAC on Chip Enable 1 (CE1/GPIO7)
    DAC1 = MCP492X(chip=1, channelCount=2, vref=3.3)
    # Define ADC on Chip Enable 0 (CE0/GPIO8)
    ADC0 = MCP3208(chip=0)

    # Arrays to store time and signal data
    time_array = np.zeros(100)
    sig_V_array = np.zeros(100)

    # Loop through 100 points reading signal from ADC0 channel 1
    # Set first time to 0 and others relative to it
    start_t = time.time()
    for i in range(len(time_array)):
        if i == 0:
            start_t = time.time()
            time_array[i] = 0
        else:
            time_array[i] = time.time() - start_t
        sig_V_array[i] = ADC0.analogReadVolt(1)
    end_t = time.time()

    # Last time minus first time
    total_t = time_array[-1] - time_array[0]
    mean_sample_t = total_t/len(time_array)
    print('Time taken: ' + str(total_t) + ' s')
    print('Mean time between samples: ' + str(mean_sample_t) + ' s')

    # Plot signal against time and save plot to pdf
    pylab.plot(time_array, sig_V_array)
    pylab.xlabel('time / s')
    pylab.ylabel('Signal Generator Voltage / V')
    pylab.title('Signal Voltage against Time')
    pylab.grid(True)
    pylab.savefig("samplingplot.pdf")
    pylab.show()

main()
