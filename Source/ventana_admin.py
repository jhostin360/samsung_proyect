from tkinter import *
from tkinter import ttk
import tkinter as tk
import util.generic as utl
from tkinter import LabelFrame, PhotoImage, Label, Frame, messagebox
from Conexion import *



def ventana_admin():

    def cargar_datos():

        cursor = connection.cursor()

        # Consulta para obtener profesores y cantidad de estudiantes
        query = """
       SELECT p.nombre, p.apellido, p.usuario, p.contrasena, COUNT(a.id_alumnos) AS cantidad_estudiantes
    FROM profesores p
    LEFT JOIN alumnos a ON p.id_profesores = a.fk_id_profesores
    GROUP BY p.id_profesores, p.nombre, p.apellido, p.usuario, p.contrasena
        """
        cursor.execute(query)
        profesores = cursor.fetchall()

        for profesor in profesores:
            tree.insert("", "end", values=(profesor[0], profesor[1], profesor[2], profesor[3], profesor[4]))

    def cargar_datos_alumnos():

        cursor = connection.cursor()

        # Consulta para obtener alumnos y su profesor
        query = """
        SELECT a.nombre, a.apellido, a.usuario, a.contrasena, p.nombre AS nombre_profesor, p.apellido AS apellido_profesor
        FROM alumnos a
        LEFT JOIN profesores p ON a.fk_id_profesores = p.id_profesores
        """
        cursor.execute(query)
        alumnos = cursor.fetchall()

        for alumno in alumnos:
            tree_alumnos.insert("", "end", values=(alumno[0], alumno[1], alumno[2], alumno[3], alumno[4] + " " + alumno[5]))

    def cargar_datos_calificaciones():
        cursor = connection.cursor()

        # Consulta para obtener calificaciones y el promedio calculado en la base de datos
        query = """
        SELECT a.nombre, a.apellido, c.Primer_examen, c.Segundo_examen, c.Tercer_examen, c.Examen_final, 
            (c.Primer_examen + c.Segundo_examen + c.Tercer_examen + c.Examen_final) / 4 as Promedio
        FROM calificaciones c
        INNER JOIN alumnos a ON c.id_alumnos = a.id_alumnos
        """
        cursor.execute(query)
        calificaciones = cursor.fetchall()

        for calificacion in calificaciones:
            nombre_completo = calificacion[0] + " " + calificacion[1]  # Concatenar nombre y apellido
            primer_examen = calificacion[2]
            segundo_examen = calificacion[3]
            tercer_examen = calificacion[4]
            examen_final = calificacion[5]
            promedio = calificacion[6]
            
            # Insertar en la tabla
            tree_calificaciones.insert("", "end", values=(nombre_completo, primer_examen, segundo_examen, tercer_examen, examen_final, promedio))
            
    ventana_admin = tk.Toplevel()
    ventana_admin.title('Ventana Administradores')
    ventana_admin.geometry('1200x700')
    ventana_admin.configure(bg="#fff")
    ventana_admin.resizable(False, False)
    utl.centrar_ventana(ventana_admin, 1200, 700)

    # Crear los frames para dividir la ventana
    frame1 = Frame(ventana_admin, bg='white', highlightthickness=1, highlightbackground="black")
    frame2 = Frame(ventana_admin, bg='white')
    frame3 = Frame(ventana_admin, bg='white')

    # Configurar dimensiones y posiciones de los frames usando el método place
    frame1.place(x=10, y=10, width=650, height=380)
    frame2.place(x=670, y=10, width=520, height=380)
    frame3.place(x=10, y=400, width=1180, height=280)

    #Image principal
    img = PhotoImage(file='source/img/admin.png')
    Label(frame2, image=img, bg='white').place(x=35,y=15)

    # Crear el notebook y sus pestañas
    notebook = ttk.Notebook(frame3)
    tab1 = Frame(notebook)
    tab2 = Frame(notebook)
    tab3 = Frame(notebook)
    notebook.add(tab1, text='Profesores')
    notebook.add(tab2, text='Estudiantes')
    notebook.add(tab3, text='Calificaciones')
    notebook.place(x=10, y=10)  # Establecer la posición del notebook dentro de frame3

    #Label(tab1, text='Estos son los Profesores en el tab 1', width=164, height=15, bg='white').pack()
    # Tabla para mostrar profesores y cantidad de estudiantes
    tree = ttk.Treeview(tab1, columns=("Nombre", "Apellido", "Usuario", "Contraseña", "Cantidad Estudiantes"), show="headings")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("Usuario", text="Usuario")
    tree.heading("Contraseña", text="Contraseña")
    tree.heading("Cantidad Estudiantes", text="Cantidad Estudiantes")
    tree.pack()
    cargar_datos()

    # Tabla para mostrar alumnos y su profesor
    tree_alumnos = ttk.Treeview(tab2, columns=("Nombre", "Apellido", "Usuario", "Contraseña", "Profesor"), show="headings")
    tree_alumnos.heading("Nombre", text="Nombre")
    tree_alumnos.heading("Apellido", text="Apellido")
    tree_alumnos.heading("Usuario", text="Usuario")
    tree_alumnos.heading("Contraseña", text="Contraseña")
    tree_alumnos.heading("Profesor", text="Profesor")
    tree_alumnos.pack()
    cargar_datos_alumnos()

    # Tabla para mostrar calificaciones y nombre/apellido de estudiantes
    tree_calificaciones = ttk.Treeview(tab3, columns=("Nombre", "Primer Examen", "Segundo Examen", "Tercer Examen", "Examen Final", "Promedio"), show="headings")
    tree_calificaciones.heading("Nombre", text="Nombre")
    tree_calificaciones.heading("Primer Examen", text="Primer Examen")
    tree_calificaciones.heading("Segundo Examen", text="Segundo Examen")
    tree_calificaciones.heading("Tercer Examen", text="Tercer Examen")
    tree_calificaciones.heading("Examen Final", text="Examen Final")
    tree_calificaciones.heading("Promedio", text="Promedio")
    tree_calificaciones.pack()
    cargar_datos_calificaciones()

    # Configurar pesos para que frame3 ocupe el espacio restante
    ventana_admin.grid_rowconfigure(0, weight=1)
    ventana_admin.grid_rowconfigure(1, weight=1)
    ventana_admin.grid_columnconfigure(0, weight=1)
    ventana_admin.grid_columnconfigure(1, weight=1)

    ventana_admin.mainloop()