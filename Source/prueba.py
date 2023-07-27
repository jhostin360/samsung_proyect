from tkinter import *
from tkinter import ttk

ventana=Tk()
ventana.title("Gestion de Estudiantes - PROFESORES")
ventana.geometry("600x600")

num_1 =StringVar()
num_2 = StringVar()

marco= LabelFrame(ventana, text="Formulario de estudiantes")
marco.place(x=50,y=50, width=500, height=500)

lbl_num_1 =Label(marco, text="numero 1").grid(column=0, row=0, padx=5, pady=5)
txt_num_1 =Entry(marco, textvariable=num_1)
txt_num_1.grid(column=1, row=0)

lbl_num_2 =Label(marco, text="numero 2").grid(column=0, row=1, padx=5, pady=5)
txt_num_2 =Entry(marco, textvariable=num_2)
txt_num_2.grid(column=1, row=1)

btnNuevo = Button(marco, text="abrir ventana", command=lambda:ventana_agregar())
btnNuevo.grid(column=0, row=6, pady=5, padx=5)

btnNuevo = Button(marco, text="boton prueba", command=lambda:nuevo_estudiante())
btnNuevo.grid(column=1, row=6, pady=5, padx=5)

def ventana_agregar():
    ventana_2=Tk()
    ventana_2.title("Gestion de Estudiantes - PROFESORES - Nuevo")
    ventana_2.geometry("500x600")

    #marco 1

    #labels
    marco_2= LabelFrame(ventana_2, text="Datos del estudiante")
    marco_2.place(x=50, y=50, width=400, height=250)

    lbl_num_1 =Label(marco_2, text="valor 1").grid(column=0, row=1, padx=5, pady=5)
    txt_num_1 =Entry(marco_2, textvariable=num_1)
    txt_num_1.grid(column=1, row=1)

    lbl_num_2 =Label(marco_2, text="valor 2").grid(column=0, row=2, padx=5, pady=5)
    txt_num_2 =Entry(marco_2, textvariable=num_2)
    txt_num_2.grid(column=1, row=2)

    btnNuevo = Button(marco_2, text="boton prueba", command=lambda:nuevo_estudiante())
    btnNuevo.grid(column=0, row=6, pady=5, padx=5)

def nuevo_estudiante():
    print(StringVar(num_1.get))
    print(StringVar(num_2.get))

ventana.mainloop()