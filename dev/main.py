import tkinter as tk
from tkinter import ttk
import formulario_1
import formulario_2

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interfaz con Menú y Formularios")
        self.geometry("600x400")

        # Crear el menú de navegación
        self.navigation_menu = ttk.Frame(self, width=100, height=400, relief="raised", padding=(5, 5))
        self.navigation_menu.grid(row=0, column=0, sticky="nsw")

        self.formulario_selector = ttk.Combobox(self.navigation_menu, values=["Formulario 1", "Formulario 2"])
        self.formulario_selector.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.formulario_selector.bind("<<ComboboxSelected>>", self.switch_form)

        # Crear el contenedor para los formularios
        self.form_container = ttk.Frame(self, width=500, height=400, relief="sunken", padding=(5, 5))
        self.form_container.grid(row=0, column=1, sticky="nsew")

        # Inicializar self.current_form como None
        self.current_form = None

    def switch_form(self, event=None):
        # Verificar si self.current_form ya existe antes de destruirlo
        if self.current_form:
            self.current_form.destroy()

        # Crear y mostrar el nuevo formulario seleccionado
        if self.formulario_selector.get() == "Formulario 1":
            self.current_form = formulario_1.Formulario1(self.form_container)
        elif self.formulario_selector.get() == "Formulario 2":
            self.current_form = formulario_2.Formulario2(self.form_container)

        self.current_form.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()