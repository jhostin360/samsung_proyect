import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from Conexion import *
from ttkthemes import ThemedStyle
import main
import util.generic as utl
from tkinter import LabelFrame, PhotoImage, Label, Frame, messagebox
from Conexion import *
import openpyxl



def ventana_estudiante(id_estudiante, nombre_estudiante):

    def obtener_datos_estudiante():
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT a.id_alumnos, a.nombre, a.apellido, a.usuario, a.contrasena,
                       CONCAT(p.nombre, ' ', p.apellido) AS profesor,
                       c.Primer_examen, c.Segundo_examen, c.Tercer_examen, c.Examen_final, c.Promedio
                FROM alumnos a
                INNER JOIN profesores p ON a.fk_id_profesores = p.id_profesores
                LEFT JOIN calificaciones c ON a.id_alumnos = c.id_alumnos
                WHERE a.id_alumnos = ?
            """, id_estudiante)
            datos_estudiante = cursor.fetchone()
            return datos_estudiante
        except Exception as ex:
            print(ex)
            return None

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

    datos_estudiante = obtener_datos_estudiante()
    if datos_estudiante:
        id_alumno, nombre_alumno, apellido_alumno, usuario_alumno, contrasena_alumno, profesor, primer_examen, segundo_examen, tercer_examen, examen_final, promedio = datos_estudiante  

    mensaje = f"Soy un estudiante\nID: {id_alumno}\nNombre: {nombre_alumno} {apellido_alumno}\nProfesor: {profesor}\n"
    mensaje += f"Calificaciones:\nPrimer Examen: {primer_examen}\nSegundo Examen: {segundo_examen}\nTercer Examen: {tercer_examen}\nExamen Final: {examen_final}\nPromedio: {promedio}"

    def calcular_calificacion(p):
        if p > 90:
            return "A"
        elif p > 80:
            return "B"
        elif p > 70:
            return "C"
        else:
            return "D"
        

    heading=Label(ventana_estudiante, text=f'Bienvenido {nombre_estudiante}', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',19,'bold'))
    heading.place(x=560,y=15)

    frame=Frame(ventana_estudiante, width=420, height=450,bg='white')
    frame.place(x=25,y=20)

    #marco que encierra el primer formulario y la tabla
    marco = LabelFrame(frame, text="Mi perfil", bg='white')
    marco.place(x=5,y=20, width=400, height=210)

    # Crear etiquetas y campos de entrada para mostrar los datos
    label_none = Label(marco, text="", bg='white')
    label_none.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    entry_none = Label(marco, text='', bg='white')
    entry_none.grid(row=0, column=1, padx=10, pady=5)

    label_id = Label(marco, text="ID:", bg='white')
    label_id.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    entry_id = Label(marco, text=id_alumno, bg='white')
    entry_id.grid(row=1, column=1, padx=10, pady=5)

    label_nombre = Label(marco, text="Nombre:", bg='white')
    label_nombre.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    entry_nombre = Label(marco, text=nombre_alumno, bg='white')
    entry_nombre.grid(row=2, column=1, padx=10, pady=5)

    label_apellido = Label(marco, text="Apellido:", bg='white')
    label_apellido.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    entry_apellido = Label(marco, text=apellido_alumno,  bg='white')
    entry_apellido.grid(row=3, column=1, padx=10, pady=5)

    label_profesor = Label(marco, text="Profesor:", bg='white')
    label_profesor.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    label_profesor_value = Label(marco, text=profesor, bg='white')
    label_profesor_value.grid(row=4, column=1, padx=10, pady=5)

    marco_perfil_change = LabelFrame(marco, text="Credenciales", bg='white')
    marco_perfil_change.place(x=175,y=2, width=210, height=175)

    estilo_inputs = {
        "background": "#fff",  # Color de fondo
        "foreground": "#333333",  # Color del texto
        "width": 26,
    }

    def toggle_password_visibility():
        if entry_contrasena['show'] == '*':
            entry_contrasena.config(show='')
            boton_mostrar_contrasena.config(image=imagen_ocultar)
        else:
            entry_contrasena.config(show='*')
            boton_mostrar_contrasena.config(image=imagen_mostrar)

    #Instancias
    cursor = connection.cursor()

    def editar_perfil():
        respuesta = messagebox.askyesno("Actualizar Credenciales", "¿Deseas actualizar tus credenciales?")
        if respuesta:
            nuevo_usuario = entry_usuario.get()
            nueva_contrasena = entry_contrasena.get()

            # Aquí debes ejecutar la sentencia SQL UPDATE para actualizar el usuario y contraseña
            sql = "UPDATE alumnos SET usuario = ?, contrasena = ? WHERE id_alumnos = ?"
            cursor.execute(sql, (nuevo_usuario, nueva_contrasena, id_alumno))  # Reemplaza id_alumno con el ID correspondiente

            # Asegúrate de confirmar los cambios en la base de datos
            connection.commit()

            # Actualiza los campos en la interfaz gráfica
            usuario_alumno.set(nuevo_usuario)
            contrasena_alumno.set(nueva_contrasena)

    # Carga de imágenes file='source/img/apagar.png'
    imagen_mostrar = tk.PhotoImage(file='source/img/esconder.png')
    
    imagen_ocultar = tk.PhotoImage(file='source/img/vista.png')

    label_usuario = Label(marco_perfil_change, text="Usuario:", bg='white')
    label_usuario.grid(row=0, column=0, padx=10, pady=3, sticky='w')
    entry_usuario = Entry(marco_perfil_change,**estilo_inputs)
    entry_usuario.grid(row=1, column=0, padx=10, pady=3)
    entry_usuario.insert(0, usuario_alumno)

    label_contrasena = Label(marco_perfil_change, text="Contraseña:", bg='white')
    label_contrasena.grid(row=2, column=0, padx=10, pady=3, sticky='w')
    entry_contrasena = Entry(marco_perfil_change, show='*',**estilo_inputs)
    entry_contrasena.grid(row=3, column=0, padx=10, pady=3)
    entry_contrasena.insert(0, contrasena_alumno)

    boton_mostrar_contrasena = Button(marco_perfil_change, image=imagen_mostrar, bd=0, bg='white', cursor='hand2' ,command=toggle_password_visibility)
    boton_mostrar_contrasena.grid(row=3, column=1, padx=0, pady=3)

    boton_editar = Button(marco_perfil_change, width=20, pady=2, text='Editar', bg='#FFC107', fg='white', border=0, cursor='hand2',command=editar_perfil)
    boton_editar.grid(row=4, column=0, padx=10, pady=8)
   
    marco2 = LabelFrame(frame, text="Mis Calificaciones", bg='white')
    marco2.place(x=5,y=250, width=400, height=150)
    
    examen1_label = tk.Label(marco2, text='Examen 1: ',  bg='white', font=('Helvetica', 10))
    examen1_label.place(x=5, y=15,)
    examen1_input = tk.Label(marco2, text=str(primer_examen), bg='white', bd=1, relief='solid', font=('Helvetica', 10, 'bold'))
    examen1_input.place(x=78, y=15, width=26, height=26) 

    examen2_label = tk.Label(marco2, text='Examen 2: ',  bg='white', font=('Helvetica', 10))
    examen2_label.place(x=5, y=50,)
    examen2_input = tk.Label(marco2, text=str(segundo_examen), bg='white', bd=1, relief='solid', font=('Helvetica', 10, 'bold'))
    examen2_input.place(x=78, y=50, width=26, height=26) 

    examen3_label = tk.Label(marco2, text='Examen 3: ',  bg='white', font=('Helvetica', 10))
    examen3_label.place(x=5, y=85,)
    examen3_input = tk.Label(marco2, text=str(tercer_examen), bg='white', bd=1, relief='solid', font=('Helvetica', 10, 'bold'))
    examen3_input.place(x=78, y=85, width=26, height=26)

    final_label = tk.Label(marco2, text='Examen Final: ',  bg='white', font=('Helvetica', 10))
    final_label.place(x=125, y=15,)
    final_input = tk.Label(marco2, text=str(examen_final), bg='white', bd=1, relief='solid', font=('Helvetica', 10, 'bold'))
    final_input.place(x=220, y=15, width=26, height=26)

    promedio_label = tk.Label(marco2, text='Promedio: ',  bg='white', font=('Helvetica', 10))
    promedio_label.place(x=125, y=85,)
    promedio_input = tk.Label(marco2, text=str(promedio), bg='white', bd=1, relief='solid', font=('Helvetica', 10, 'bold'))
    promedio_input.place(x=220, y=85, width=26, height=26)
   
    img3 = PhotoImage(file='source/img/circular.png')
    label_img = Label(marco2, bg='white', image=img3)
    label_img.place(x=275, y=5)

    literal = calcular_calificacion(promedio)
    literal_label = Label(marco2, text=literal, bg='white', fg='#57A1F8', font=('Helvetica', 44, 'bold'))
    literal_label.place(x=300, y=22)


    boton_exportar_excel = Button(frame, pady=7, text='Exportar a Excel', bg='#2D6051', fg='white', border=0, cursor='hand2', command=lambda:exportar_excel(datos_estudiante))
    boton_exportar_excel.place(x=75, y=413, width=250)

    def exportar_excel(datos_estudiante):
        id_alumno, nombre_alumno, apellido_alumno, usuario_alumno, contrasena_alumno, profesor, primer_examen, segundo_examen, tercer_examen, examen_final, promedio = datos_estudiante

        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Datos Estudiante"

        # Encabezados de las columnas
        encabezados = ["ID", "Nombre", "Apellido", "Profesor", "Primer Examen", "Segundo Examen", "Tercer Examen", "Examen Final", "Promedio"]
        sheet.append(encabezados)

        # Agregar los datos del estudiante
        fila_estudiante = [id_alumno, nombre_alumno, apellido_alumno, profesor, primer_examen, segundo_examen, tercer_examen, examen_final, promedio]
        sheet.append(fila_estudiante)

        # Guardar el archivo Excel
        nombre_archivo = f"datos_de_{nombre_estudiante}.xlsx"
        workbook.save(nombre_archivo)
        ruta_archivo = os.path.abspath(f"datos_de_{nombre_estudiante}.xlsx")
        os.startfile(ruta_archivo)

        messagebox.showinfo("Exportar a Excel", f"Los datos se han exportado a {nombre_archivo}")



    # Elevar la ventana al frente al crearla
    ventana_estudiante.lift()
    # Mostrar la ventana
    ventana_estudiante.mainloop()