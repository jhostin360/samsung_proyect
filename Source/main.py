from tkinter import *
from tkinter import ttk
from Conexion import *
from tkinter import messagebox

#abrir ventana principal
ventana=Tk()
ventana.title("Gestion de Estudiantes - PROFESORES")
ventana.geometry("600x600")
#marco que encierra el primer formulario y la tabla
marco= LabelFrame(ventana, text="Formulario de estudiantes")
marco.place(x=50,y=50, width=500, height=500)

#variables

cursor = connection.cursor()

id =StringVar()
nombre =StringVar()
apellido =StringVar()
sexo =StringVar()
usuario =StringVar()
contrasena =StringVar()

id_calificaciones =StringVar()
fk_id_alumnos =StringVar()
primer_examen =StringVar()
segundo_examen =StringVar()
tercero_examen =StringVar()
examen_final =StringVar()
promedio =StringVar()

#labels aqui se recogen los datos

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

btnEliminar = Button(marco, text="Eliminar", command=lambda:eliminar())
btnEliminar.grid(column=0, row=6, pady=5, padx=5)

btnNuevo = Button(marco, text="Agregar", command=lambda:agregar())
btnNuevo.grid(column=1, row=6, pady=5, padx=5)

btnModificar = Button(marco, text="Modificar", command=lambda:modificar())
btnModificar.grid(column=2, row=6, pady=5, padx=5)

#funciones de llenar, vaciar, eliminar etc

def vaciar_tabla():
    filas = tvEstudiantes.get_children()
    for fila in filas:
        tvEstudiantes.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    sql="SELECT id_alumnos, nombre, apellido, sexo, Primer_examen, Segundo_examen, Tercer_examen, Examen_final, Promedio FROM alumnos, calificaciones Where fk_id_alumnos = id_alumnos"
    cursor.execute(sql)
    filas = cursor.fetchall()
    for fila in filas:
        id = fila[0]
        tvEstudiantes.insert("", END, id, text= id, values= fila)

def eliminar():
    id = tvEstudiantes.selection()[0]
    if int(id)>0:
        sql="delete from alumnos where id_alumnos="+id
        cursor.execute(sql)
        cursor.connection.commit()
        tvEstudiantes.delete(id)
        messagebox.showinfo(message="Eliminado con exito", title="Mensaje importante")
    else:
        messagebox.showinfo(message="Seleccione un registrar para eliminar", title="Mensaje importante")

def agregar():
    ventana_agregar()

def modificar():
    pass

def nuevo_estudiante():
    print(nombre, "nombre")
    print(apellido, "apellido")
    print(sexo, "sexo")
    print(usuario, "usuario")
    print(contrasena, "contrasena")
    sql="insert into alumnos values(?, ?, ?, ?, ?)"
    val = {nombre, apellido, sexo, usuario, contrasena}
    cursor.execute(sql, val)
    cursor.connection.commit()
    messagebox.showinfo(message="Se a guardado el nuevo estudiante", title="Mensaje importante")
    llenar_tabla()

def nuevo_calificacion():
    sql="insert into calificaciones (id_calificaciones, id_alumnos, Primer_examen, Segundo_examen, Tercer_examen, Examen_final, contrasena) values()"
    cursor.execute(sql)
    cursor.connection.commit()
    messagebox.showinfo(message="Se a guardado el nuevo estudiante", title="Mensaje importante")
    llenar_tabla()

#funcion que contiene la segunda ventana, aqui se ingresan los datos para hacer el insert en las dos tablas
def ventana_agregar():
    ventana_2=Tk()
    ventana_2.title("Gestion de Estudiantes - PROFESORES - Nuevo")
    ventana_2.geometry("500x600")

    #marco 1

    #labels
    marco= LabelFrame(ventana_2, text="Datos del estudiante")
    marco.place(x=50, y=50, width=400, height=250)

    lbl_Nombre =Label(marco, text="Nombre").grid(column=0, row=1, padx=5, pady=5)
    txt_Nombre =Entry(marco, textvariable=nombre)
    txt_Nombre.grid(column=1, row=1)

    lbl_Apellido =Label(marco, text="Apellido").grid(column=0, row=2, padx=5, pady=5)
    txt_Apellido =Entry(marco, textvariable=apellido)
    txt_Apellido.grid(column=1, row=2)

    lbl_Sexo =Label(marco, text="Sexo").grid(column=0, row=3, padx=5, pady=5)
    txt_Sexo =ttk.Combobox(marco, values=["Hombre", "Mujer"],  textvariable=sexo)
    txt_Sexo.grid(column=1, row=3)
    txt_Sexo.current(0)

    lbl_Usuario =Label(marco, text="Usuario").grid(column=0, row=4, padx=5, pady=5)
    txt_Usuario =Entry(marco, textvariable=usuario)
    txt_Usuario.grid(column=1, row=4)

    lbl_Contrasena =Label(marco, text="Contraseña").grid(column=0, row=5, padx=5, pady=5)
    txt_Contrasena =Entry(marco, textvariable=contrasena)
    txt_Contrasena.grid(column=1, row=5)

    #botones marco 1
    btnNuevo = Button(marco, text="Agregar", command=lambda:nuevo_estudiante())
    btnNuevo.grid(column=0, row=6, pady=5, padx=5)

    #marco 2

    #labels
    marco_2= LabelFrame(ventana_2, text="Calificaciones del estudiante")
    marco_2.place(x=50,y=300, width=400, height=250)

    lbl_id_calificaciones =Label(marco_2, text="Id").grid(column=0, row=0, padx=5, pady=5)
    txt_id_calificaciones =Entry(marco_2, textvariable=id_calificaciones)
    txt_id_calificaciones.grid(column=1, row=0)

    lbl_fk_id_alumnos =Label(marco_2, text="Id_alumnos").grid(column=0, row=0, padx=5, pady=5)
    txt_fk_id_alumnos =Entry(marco_2, textvariable=fk_id_alumnos)
    txt_fk_id_alumnos.grid(column=1, row=0)

    lbl_Primer_examen =Label(marco_2, text="Primer Examen").grid(column=0, row=1, padx=5, pady=5)
    txt_Primer_examen =Entry(marco_2, textvariable=primer_examen)
    txt_Primer_examen.grid(column=1, row=1)

    lbl_Segundo_examen =Label(marco_2, text="Segundo Examen").grid(column=0, row=2, padx=5, pady=5)
    txt_Segundo_examen =Entry(marco_2, textvariable=segundo_examen)
    txt_Segundo_examen.grid(column=1, row=2)

    lbl_Tercer_examen =Label(marco_2, text="Tercer Examen").grid(column=0, row=3, padx=5, pady=5)
    txt_Tercer_examen =Entry(marco_2, textvariable=tercero_examen)
    txt_Tercer_examen.grid(column=1, row=3)

    lbl_Examen_final =Label(marco_2, text="Examen Final").grid(column=0, row=4, padx=5, pady=5)
    txt_Examen_final =Entry(marco_2, textvariable=examen_final)
    txt_Examen_final.grid(column=1, row=4)

    #botones marco 2
    btnNuevo = Button(marco_2, text="Agregar", command=lambda:nuevo_calificacion())
    btnNuevo.grid(column=0, row=5, pady=5, padx=5)

    ventana.mainloop()

#aqui se invoca el metodo de llenar la tabla y se termina la ejecucion.
llenar_tabla()
ventana.mainloop()