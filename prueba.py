import tkinter as tk

ventana = tk.Tk()
ventana.title("Prueba de Tkinter")
ventana.geometry("300x100")
tk.Label(ventana, text="¡Tkinter funciona!").pack(pady=20)
ventana.mainloop()
