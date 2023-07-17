import RPi.GPIO as GPIO
from gpiozero import LEDCharDisplay
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED1_PIN = 18
LED2_PIN = 23
LED3_PIN = 24

GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.setup(LED3_PIN, GPIO.OUT)

LED_OFF = 0
LED_ON = 1

def cycle_leds():
    GPIO.output(LED1_PIN, LED_ON)
    display_countdown()
    GPIO.output(LED1_PIN, LED_OFF)

    GPIO.output(LED2_PIN, LED_ON)
    display_countdown()
    GPIO.output(LED2_PIN, LED_OFF)

    GPIO.output(LED3_PIN, LED_ON)
    display_countdown()
    GPIO.output(LED3_PIN, LED_OFF)

display = LEDCharDisplay(26, 19, 13, 6, 5, 21, 20, active_high=False)

def display_countdown():
    for i in range(5, 0, -1):
        display.value = str(i)
        sleep(1)

while True:
    command = input("Enter 'auto' to activate automatic mode or 'exit' to quit: ")

    if command == 'auto':
        while True:
            cycle_leds()
    elif command == 'exit':
        break
    else:
        print("Unknown command:", command)

GPIO.cleanup()
