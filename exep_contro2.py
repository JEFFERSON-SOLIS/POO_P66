import threading
import time
from exep_mod2 import Modelo
from exep_vist2 import Vista
import RPi.GPIO as GPIO

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista(self)
        self.estado_led = False

        self.hilo_boton = threading.Thread(target=self.monitor_boton)
        self.hilo_boton.daemon = True
        self.hilo_boton.start()

    def encender_led(self):
        try:
            self.modelo.encender_led()
            self.estado_led = True
            self.vista.mostrar_estado("Encendido")
        except Exception as e:
            self.vista.mostrar_estado(f"Error: {e}")

    def apagar_led(self):
        try:
            self.modelo.apagar_led()
            self.estado_led = False
            self.vista.mostrar_estado("Apagado")
        except Exception as e:
            self.vista.mostrar_estado(f"Error: {e}")

    def alternar_led(self):
        if self.estado_led:
            self.apagar_led()
        else:
            self.encender_led()

    def monitor_boton(self):
        while True:
            try:
                if self.modelo.leer_boton() == 0:  # Botón presionado
                    self.alternar_led()
                    time.sleep(0.5)  # Antirrebote
            except Exception as e:
                self.vista.mostrar_estado(f"Error botón: {e}")
            time.sleep(0.1)

    def salir(self):
        self.modelo.limpiar()
        self.vista.root.destroy()

    def ejecutar(self):
        self.vista.iniciar()
