import RPi.GPIO as GPIO 
import time 
LED_PIN = 18 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_PIN, GPIO.OUT) 
try: 
	while True: 
		GPIO.output(LED_PIN, GPIO.HIGH) # Liga 
		time.sleep(0.5) 
		GPIO.output(LED_PIN, GPIO.LOW) # Desliga 
		time.sleep(0.5) 
finally: 
	GPIO.cleanup()  
