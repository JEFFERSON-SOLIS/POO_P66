# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import time
import threading

def contar(label):
    for i in range(1, 11):
        label.config(text=f"Contando: {i}")
        time.sleep(1)
    label.config(text="¡Finalizado!")

def iniciar_conteo(label):
    hilo = threading.Thread(target=contar, args=(label,))
    hilo.start()

# Crear ventana
ventana = tk.Tk()
ventana.title("Contador con Hilo")

label = ttk.Label(ventana, text="Pulsa el botón para comenzar")
label.pack(pady=10)

boton = ttk.Button(ventana, text="Iniciar conteo", command=lambda: iniciar_conteo(label))
boton.pack(pady=10)

ventana.mainloop()
