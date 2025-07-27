import RPi.GPIO as GPIO
import dht11

class SensorError(Exception):
    pass

class Modelo:
    def __init__(self):
        self.GPIO_LED = 4       # Pin GPIO para LED
        self.GPIO_BTN = 17      # Pin GPIO para botón
        self.GPIO_DHT11 = 18    # Pin GPIO para DHT11

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_LED, GPIO.OUT)
        GPIO.setup(self.GPIO_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.dht_sensor = dht11.DHT11(pin=self.GPIO_DHT11)
        self.estado_led = False

    def encender_led(self):
        GPIO.output(self.GPIO_LED, GPIO.HIGH)
        self.estado_led = True

    def apagar_led(self):
        GPIO.output(self.GPIO_LED, GPIO.LOW)
        self.estado_led = False

    def cambiar_estado_led(self):
        if self.estado_led:
            self.apagar_led()
        else:
            self.encender_led()

    def leer_boton(self):
        return GPIO.input(self.GPIO_BTN)

    def leer_dht11(self):
        resultado = self.dht_sensor.read()
        if resultado.is_valid():
            return resultado.temperature, resultado.humidity
        else:
            raise SensorError("Error leyendo DHT11")

    def limpiar_gpio(self):
        GPIO.cleanup()
