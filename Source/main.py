from tkinter import *
from tkinter import ttk
from Conexion import *

ventana=Tk()
ventana.title("Gestion de Estudiantes - PROFESORES")
ventana.geometry("600x600")

marco= LabelFrame(ventana, text="Formulario de estudiantes")
marco.place(x=50,y=50, width=500, height=500)

#variables

cursor = connection.cursor()

id =StringVar()
nombre =StringVar()
apellido =StringVar()
sexo =StringVar()

primer_examen =int()
segundo_examen =int()
tercero_examen =int()
examen_final =int()
promedio =int()

#labels

lbl_id =Label(marco, text="Id").grid(column=0, row=0, padx=5, pady=5)
txt_id =Entry(marco, textvariable=id)
txt_id.grid(column=1, row=0)

lbl_Nombre =Label(marco, text="Nombre").grid(column=0, row=1, padx=5, pady=5)
txt_Nombre =Entry(marco, textvariable=nombre)
txt_Nombre.grid(column=1, row=1)

lbl_Apellido =Label(marco, text="Apellido").grid(column=2, row=0, padx=5, pady=5)
txt_Apellido =Entry(marco, textvariable=apellido)
txt_Apellido.grid(column=3, row=0)

lbl_Sexo =Label(marco, text="Sexo").grid(column=2, row=1, padx=5, pady=5)
txt_Sexo =Entry(marco, textvariable=sexo)
txt_Sexo.grid(column=3, row=1)

lbl_Primer_examen =Label(marco, text="Primer Examen").grid(column=0, row=2, padx=5, pady=5)
txt_Primer_examen =Entry(marco, textvariable=primer_examen)
txt_Primer_examen.grid(column=1, row=2)

lbl_Segundo_examen =Label(marco, text="Segundo Examen").grid(column=2, row=2, padx=5, pady=5)
txt_Segundo_examen =Entry(marco, textvariable=segundo_examen)
txt_Segundo_examen.grid(column=3, row=2)

lbl_Tercer_examen =Label(marco, text="Tercer Examen").grid(column=0, row=3, padx=5, pady=5)
txt_Tercer_examen =Entry(marco, textvariable=tercero_examen)
txt_Tercer_examen.grid(column=1, row=3)

lbl_Examen_final =Label(marco, text="Examen Final").grid(column=2, row=3, padx=5, pady=5)
txt_Examen_final =Entry(marco, textvariable=examen_final)
txt_Examen_final.grid(column=3, row=3)

lbl_Promedio =Label(marco, text="Promedio").grid(column=0, row=4, padx=5, pady=5)
txt_Promedio =Entry(marco, textvariable=promedio)
txt_Promedio.grid(column=1, row=4)

#tabla de estudiantes

tvEstudiantes =ttk.Treeview(marco)
tvEstudiantes.grid(column=0, row=5, columnspan=5, padx=5)
tvEstudiantes["columns"]=("Id", "Nombre", "Apellido", "Sexo", "Primer Examen", "Segundo Examen", "Tercer Examen", "Examen Final", "Promedio")
tvEstudiantes.column("#0", width=0, stretch=NO)

tvEstudiantes.column("Id", width=30, anchor=CENTER)
tvEstudiantes.column("Nombre", width=55, anchor=CENTER)
tvEstudiantes.column("Apellido", width=55, anchor=CENTER)
tvEstudiantes.column("Sexo", width=50, anchor=CENTER)
tvEstudiantes.column("Primer Examen", width=60, anchor=CENTER)
tvEstudiantes.column("Segundo Examen", width=60, anchor=CENTER)
tvEstudiantes.column("Tercer Examen", width=60, anchor=CENTER)
tvEstudiantes.column("Examen Final", width=60, anchor=CENTER)
tvEstudiantes.column("Promedio", width=50, anchor=CENTER)

tvEstudiantes.heading("#0", text="")

tvEstudiantes.heading("Id", text="Id", anchor=CENTER)
tvEstudiantes.heading("Nombre", text="Nombre", anchor=CENTER)
tvEstudiantes.heading("Apellido", text="Apellido", anchor=CENTER)
tvEstudiantes.heading("Sexo", text="Sexo", anchor=CENTER)
tvEstudiantes.heading("Primer Examen", text="Primer Examen", anchor=CENTER)
tvEstudiantes.heading("Segundo Examen", text="Segundo Examen", anchor=CENTER)
tvEstudiantes.heading("Tercer Examen", text="Tercer Examen", anchor=CENTER)
tvEstudiantes.heading("Examen Final", text="Examen Final", anchor=CENTER)
tvEstudiantes.heading("Promedio", text="Promedio", anchor=CENTER)

#botones

btnEliminar = Button(marco, text="Eliminar Estudiante", command=lambda:eliminar_estudiante())
btnEliminar.grid(column=0, row=6, pady=5, padx=5)

btnEliminar = Button(marco, text="Eliminar Calificaciones", command=lambda:eliminar_estudiante())
btnEliminar.grid(column=0, row=6, pady=5, padx=5)

btnNuevo = Button(marco, text="Agregar", command=lambda:nuevo())
btnNuevo.grid(column=1, row=6, pady=5, padx=5)

btnModificar = Button(marco, text="Modificar", command=lambda:modificar())
btnModificar.grid(column=2, row=6, pady=5, padx=5)

#funciones

def vaciar_tabla():
    filas = tvEstudiantes.get_children()
    for fila in filas:
        tvEstudiantes.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    sql="SELECT id_alumnos, nombre, apellido, sexo, Primer_examen, Segundo_examen, Tercer_examen, Examen_final, Promedio FROM alumnos, calificaciones Where foreign_id_alumnos = id_alumnos"
    cursor.execute(sql)
    filas = cursor.fetchall()
    for fila in filas:
        id = fila[0]
        tvEstudiantes.insert("", END, id, text= id, values= fila)

def eliminar_estudiante():
    pass

def eliminar_calificaciones():
    pass

def nuevo():
    pass

def modificar():
    pass

llenar_tabla()
#hello
ventana.mainloop()