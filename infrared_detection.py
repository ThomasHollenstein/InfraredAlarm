import RPi.GPIO as GPIO
import time

IR_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
last_state = 1

print("gestartet")


try:
    while True:
        current_state = GPIO.input(IR_PIN)
#         print(current_state)
        if current_state == 0 and last_state == 1:
            counter += 1
            print("Objekt erkannt Anzahl:" , counter)
            time.sleep(0.3)
            
        last_state = current_state
        time.sleep(0.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Ende")