
import RPi.GPIO as GPIO
import time
PIN_LumiereJaune = 15
PIN_LumiereRouge = 14
PIN_Button = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LumiereJaune, GPIO.OUT)
GPIO.setup(PIN_LumiereRouge, GPIO.OUT)
GPIO.setup(PIN_Button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(PIN_Button) == GPIO.LOW:
            print("Button appuye")
            GPIO.output(PIN_LumiereJaune, GPIO.HIGH)
            GPIO.output(PIN_LumiereRouge, GPIO.LOW)
        else:
            print("Button laisse")
            GPIO.output(PIN_LumiereJaune, GPIO.LOW)
            GPIO.output(PIN_LumiereRouge, GPIO.HIGH)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()