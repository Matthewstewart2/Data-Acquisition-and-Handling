import pylab
import matplotlib.animation as animation
import time
from webiopi.devices.sensor.onewiretemp import DS18S20

# Readout temperature sensor
tmp0 = DS18S20(slave="10-000802de022c")
temp1 = DS18S20(slave="10-000802ddfaec")

# Empty arrays of time and measurement values to plot
timeValues = []
measurements = []

# Set up the plot object
plotFigure = pylab.figure()

# The function to call each time the plot is updated
def updatePlot(i, start_t):

    # Store the current time
    timeValues.append(time.time() - start_t)
    # Store the measurement
    measurements.append(tmp0.getCelsius())
    # Clear the old plot
    plotFigure.clear()
    # Make the new plot
    pylab.plot(timeValues, measurements)
    pylab.xlabel('time / s')
    pylab.ylabel('Temperature / ^degC')
    pylab.title('Temperature against time')
    pylab.grid(True)

def main1():
    # Make the animated plot
    start_t = time.time()
    ani = animation.FuncAnimation(plotFigure, updatePlot, frames=50, fargs=(start_t,), interval=1000, repeat=False)

    pylab.show()

def main2():
    # Non-animated plot
    
    time_array = np.zeros(50)
    temp_array = np.zeros(50)

    start_t = time.time()
    for i in range(len(time_array)):
        time_array[i] = time.time() - start_t
        Temp_array[i] = tmp0.getCelsius()

    pylab.plot(time_array, temp_array)
    pylab.xlabel('time / s')
    pylab.ylabel('Temperature / ^degC')
    pylab.title('Temperature against Time')
    pylab.grid(True)
    pylab.show()

#main1()
main2()
