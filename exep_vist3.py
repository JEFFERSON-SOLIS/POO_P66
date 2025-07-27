import tkinter as tk

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Control LED + Sensor DHT11")

        self.label_led = tk.Label(self.root, text="LED APAGADO", font=("Arial", 16))
        self.label_led.pack(pady=10)

        self.boton_led = tk.Button(self.root, text="Encender LED", command=self.controlador.toggle_led)
        self.boton_led.pack(pady=10)

        self.label_dht = tk.Label(self.root, text="Leyendo sensor...", font=("Arial", 14))
        self.label_dht.pack(pady=10)

        # Cerrar limpia GPIO y cierra ventana
        self.root.protocol("WM_DELETE_WINDOW", self.controlador.salir)

    def actualizar_estado_led(self, encendido):
        texto = "LED ENCENDIDO" if encendido else "LED APAGADO"
        self.label_led.config(text=texto)
        self.boton_led.config(text="Apagar LED" if encendido else "Encender LED")

    def actualizar_dht(self, texto):
        self.label_dht.config(text=texto)

    def iniciar(self):
        self.root.mainloop()
