import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

IR_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def send_email():
    EMAIL_FROM = "thomashollenstein06@gmail.com"
    EMAIL_PASSWORD = "hlbogdrhbcjepfxf"
    EMAIL_TO = "thomashollenstein06@gmail.com"
    
    time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = "IR-Sensor Alarm"
    
    text = f"Der Infrarot-Sensor wurde ausgelöst.\nZeit: {time}"
    msg.attach(MIMEText(text, "plain"))
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
    
    print("E-Mail gesendet")
    
last_state = 1

print("gestartet")


try:
    while True:
        current_state = GPIO.input(IR_PIN)
        if current_state == 0 and last_state == 1:
            print("Objekt erkannt")
            send_email()
            time.sleep(5)
            
        last_state = current_state
        time.sleep(0.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Ende")
