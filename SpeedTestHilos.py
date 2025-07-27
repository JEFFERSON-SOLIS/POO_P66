# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 08:10:27 2025
@author: Juan Carlos
"""

import tkinter as tk
from tkinter import ttk, messagebox
import speedtest
import sqlite3
import datetime
import threading
import time

DB_PATH = "InternetSpeed.db"

def medir_en_hilo():
    btn_probar.config(state="disabled")
    thread = threading.Thread(target=probar_velocidad)
    thread.start()

def probar_velocidad():
    try:
        progress_download['value'] = 0
        progress_upload['value'] = 0
        lbl_resultado.config(text="⏳ Midiendo velocidad...")

        for i in range(0, 100, 5):
            progress_download['value'] = i
            ventana.update()
            time.sleep(0.1)

        s = speedtest.Speedtest()
        s.get_best_server()

        download = round(s.download() / 1_000_000, 2)
        progress_download['value'] = min(download, 100)
        ventana.update()

        for i in range(0, 100, 5):
            progress_upload['value'] = i
            ventana.update()
            time.sleep(0.1)

        upload = round(s.upload() / 1_000_000, 2)
        progress_upload['value'] = min(upload, 100)
        ping = s.results.ping
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        lbl_resultado.config(
            text=f"↓ {download} Mbps | ↑ {upload} Mbps | ↔ {ping} ms\n{timestamp}")

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS internet_speed (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            download REAL,
            upload REAL,
            ping REAL
        )''')
        c.execute("INSERT INTO internet_speed (timestamp, download, upload, ping) VALUES (?, ?, ?, ?)",
                  (timestamp, download, upload, ping))
        conn.commit()
        conn.close()

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo medir la velocidad:\n{e}")
        lbl_resultado.config(text="")
    finally:
        btn_probar.config(state="normal")

def cargar_datos():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        if var_filtro.get():
            c.execute("SELECT timestamp, download, upload, ping FROM internet_speed WHERE ping > 100 ORDER BY id DESC LIMIT 10")
        else:
            c.execute("SELECT timestamp, download, upload, ping FROM internet_speed ORDER BY id DESC LIMIT 10")

        registros = c.fetchall()
        conn.close()

        for row in tabla.get_children():
            tabla.delete(row)

        for r in registros:
            tabla.insert("", "end", values=r)

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la base de datos:\n{e}")

# --- GUI ---
ventana = tk.Tk()
ventana.title("WiFi Meter Realtime")
ventana.geometry("520x460")

# Estilo para barras azules
style = ttk.Style()
style.theme_use('default')
style.configure("Blue.Horizontal.TProgressbar", background='blue', troughcolor='lightgray')

tabs = ttk.Notebook(ventana)
tab_medicion = ttk.Frame(tabs)
tab_consultas = ttk.Frame(tabs)
tabs.add(tab_medicion, text="📶 Medir Velocidad")
tabs.add(tab_consultas, text="📋 Consultas")
tabs.pack(expand=1, fill="both")

# Tab 1: Medición
btn_probar = tk.Button(tab_medicion, text="Probar velocidad", font=("Arial", 14), command=medir_en_hilo)
btn_probar.pack(pady=10)

lbl_resultado = tk.Label(tab_medicion, text="", font=("Arial", 12))
lbl_resultado.pack(pady=5)

lbl_down = tk.Label(tab_medicion, text="Descarga", font=("Arial", 10))
lbl_down.pack()
progress_download = ttk.Progressbar(tab_medicion, length=400, maximum=100, style="Blue.Horizontal.TProgressbar", mode="determinate")
progress_download.pack(pady=5, ipady=6)  # ipady ajusta altura

lbl_up = tk.Label(tab_medicion, text="Subida", font=("Arial", 10))
lbl_up.pack()
progress_upload = ttk.Progressbar(tab_medicion, length=400, maximum=100, style="Blue.Horizontal.TProgressbar", mode="determinate")
progress_upload.pack(pady=5, ipady=6)

# Tab 2: Consultas
btn_cargar = tk.Button(tab_consultas, text="🔄 Cargar últimos 10 registros", command=cargar_datos)
btn_cargar.pack(pady=10)

# Filtro de ping > 100 ms
var_filtro = tk.BooleanVar()
chk_ping = tk.Checkbutton(tab_consultas, text="🔍 Mostrar solo ping > 100 ms", variable=var_filtro)
chk_ping.pack()

tabla = ttk.Treeview(tab_consultas, columns=("Fecha", "Descarga", "Subida", "Ping"), show="headings")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Descarga", text="↓ (Mbps)")
tabla.heading("Subida", text="↑ (Mbps)")
tabla.heading("Ping", text="↔ (ms)")
tabla.pack(padx=10, pady=10, fill="both", expand=True)

ventana.mainloop()
