import RPi.GPIO as GPIO
import time

def main():
    # Configure standard GPIO mode
    # "BCM" refers to the Broadcom processor
    GPIO.setmode(GPIO.BCM)

    SWITCH0 = 23
    LED0 = 24
    GPIO.setup(SWITCH0, GPIO.IN)
    GPIO.setup(LED0, GPIO.OUT)

    # Read the switch and if it is pressed toggle the state of the LED
    while True:
        if (GPIO.input(SWITCH0) == GPIO.HIGH):
            value = not GPIO.input(LED0)
            GPIO.output(LED0, value)
            time.sleep(1)

main()
