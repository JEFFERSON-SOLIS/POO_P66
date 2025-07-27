import time
from exep_mod import Modelo
from exep_vist import Vista

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista()

    def ejecutar(self):
        self.vista.mostrar_mensaje("Presiona Ctrl+C para salir")
        try:
            while True:
                try:
                    boton_estado = self.modelo.leer_boton()
                    if boton_estado == 0:  # Botón presionado (LOW)
                        self.modelo.encender_led()
                        self.vista.mostrar_mensaje("LED encendido por botón")
                    else:
                        self.modelo.apagar_led()
                        self.vista.mostrar_mensaje("LED apagado")
                except Exception as e:
                    self.vista.mostrar_mensaje(f"Error GPIO: {e}")
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.vista.mostrar_mensaje("Programa terminado")
        finally:
            self.modelo.limpiar()
