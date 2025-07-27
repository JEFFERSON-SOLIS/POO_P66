import threading
import time
import telebot
from exep_mod3 import Modelo, SensorError
from exep_vist3 import Vista
import RPi.GPIO as GPIO

TOKEN = "7500419863:AAEpSA--y0SXdTZAEWQ0gAv31sBh-V7m1qU"  # Cambia por tu token real

class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista(self)
        self.bot = telebot.TeleBot(TOKEN)

        # Hilo para monitorear botón físico
        self.hilo_boton = threading.Thread(target=self.monitor_boton)
        self.hilo_boton.daemon = True
        self.hilo_boton.start()

        # Hilo para actualizar sensor DHT11
        self.hilo_dht = threading.Thread(target=self.actualizar_dht)
        self.hilo_dht.daemon = True
        self.hilo_dht.start()

        # Configurar comandos telegram
        self.configurar_bot()

    def ejecutar(self):
        self.vista.iniciar()

    def toggle_led(self):
        try:
            self.modelo.cambiar_estado_led()
            self.vista.actualizar_estado_led(self.modelo.estado_led)
        except Exception as e:
            print(f"Error controlando LED: {e}")

    def monitor_boton(self):
        boton_anterior = self.modelo.leer_boton()
        while True:
            boton_actual = self.modelo.leer_boton()
            if boton_anterior == GPIO.HIGH and boton_actual == GPIO.LOW:
                # Presionaron el botón, cambiar LED
                self.toggle_led()
            boton_anterior = boton_actual
            time.sleep(0.1)

    def actualizar_dht(self):
        while True:
            try:
                temp, hum = self.modelo.leer_dht11()
                texto = f"Temperatura: {temp}°C | Humedad: {hum}%"
                self.vista.actualizar_dht(texto)
            except SensorError as e:
                self.vista.actualizar_dht(str(e))
            time.sleep(5)

    def configurar_bot(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def enviar_mensaje(mensaje):
            self.bot.reply_to(mensaje, "Comandos disponibles:\n/on - Encender LED\n/off - Apagar LED\n/status - Estado LED y sensor")

        @self.bot.message_handler(commands=['on'])
        def encender(mensaje):
            try:
                self.modelo.encender_led()
                self.vista.actualizar_estado_led(True)
                self.bot.reply_to(mensaje, "LED encendido")
            except Exception as e:
                self.bot.reply_to(mensaje, f"Error: {e}")

        @self.bot.message_handler(commands=['off'])
        def apagar(mensaje):
            try:
                self.modelo.apagar_led()
                self.vista.actualizar_estado_led(False)
                self.bot.reply_to(mensaje, "LED apagado")
            except Exception as e:
                self.bot.reply_to(mensaje, f"Error: {e}")

        @self.bot.message_handler(commands=['status'])
        def status(mensaje):
            try:
                estado = "ENCENDIDO" if self.modelo.estado_led else "APAGADO"
                temp, hum = self.modelo.leer_dht11()
                respuesta = f"LED está {estado}\nTemperatura: {temp}°C\nHumedad: {hum}%"
                self.bot.reply_to(mensaje, respuesta)
            except SensorError as e:
                self.bot.reply_to(mensaje, f"Sensor error: {e}")

        # Ejecutar bot en hilo separado para no bloquear GUI
        hilo_bot = threading.Thread(target=self.bot.polling)
        hilo_bot.daemon = True
        hilo_bot.start()

    def salir(self):
        print("Limpiando GPIO y cerrando...")
        self.modelo.limpiar_gpio()
        self.vista.root.destroy()
