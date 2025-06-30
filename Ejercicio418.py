import tkinter as tk
from tkinter import messagebox


# --------------------------
# Clase Programador
# --------------------------
class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


# --------------------------
# Clase EquipoMaratonProgramacion
# --------------------------
class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores = []
    
    def esta_lleno(self):
        return len(self.programadores) >= 3

    def añadir_programador(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar más programadores.")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo):
        if any(char.isdigit() for char in campo):
            raise Exception("El campo no puede contener números.")
        if len(campo) > 20:
            raise Exception("El campo no puede tener más de 20 caracteres.")


# --------------------------
# Interfaz gráfica con Tkinter
# --------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Equipo Maratón de Programación")
        self.equipo = None

        # ----- Datos del equipo -----
        tk.Label(root, text="Nombre del Equipo:").grid(row=0, column=0, sticky="e")
        tk.Label(root, text="Universidad:").grid(row=1, column=0, sticky="e")
        tk.Label(root, text="Lenguaje de Programación:").grid(row=2, column=0, sticky="e")

        self.entry_nombre_equipo = tk.Entry(root)
        self.entry_universidad = tk.Entry(root)
        self.entry_lenguaje = tk.Entry(root)

        self.entry_nombre_equipo.grid(row=0, column=1)
        self.entry_universidad.grid(row=1, column=1)
        self.entry_lenguaje.grid(row=2, column=1)

        tk.Button(root, text="Crear Equipo", command=self.crear_equipo).grid(row=3, column=0, columnspan=2, pady=5)

        # ----- Datos de los programadores -----
        tk.Label(root, text="Nombre Programador:").grid(row=4, column=0, sticky="e")
        tk.Label(root, text="Apellidos Programador:").grid(row=5, column=0, sticky="e")

        self.entry_nombre_programador = tk.Entry(root)
        self.entry_apellidos_programador = tk.Entry(root)

        self.entry_nombre_programador.grid(row=4, column=1)
        self.entry_apellidos_programador.grid(row=5, column=1)

        tk.Button(root, text="Agregar Programador", command=self.agregar_programador).grid(row=6, column=0, columnspan=2, pady=5)

        # ----- Mostrar información -----
        tk.Button(root, text="Mostrar Equipo", command=self.mostrar_equipo).grid(row=7, column=0, columnspan=2, pady=5)

        # ----- Área de salida -----
        self.text_salida = tk.Text(root, width=50, height=10, state="disabled")
        self.text_salida.grid(row=8, column=0, columnspan=2, pady=5)

    # --------------------------
    def crear_equipo(self):
        nombre = self.entry_nombre_equipo.get().strip()
        universidad = self.entry_universidad.get().strip()
        lenguaje = self.entry_lenguaje.get().strip()

        if not nombre or not universidad or not lenguaje:
            messagebox.showerror("Error", "Todos los campos del equipo son obligatorios.")
            return

        self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)
        messagebox.showinfo("Éxito", "Equipo creado correctamente.")
        self.text_salida.config(state="normal")
        self.text_salida.delete(1.0, tk.END)
        self.text_salida.insert(tk.END, f"Equipo '{nombre}' creado.\n")
        self.text_salida.config(state="disabled")

    # --------------------------
    def agregar_programador(self):
        if self.equipo is None:
            messagebox.showerror("Error", "Primero debe crear un equipo.")
            return

        nombre = self.entry_nombre_programador.get().strip()
        apellidos = self.entry_apellidos_programador.get().strip()

        try:
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)

            programador = Programador(nombre, apellidos)
            self.equipo.añadir_programador(programador)

            messagebox.showinfo("Éxito", f"Programador {nombre} {apellidos} añadido correctamente.")
            self.entry_nombre_programador.delete(0, tk.END)
            self.entry_apellidos_programador.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # --------------------------
    def mostrar_equipo(self):
        if self.equipo is None:
            messagebox.showerror("Error", "No hay equipo creado.")
            return

        self.text_salida.config(state="normal")
        self.text_salida.delete(1.0, tk.END)

        self.text_salida.insert(tk.END, f"Equipo: {self.equipo.nombre_equipo}\n")
        self.text_salida.insert(tk.END, f"Universidad: {self.equipo.universidad}\n")
        self.text_salida.insert(tk.END, f"Lenguaje: {self.equipo.lenguaje}\n")
        self.text_salida.insert(tk.END, "Programadores:\n")

        if self.equipo.programadores:
            for idx, p in enumerate(self.equipo.programadores, start=1):
                self.text_salida.insert(tk.END, f"  {idx}. {p.nombre} {p.apellidos}\n")
        else:
            self.text_salida.insert(tk.END, "  No hay programadores aún.\n")

        self.text_salida.config(state="disabled")


# --------------------------
# Ejecutar la aplicación
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
