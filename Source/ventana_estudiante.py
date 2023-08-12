import tkinter as tk
import main
import util.generic as utl
from tkinter import PhotoImage, Label, Frame, messagebox


def ventana_estudiante(id_estudiante, nombre_estudiante):

    ventana_estudiante = tk.Toplevel()
    ventana_estudiante.title("Ventana para Estudiantes")
    ventana_estudiante.geometry("925x500+300+200")
    utl.centrar_ventana(ventana_estudiante, 925, 500)
    ventana_estudiante.resizable(width=0, height=0)
    ventana_estudiante.configure(bg="#fff" )
    ventana_estudiante.resizable (False, False)

    img = PhotoImage(file='source/img/students.png')
    Label(ventana_estudiante, image=img, bg='white').place(x=495,y=75)

    img2 = tk.PhotoImage(file='source/img/apagar.png')
    boton_cerrar_sesion = tk.Label(ventana_estudiante, image=img2, bg='white', cursor='hand2')
    boton_cerrar_sesion.place(x=885, y=460)

    boton_cerrar_sesion.bind("<Button-1>", lambda e: cerrar_sesion())

    def cerrar_sesion():
        respuesta = messagebox.askyesno("Cerrar Sesión", "¿Estás seguro que quieres cerrar la sesión?")
        if respuesta:
            ventana_estudiante.destroy()  # Cierra la ventana actual
            # main.ventana_login()

    mensaje = f"Soy un estudiante\nID: {id_estudiante}\nNombre: {nombre_estudiante}"
    heading=Label(ventana_estudiante, text=f'Bienvenido {nombre_estudiante}', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',19,'bold'))
    heading.place(x=560,y=15)

    frame=Frame(ventana_estudiante, width=400, height=450,bg='red')
    frame.place(x=50,y=20)

    # Elevar la ventana al frente al crearla
    ventana_estudiante.lift()
    # Mostrar la ventana
    ventana_estudiante.mainloop()