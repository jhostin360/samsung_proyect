from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.title("Gestion de Estudiantes - PROFESORES")
ventana.geometry("600x600")

nombre =StringVar()

marco= LabelFrame(ventana, text="Formulario de estudiantes")
marco.place(x=50,y=50, width=500, height=500)

lbl_nombre =Label(marco, text="nombre").grid(column=0, row=0, padx=5, pady=5)
txt_nombre =Entry(marco, textvariable=nombre)
txt_nombre.grid(column=1, row=0)

btnNuevo = Button(marco, text="prueba", command=lambda:nuevo_estudiante())
btnNuevo.grid(column=0, row=6, pady=5, padx=5)

def nuevo_estudiante():
    print("Mi nombre es ", nombre)

ventana.mainloop()