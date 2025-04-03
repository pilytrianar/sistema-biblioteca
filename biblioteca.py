import tkinter as tk
from tkinter import messagebox

usuarios = []
libros = []
prestamos = []

def registrar_usuario():
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registrar Usuario")
    ventana_registro.geometry("300x250")

    tk.Label(ventana_registro, text="ID:").pack(pady=5)
    entry_id = tk.Entry(ventana_registro)
    entry_id.pack()

    tk.Label(ventana_registro, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(ventana_registro)
    entry_nombre.pack()

    tk.Label(ventana_registro, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(ventana_registro)
    entry_correo.pack()

    def guardar_usuario():
        id_usuario = entry_id.get()
        nombre = entry_nombre.get()
        correo = entry_correo.get()

        if id_usuario and nombre and correo:
            usuarios.append({
                "id": id_usuario,
                "nombre": nombre,
                "correo": correo
            })
            messagebox.showinfo("Éxito", "Usuario registrado con éxito")
            ventana_registro.destroy()
        else:
            messagebox.showwarning("Error", "Por favor llena todos los campos")

    tk.Button(ventana_registro, text="Guardar", command=guardar_usuario).pack(pady=10)

def registrar_libro():
    ventana_libro = tk.Toplevel()
    ventana_libro.title("Registrar Libro")
    ventana_libro.geometry("300x300")

    tk.Label(ventana_libro, text="ID del libro:").pack(pady=5)
    entry_id = tk.Entry(ventana_libro)
    entry_id.pack()

    tk.Label(ventana_libro, text="Título:").pack(pady=5)
    entry_titulo = tk.Entry(ventana_libro)
    entry_titulo.pack()

    tk.Label(ventana_libro, text="Autor:").pack(pady=5)
    entry_autor = tk.Entry(ventana_libro)
    entry_autor.pack()

    tk.Label(ventana_libro, text="Categoría:").pack(pady=5)
    entry_categoria = tk.Entry(ventana_libro)
    entry_categoria.pack()

    def guardar_libro():
        id_libro = entry_id.get()
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        categoria = entry_categoria.get()

        if id_libro and titulo and autor and categoria:
            libros.append({
                "id": id_libro,
                "titulo": titulo,
                "autor": autor,
                "categoria": categoria,
                "disponible": True
            })
            messagebox.showinfo("Éxito", "Libro registrado con éxito")
            ventana_libro.destroy()
        else:
            messagebox.showwarning("Error", "Por favor llena todos los campos")

    tk.Button(ventana_libro, text="Guardar", command=guardar_libro).pack(pady=10)

def prestar_libro():
    if not usuarios or not libros:
        messagebox.showwarning("Error", "Debe haber al menos un usuario y un libro")
        return

    ventana_prestamo = tk.Toplevel()
    ventana_prestamo.title("Prestar Libro")
    ventana_prestamo.geometry("300x300")

    tk.Label(ventana_prestamo, text="Selecciona Usuario:").pack(pady=5)
    opciones_usuarios = [u["nombre"] for u in usuarios]
    usuario_var = tk.StringVar(ventana_prestamo)
    usuario_var.set(opciones_usuarios[0])
    tk.OptionMenu(ventana_prestamo, usuario_var, *opciones_usuarios).pack()

    tk.Label(ventana_prestamo, text="Selecciona Libro:").pack(pady=5)
    libros_disponibles = [l["titulo"] for l in libros if l["disponible"]]
    if not libros_disponibles:
        tk.Label(ventana_prestamo, text="(No hay libros disponibles)").pack()
        return
    libro_var = tk.StringVar(ventana_prestamo)
    libro_var.set(libros_disponibles[0])
    tk.OptionMenu(ventana_prestamo, libro_var, *libros_disponibles).pack()

    def confirmar_prestamo():
        usuario = usuario_var.get()
        libro_titulo = libro_var.get()

        for libro in libros:
            if libro["titulo"] == libro_titulo and libro["disponible"]:
                libro["disponible"] = False
                prestamos.append({
                    "usuario": usuario,
                    "libro": libro_titulo
                })
                messagebox.showinfo("Éxito", f"Libro '{libro_titulo}' prestado a {usuario}")
                ventana_prestamo.destroy()
                return

        messagebox.showwarning("Error", "El libro no está disponible")

    tk.Button(ventana_prestamo, text="Confirmar Préstamo", command=confirmar_prestamo).pack(pady=10)

def devolver_libro():
    if not prestamos:
        messagebox.showinfo("Info", "No hay libros en préstamo.")
        return

    ventana_devolver = tk.Toplevel()
    ventana_devolver.title("Devolver Libro")
    ventana_devolver.geometry("300x250")

    tk.Label(ventana_devolver, text="Selecciona préstamo a devolver:").pack(pady=5)
    prestamos_texto = [f"{p['libro']} ← {p['usuario']}" for p in prestamos]
    prestamo_var = tk.StringVar(ventana_devolver)
    prestamo_var.set(prestamos_texto[0])
    tk.OptionMenu(ventana_devolver, prestamo_var, *prestamos_texto).pack()

    def confirmar_devolucion():
        seleccionado = prestamo_var.get()
        for prestamo in prestamos:
            if f"{prestamo['libro']} ← {prestamo['usuario']}" == seleccionado:
                for libro in libros:
                    if libro["titulo"] == prestamo["libro"]:
                        libro["disponible"] = True
                        break
                prestamos.remove(prestamo)
                messagebox.showinfo("Éxito", "Libro devuelto con éxito")
                ventana_devolver.destroy()
                return

    tk.Button(ventana_devolver, text="Confirmar Devolución", command=confirmar_devolucion).pack(pady=10)

def ver_catalogo():
    if not libros:
        messagebox.showinfo("Info", "No hay libros registrados.")
        return

    ventana_catalogo = tk.Toplevel()
    ventana_catalogo.title("Catálogo de Libros")
    ventana_catalogo.geometry("400x300")

    for libro in libros:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        info = f"{libro['titulo']} - {libro['autor']} ({libro['categoria']}) - [{estado}]"
        tk.Label(ventana_catalogo, text=info).pack(anchor="w")

# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Biblioteca")
ventana.geometry("400x550")

tk.Label(ventana, text="Bienvenido al sistema", font=("Arial", 16)).pack(pady=20)

tk.Button(ventana, text="Registrar Usuario", command=registrar_usuario).pack(pady=10)
tk.Button(ventana, text="Registrar Libro", command=registrar_libro).pack(pady=10)
tk.Button(ventana, text="Prestar Libro", command=prestar_libro).pack(pady=10)
tk.Button(ventana, text="Devolver Libro", command=devolver_libro).pack(pady=10)
tk.Button(ventana, text="Ver Catálogo", command=ver_catalogo).pack(pady=10)

ventana.mainloop()
