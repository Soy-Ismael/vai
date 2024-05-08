import tkinter as tk
from tkinter import ttk
import subprocess

class Formulario1(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text="Este es el formulario 1")
        self.label.pack(pady=10)

        # Crear el botón circular grande
        self.btn_ejecutar = ttk.Button(self, text="Ejecutar", command=self.ejecutar_funcion)
        self.btn_ejecutar.config(style="Circular.TButton")  # Aplicar estilo personalizado
        self.btn_ejecutar.pack(pady=10)

    def ejecutar_funcion(self):
            subprocess.Popen(['python', 'dev/va.py'])
        

# Crear un estilo personalizado para el botón circular grande
def create_circle_button_style():
    style = ttk.Style()
    style.theme_use('default')

    # Define el estilo del botón circular
    style.layout("Circular.TButton",
                [('Button.focus', {'children': [('Button.border', {'border': '2', 'children': [('Button.padding', {'children': [('Button.label', {'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})], 'border': '6', 'sticky': 'nswe'})])

    # Crea el efecto de botón circular
    style.configure("Circular.TButton", foreground="black", background="white", bordercolor="black", font=('Arial', 12))  # Tamaño de fuente más grande

if __name__ == "__main__":
    # Crear el estilo del botón circular
    create_circle_button_style()
