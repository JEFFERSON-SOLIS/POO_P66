import RPi.GPIO as GPIO

class Modelo:
    def __init__(self):
        self.GPIO_LED = 4
        self.GPIO_BTN = 17
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_LED, GPIO.OUT)
        GPIO.setup(self.GPIO_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def encender_led(self):
        GPIO.output(self.GPIO_LED, GPIO.HIGH)

    def apagar_led(self):
        GPIO.output(self.GPIO_LED, GPIO.LOW)

    def leer_boton(self):
        return GPIO.input(self.GPIO_BTN)

    def limpiar(self):
        GPIO.cleanup()
