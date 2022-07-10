import pylab
import numpy as np
import time
from webiopi.devices.sensor.onewiretemp import DS18S20


def main():
    # Non-animated plot
    # Setup sensors from serial numbers
    tmp0 = DS18S20(slave="10-000802de022c")
    tmp1 = DS18S20(slave="10-000802ddfaec")

    # Had both sensors with own time scale
    time0_array = np.zeros(50)
    time1_array = np.zeros(50)
    temp0_array = np.zeros(50)
    temp1_array = np.zeros(50)

    # Times were taken relative to start_t
    start_t = time.time()
    for i in range(len(time0_array)):
        time0_array[i] = time.time() - start_t
        temp0_array[i] = tmp0.getCelsius()
        time.sleep(0.25)

        time1_array[i] = time.time() - start_t
        temp1_array[i] = tmp1.getCelsius()
        time.sleep(0.25)

    # Plot both curves on same figure
    pylab.plot(time0_array, temp0_array, label='Sensor 1')
    pylab.plot(time1_array, temp1_array, label='Sensor 2')
    pylab.xlabel('Time / s')
    pylab.ylabel('Temperature / ^degC')
    pylab.title('Temperature against Time')
    pylab.legend()
    pylab.grid(True)
    pylab.show()

main()
