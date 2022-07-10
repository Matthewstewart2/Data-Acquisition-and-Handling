# Imports
import webiopi
import time
from webiopi.devices.digital.pcf8574 import PCF8574A

def pattern1(mcp, wait_t):
    # Send commands to all four LEDs with each call of .portWrite(value)
    # Value is the decimal number corresponding to a 'byte', made of 8 bits (0's or 1's)
    # Only the first four bits are used here, the first bit is for P0, second for P1 etc.
    # For example values 0 = 0b0000 turns all on, 15 = 0b1111 turns all off

    for i in range(10):
        # 10 iterations
        # LED3 - LED2 - LED1  - LED0
        # LOW (on) - HIGH (off) - HIGH (off) - HIGH (off)
        mcp.portWrite(0b0111)
        # wait a bit
        time.sleep(wait_t)
        # HIGH - LOW - HIGH - HIGH
        mcp.portWrite(0b1011)
        time.sleep(wait_t)
        # HIGH - HIGH - LOW - HIGH
        mcp.portWrite(0b1101)
        time.sleep(wait_t)
        # HIGH - HIGH - HIGH - LOW
        mcp.portWrite(0b1110)
        time.sleep(wait_t)

    # all off
    mcp.portWrite(0b1111)

def pattern2(mcp, wait_t):

    for i in range(10):
        mcp.portWrite(0b1100)
        time.sleep(wait_t)
        mcp.portWrite(0b1001)
        time.sleep(wait_t)
        mcp.portWrite(0b0011)
        time.sleep(wait_t)
        mcp.portWrite(0b0110)
        time.sleep(wait_t)

    mcp.portWrite(0b1111)

def pattern3(mcp, wait_t):

    for i in range(10):
        mcp.portWrite(0b1010)
        time.sleep(wait_t)
        mcp.portWrite(0b0000)
        time.sleep(wait_t)
        mcp.portWrite(0b0101)
        time.sleep(wait_t)
        mcp.portWrite(0b1111)
        time.sleep(wait_t)

    mcp.portWrite(0b1111)


def main():
    # Retrieve GPIO lib
    GPIO = webiopi.GPIO

    # Setup chip
    mcp = PCF8574A(slave=0x38)

    # Set which PCF8574 GPIO pin is connected to the LED (negative logic)
    LED0 = 0

    # Setup GPIOs
    # Set Pin as output
    mcp.setFunction(LED0, GPIO.OUT)

    # Wait 0.3 seconds between flashes
    pattern1(mcp, 0.3)
    # Choose pattern 1
    #pattern2(mcp, 0.3)
    #pattern3(mcp, 0.3)


main()
