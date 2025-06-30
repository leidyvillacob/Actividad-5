import tkinter as tk
from tkinter import messagebox, filedialog


# --------------------------
# Clase LeerArchivo
# --------------------------
class LeerArchivo:
    def __init__(self, ruta):
        self.ruta = ruta

    def leer_contenido(self):
        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            raise Exception("El archivo no fue encontrado.")
        except Exception as e:
            raise Exception(f"No se pudo leer el archivo: {e}")


# --------------------------
# Interfaz gráfica con Tkinter
# --------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("📄 Lector de Archivos .txt")
        self.root.configure(bg="#e6f2ff")

        # Título
        tk.Label(root, text="Lector de Archivos de Texto", font=("Arial Rounded MT Bold", 16),
                 bg="#004d99", fg="white", pady=10)\
            .grid(row=0, column=0, columnspan=3, sticky="ew")

        # Ruta del archivo
        tk.Label(root, text="Ruta del archivo:", font=("Arial", 11, "bold"), bg="#e6f2ff")\
            .grid(row=1, column=0, sticky="e", pady=5, padx=5)

        self.entry_ruta = tk.Entry(root, width=50)
        self.entry_ruta.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(root, text="📂 Buscar Archivo", bg="#007acc", fg="white", width=15,
                  command=self.buscar_archivo)\
            .grid(row=1, column=2, padx=5)

        # Botón leer
        tk.Button(root, text="📖 Leer Archivo", bg="#00b33c", fg="white", width=20,
                  command=self.leer_archivo)\
            .grid(row=2, column=0, columnspan=3, pady=10)

        # Área de texto
        tk.Label(root, text="Contenido del archivo:", font=("Arial", 11, "bold"), bg="#e6f2ff")\
            .grid(row=3, column=0, columnspan=3, sticky="w", padx=5)

        self.text_contenido = tk.Text(root, width=80, height=20, state="disabled", relief="solid", bd=1,
                                      bg="white", fg="black", font=("Consolas", 10))
        self.text_contenido.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        # Footer
        tk.Label(root, text="Desarrollado con Python & Tkinter", bg="#004d99", fg="white",
                 font=("Arial", 9), pady=4)\
            .grid(row=5, column=0, columnspan=3, sticky="ew")

    # --------------------------
    def buscar_archivo(self):
        ruta = filedialog.askopenfilename(
            title="Selecciona un archivo",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"))
        )
        if ruta:
            self.entry_ruta.delete(0, tk.END)
            self.entry_ruta.insert(0, ruta)

    # --------------------------
    def leer_archivo(self):
        ruta = self.entry_ruta.get().strip()

        if not ruta:
            messagebox.showerror("❌ Error", "Debe ingresar la ruta del archivo.")
            return

        lector = LeerArchivo(ruta)

        try:
            contenido = lector.leer_contenido()
            self.text_contenido.config(state="normal")
            self.text_contenido.delete(1.0, tk.END)
            self.text_contenido.insert(tk.END, contenido)
            self.text_contenido.config(state="disabled")
        except Exception as e:
            messagebox.showerror("❌ Error", str(e))


# --------------------------
# Ejecutar la aplicación
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
