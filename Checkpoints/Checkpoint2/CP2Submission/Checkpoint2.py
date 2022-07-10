#Import DAC  and ADC chip libraries
from webiopi.devices.analog.mcp492X import MCP492X
from webiopi.devices.analog.mcp3x0x import MCP3208
import numpy as np
import time

def main():
    # Define DAC on Chip Enable 1 (CE1/GPIO7)
    DAC1 = MCP492X(chip=1, channelCount=2, vref=3.3)
    # Define ADC on Chip Enable 0 (CE0/GPIO8)
    ADC0 = MCP3208(chip=0)

    first_V = 0
    last_V = 3.3
    num_points = 50
    output_Vs = np.linspace(first_V, last_V, num_points)

    print('Output V on channel 0 of DAC1    Input V on channel 0 of ADC0')

    for output_V in output_Vs:
        # Output V on channel 0 of DAC1
        DAC1.analogWriteVolt(0, output_V)
        time.sleep(0.1)
        # Read input V on channel 0 of ADC0
        input_V = ADC0.analogReadVolt(0)
        print('OutputV: ' + str(round(output_V, 3)) + 'V    LDR V: ' + str(round(input_V, 3)) + 'V')

    DAC1.analogWriteVolt(0, 0)

main()
