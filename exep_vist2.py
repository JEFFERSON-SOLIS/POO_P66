import tkinter as tk

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Control LED Variante 2")

        self.boton_on = tk.Button(self.root, text="Encender LED", command=self.controlador.encender_led)
        self.boton_on.pack()

        self.boton_off = tk.Button(self.root, text="Apagar LED", command=self.controlador.apagar_led)
        self.boton_off.pack()

        self.boton_toggle = tk.Button(self.root, text="Alternar LED", command=self.controlador.alternar_led)
        self.boton_toggle.pack()

        self.estado_label = tk.Label(self.root, text="Estado LED: Desconocido")
        self.estado_label.pack()

        self.root.protocol("WM_DELETE_WINDOW", self.controlador.salir)

    def mostrar_estado(self, estado):
        self.estado_label.config(text=f"Estado LED: {estado}")

    def iniciar(self):
        self.root.mainloop()
