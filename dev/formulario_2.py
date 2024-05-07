import tkinter as tk
from tkinter import ttk


class Formulario2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text="Este es el formulario 2")
        self.label.pack(pady=10)
