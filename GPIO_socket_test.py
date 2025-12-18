import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

test_pins = [4, 17, 18, 22, 23, 24, 25, 27]

for pin in test_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
print("GPIO-TEST gestartet")

try:
    while True:
        states = []
        for pin in test_pins:
            states.append(f"{pin}:{GPIO.input(pin)}")
        print(" | ".join(states))
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Ende")