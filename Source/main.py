from tkinter import *
from tkinter import ttk
from Conexion import *
from tkinter import messagebox
from Datos import *
import util.generic as utl
import time
import locale
from tkinter import Tk, Label, Frame
import pandas as pd
import openpyxl
import os
import ventana_estudiante


nombre_profesor = ""
id_profesor_global = 0
nombre_estudiante = ""
id_estudiante_global = 0
img = None

def update_clock(label):
    locale.setlocale(locale.LC_TIME, "es_ES")
    now = time.strftime("%A %H:%M:%S")
    label.configure(text=now)
    label.after(1000, lambda: update_clock(label))


def abrir_ventana_principal():
    #login.withdraw()  # Oculta la ventana de inicio de sesión
    ventana_principal()  # Muestra la ventana principal

def abrir_ventana_estudiante(i,n):
    ventana_estudiante.ventana_estudiante(i,n)


def ventana_principal():
    global nombre_profesor
    global login
    global ventana
    #abrir ventana principal
    ventana = Tk()
    ventana.title("Gestion de Estudiantes - PROFESORES")
    ventana.geometry("1100x650")
    utl.centrar_ventana(ventana, 1100, 650)
    ventana.resizable(width=0, height=0)

    # Header
    header_frame = Frame(ventana, bg='#2D6051', height=220)
    header_frame.pack(fill='x')

    header_content = Frame(header_frame, bg='#2D6051')
    header_content.pack(fill='both', expand=True)

    header_label_left = Label(header_content, text=f"Bienvenido, {nombre_profesor}", font=('Microsoft YaHei UI Light',18,'bold'), fg='white', bg='#2D6051')
    header_label_left.pack(side='left', padx=10, pady=10)

    current_time_label = Label(header_content, text="", font=('Microsoft YaHei UI Light',18,'bold'), fg='white', bg='#2D6051')
    current_time_label.pack(side='right', padx=10, pady=10)

    def cerrar_sesion():
        # Preguntar si realmente desea cerrar sesión
        respuesta = messagebox.askyesno("Cerrar Sesión", "¿Desea cerrar sesión?")
        # Si el usuario hace clic en "Yes", cerrar la ventana actual (ventana principal)
        if respuesta:
            ventana.destroy()
            # ventana_login()

    btn_cerrar_sesion = Button(ventana, text='Cerrar Sesion', bg='#dc3545', fg='white', border=0, cursor='hand2', command=cerrar_sesion)
    btn_cerrar_sesion.place(x=1011, y=625)

    # Actualizar la hora cada segundo
    update_clock(current_time_label)

    #Instancias
    cursor = connection.cursor()

    #marco que encierra el primer formulario y la tabla
    marco= LabelFrame(ventana, text="Formulario de estudiantes")
    marco.place(x=25,y=80, width=1050, height=500)

    #Funcion para seleccionar estudiantes
    def seleccionar_estudiante(event):
        mostrar_boton()
        item = tvEstudiantes.selection()
        if item:
            # Obtener los datos del estudiante seleccionado desde la tabla
            datos_estudiante = tvEstudiantes.item(item, "values")
            if datos_estudiante:
                id_alumnos, nombre, apellido, sexo, primer_examen, segundo_examen, tercer_examen, examen_final, promedio = datos_estudiante

                # Actualizar los campos de entrada con los datos del estudiante seleccionado
                txt_id_alumnos.config(state='normal')
                txt_id_alumnos.delete(0, END)
                txt_id_alumnos.insert(0, id_alumnos)
                txt_id_alumnos.config(state='disabled')

                txt_Nombre.delete(0, END)
                txt_Nombre.insert(0, nombre)

                txt_Apellido.delete(0, END)
                txt_Apellido.insert(0, apellido)

                txt_Sexo.delete(0, END)
                txt_Sexo.insert(0, sexo)

                txt_Primer_examen.delete(0, END)
                txt_Primer_examen.insert(0, primer_examen)

                txt_Segundo_examen.delete(0, END)
                txt_Segundo_examen.insert(0, segundo_examen)

                txt_Tercer_examen.delete(0, END)
                txt_Tercer_examen.insert(0, tercer_examen)

                txt_Examen_final.delete(0, END)
                txt_Examen_final.insert(0, examen_final)

    def exportar_a_excel(workbook):
        # Guardar el archivo Excel
        workbook.save("datos_estudiantes.xlsx")
        ruta_archivo = os.path.abspath("datos_estudiantes.xlsx")
        os.startfile(ruta_archivo)

    def boton_exportar_click():
        workbook = llenar_tabla()  # Llenar la tabla y obtener el objeto workbook
        exportar_a_excel(workbook)
    #labels aqui se recogen los datos
    estilo_inputs = {
        "background": "#fff",  # Color de fondo
        "foreground": "#333333",  # Color del texto
        "font": ("Times", 12),    # Fuente y tamaño del texto
        "width": 33,
    }
    estilo_labels = {
        "foreground": "#000",
        "font":('Times', 11)
    }

    lbl_id_alumnos =Label(marco, text="ID:",**estilo_labels).grid(column=0, row=0, padx=5, pady=5)
    txt_id_alumnos =Entry(marco, textvariable="id_alumnos", state='readonly',**estilo_inputs)
    txt_id_alumnos.grid(column=1, row=0)

    lbl_Nombre =Label(marco, text="Nombre:",**estilo_labels).grid(column=0, row=1, padx=5, pady=5)
    txt_Nombre =Entry(marco, textvariable="nombre",**estilo_inputs)
    txt_Nombre.grid(column=1, row=1)

    lbl_Apellido =Label(marco, text="Apellido:",**estilo_labels).grid(column=0, row=2, padx=5, pady=5)
    txt_Apellido =Entry(marco, textvariable="apellido",**estilo_inputs)
    txt_Apellido.grid(column=1, row=2)

    lbl_Sexo =Label(marco, text="Sexo:",**estilo_labels).grid(column=0, row=3, padx=5, pady=5)
    txt_Sexo =ttk.Combobox(marco, values=["Hombre", "Mujer"],  textvariable=Datos().set_sexo,**estilo_inputs,w=31)
    txt_Sexo.grid(column=1, row=3)
    txt_Sexo.current(0)

    lbl_Primer_examen =Label(marco, text="Primer Examen:",**estilo_labels).grid(column=2, row=0, padx=5, pady=5)
    txt_Primer_examen =Entry(marco, textvariable="primer_examen",**estilo_inputs)
    txt_Primer_examen.grid(column=3, row=0)

    lbl_Segundo_examen =Label(marco, text="Segundo Examen:",**estilo_labels).grid(column=2, row=1, padx=5, pady=5)
    txt_Segundo_examen =Entry(marco, textvariable="segundo_examen",**estilo_inputs)
    txt_Segundo_examen.grid(column=3, row=1)

    lbl_Tercer_examen =Label(marco, text="Tercer Examen:",**estilo_labels).grid(column=2, row=2, padx=5, pady=5)
    txt_Tercer_examen =Entry(marco, textvariable="tercer_examen",**estilo_inputs)
    txt_Tercer_examen.grid(column=3, row=2)

    lbl_Examen_final =Label(marco, text="Examen Final:",**estilo_labels).grid(column=2, row=3, padx=5, pady=5)
    txt_Examen_final =Entry(marco, textvariable="examen_final",**estilo_inputs)
    txt_Examen_final.grid(column=3, row=3)

    #tabla de estudiantes

    tvEstudiantes =ttk.Treeview(marco)
    tvEstudiantes.grid(column=0, row=6, columnspan=5, padx=5)
    tvEstudiantes["columns"]=("Id", "Nombre", "Apellido", "Sexo", "Primer Examen", "Segundo Examen", "Tercer Examen", "Examen Final", "Promedio")
    tvEstudiantes.column("#0", width=0, stretch=NO)

    tvEstudiantes.column("Id", width=40, anchor=CENTER)
    tvEstudiantes.column("Nombre", width=100, anchor=CENTER)
    tvEstudiantes.column("Apellido", width=100, anchor=CENTER)
    tvEstudiantes.column("Sexo", width=80, anchor=CENTER)
    tvEstudiantes.column("Primer Examen", width=100, anchor=CENTER)
    tvEstudiantes.column("Segundo Examen", width=100, anchor=CENTER)
    tvEstudiantes.column("Tercer Examen", width=100, anchor=CENTER)
    tvEstudiantes.column("Examen Final", width=100, anchor=CENTER)
    tvEstudiantes.column("Promedio", width=90, anchor=CENTER)

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

    tvEstudiantes.bind("<<TreeviewSelect>>", seleccionar_estudiante)

    #controls
    controls= LabelFrame(ventana, text="Controles")
    controls.place(x=870,y=95, width=182, height=300)

    #botones
    btnEliminar = Button(controls, width=23, pady=7, text='Eliminar', bg='#dc3545', fg='white', border=0, command=lambda:eliminar_estudiante())
    btnEliminar.grid(column=6, row=3, pady=5, padx=5)

    btnNuevo = Button(controls, width=23, pady=7, text='Agregar Estudiantes', bg='#57a1f8', fg='white', border=0, command=lambda:agregar_estudiante())
    btnNuevo.grid(column=6, row=0, pady=5, padx=5)

    btnNuevoC = Button(controls, width=23, pady=7, text='Agregar Calificaciones', bg='#4898F6', fg='white', border=0, command=lambda:agregar_calificaciones())
    btnNuevoC.grid(column=6, row=1, pady=5, padx=5)

    btnModificar = Button(controls, width=23, pady=7, text='Modificar alumno', bg='#198754', fg='white', border=0, command=lambda:editar_estudiantes())
    btnModificar.grid(column=6, row=2, pady=5, padx=5)

    btnLimpiar = Button(controls, width=23, pady=7, text='Limpiar Campos', bg='#ffc107', fg='white', border=0, command=lambda:vaciar_inputs())
    btnLimpiar.grid(column=6, row=4, pady=5, padx=5)

    btnExportar = Button(controls, width=23, pady=7, text="Exportar a Excel", bg='#2D6051', fg='white', border=0, command=lambda:boton_exportar_click())
    btnExportar.grid(column=6, row=5, pady=5, padx=5)

    #funciones de llenar, vaciar, eliminar etc
  
    def vaciar_tabla():
        filas = tvEstudiantes.get_children()
        for fila in filas:
            tvEstudiantes.delete(fila)

    def editar_estudiantes():
        # Obtener los datos ingresados por el usuario
        id_alumno = txt_id_alumnos.get()
        nombre = txt_Nombre.get()
        apellido = txt_Apellido.get()
        sexo = txt_Sexo.get()
        primer_examen = txt_Primer_examen.get()
        segundo_examen = txt_Segundo_examen.get()
        tercer_examen = txt_Tercer_examen.get()
        examen_final = txt_Examen_final.get()

        # Actualizar los datos del estudiante en la base de datos
        sql_actualizar = "UPDATE alumnos SET nombre=?, apellido=?, sexo=? WHERE id_alumnos=?"
        cursor.execute(sql_actualizar, (nombre, apellido, sexo, id_alumno))

        sql_actualizar_calificaciones = "UPDATE calificaciones SET Primer_examen=?, Segundo_examen=?, Tercer_examen=?, Examen_final=? WHERE id_alumnos=?"
        cursor.execute(sql_actualizar_calificaciones, (primer_examen, segundo_examen, tercer_examen, examen_final, id_alumno))

        # Confirmar los cambios en la base de datos
        connection.commit()

        messagebox.showinfo("Editar Estudiante", "Estudiante editado exitosamente.")

        vaciar_inputs()
        # Actualizar la tabla con los datos modificados
        llenar_tabla()

    def llenar_tabla():
        vaciar_tabla()
        sql = """
            SELECT alumnos.id_alumnos, nombre, apellido, sexo, Primer_examen, Segundo_examen, Tercer_examen, Examen_final, 
                (Primer_examen + Segundo_examen + Tercer_examen + Examen_final) / 4 as Promedio 
            FROM alumnos 
            LEFT JOIN calificaciones ON alumnos.id_alumnos = calificaciones.id_alumnos
            WHERE alumnos.fk_id_profesores = ?
        """
        cursor.execute(sql, (id_profesor_global,))

        filas = cursor.fetchall()

        # Crear un archivo Excel y una hoja
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        # Insertar encabezados
        encabezados = ["ID Alumno", "Nombre", "Apellido", "Sexo", "Primer Examen", "Segundo Examen", "Tercer Examen", "Examen Final", "Promedio"]
        worksheet.append(encabezados)

        for fila in filas:
            id_alumno = fila[0]
            nombre = fila[1].strip("'")
            apellido = fila[2].strip("'")
            sexo = fila[3].strip("'")
            primer_examen = str(fila[4])
            segundo_examen = str(fila[5])
            tercer_examen = str(fila[6])
            examen_final = str(fila[7])
            promedio = str(fila[8])

            # Insertar los datos en la tabla
            tvEstudiantes.insert("", END, id_alumno, text=id_alumno, values=(
                id_alumno, nombre, apellido, sexo, primer_examen, segundo_examen, tercer_examen, examen_final, promedio
            ))
            datos_fila = [id_alumno, nombre, apellido, sexo, primer_examen, segundo_examen, tercer_examen, examen_final, promedio]
            worksheet.append(datos_fila)

        return workbook

    def vaciar_inputs():
        ocultar_boton()
        txt_id_alumnos.config(state='normal')
        txt_id_alumnos.delete(0, END)
        txt_id_alumnos.config(state='disabled')
        txt_Nombre.delete(0, END)
        txt_Apellido.delete(0, END)
        txt_Sexo.set("")  # Vaciar el combobox
        txt_Primer_examen.delete(0, END)
        txt_Segundo_examen.delete(0, END)
        txt_Tercer_examen.delete(0, END)
        txt_Examen_final.delete(0, END)

    def eliminar_estudiante():
        # Obtener el ID del estudiante seleccionado en la tabla
        seleccionado = tvEstudiantes.selection()
        if seleccionado:
            id_alumno = tvEstudiantes.item(seleccionado)['text']
            
            # Mostrar cuadro de diálogo de confirmación
            confirmar = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro que deseas eliminar este estudiante?")
            if confirmar:
                cursor = connection.cursor()
                try:
                    # Eliminar al estudiante de la base de datos
                    cursor.execute("DELETE FROM alumnos WHERE id_alumnos = ?", (id_alumno,))
                    connection.commit()
                    messagebox.showinfo("Estudiante Eliminado", "El estudiante ha sido eliminado correctamente.")
                    llenar_tabla()  # Actualizar la tabla después de eliminar al estudiante
                    vaciar_inputs() # Actualizar
                except pyodbc.Error as e:
                    messagebox.showerror("Error", "Ocurrió un error al eliminar al estudiante.")
        else:
            messagebox.showwarning("Seleccionar Estudiante", "Por favor, selecciona un estudiante para eliminar.")
    
    #funcion que contiene la segunda ventana, aqui se ingresan los datos para hacer el insert en las dos tablas

    def agregar_estudiante():
        global login
        global img

        new_student=Toplevel(login)
        new_student.title( ' Agregar Estudiantes ' )
        new_student.geometry('925x550+300+200')
        new_student.configure(bg="#fff" )
        new_student.resizable (False, False)
        utl.centrar_ventana( new_student, 925, 550)

        img = PhotoImage(file='source/img/add-estudiantes.png')
        Label(new_student, image=img, bg='white').place(x=50,y=65)

        frame=Frame(new_student, width=350, height=550,bg='white')
        frame.place(x=480,y=20)

        heading=Label(frame, text='Agregar Estudiante', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=40,y=1)
        #Nombre
        def on_enter(e):
            txt_Nombre.delete(0, 'end')

        def on_leave(e):
            name = txt_Nombre.get()
            if name == '':
                txt_Nombre.insert(0, 'Nombre')

        txt_Nombre =Entry(frame, textvariable=Datos().set_nombre, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
        txt_Nombre.place(x=25,y=80)
        txt_Nombre.insert(0, 'Nombre')
        txt_Nombre.bind('<FocusIn>', on_enter)
        txt_Nombre.bind('<FocusOut>', on_leave)
        Frame(frame, width=350, height=2, bg='black').place(x=25,y=107)
        #Apellido
        def on_enter(e):
            txt_Apellido.delete(0, 'end')

        def on_leave(e):
            name = txt_Apellido.get()
            if name == '':
                txt_Apellido.insert(0, 'Apellido')

        txt_Apellido =Entry(frame, textvariable=Datos().set_apellido, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
        txt_Apellido.place(x=25,y=150)
        txt_Apellido.insert(0, 'Apellido')
        txt_Apellido.bind('<FocusIn>', on_enter)
        txt_Apellido.bind('<FocusOut>', on_leave)
        Frame(frame, width=350, height=2, bg='black').place(x=25,y=177)

        #Sexo
        txt_Sexo = ttk.Combobox(frame, values=["Hombre", "Mujer"], textvariable=Datos().set_sexo, width=37, font=('Microsoft YaHei UI Light',11))
        txt_Sexo.place(x=25,y=220)
        txt_Sexo.insert(0, 'Seleccione el sexo')
        
        #Usuario
        def on_enter(e):
            txt_Usuario.delete(0, 'end')

        def on_leave(e):
            name = txt_Usuario.get()
            if name == '':
                txt_Usuario.insert(0, 'Usuario')

        txt_Usuario =Entry(frame, textvariable=Datos().set_usuario, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
        txt_Usuario.place(x=25,y=290)
        txt_Usuario.insert(0, 'Usuario')
        txt_Usuario.bind('<FocusIn>', on_enter)
        txt_Usuario.bind('<FocusOut>', on_leave)
        Frame(frame, width=350, height=2, bg='black').place(x=25,y=317)
        #Crontrasena
        def on_enter(e):
            txt_Contrasena = e.widget
            if txt_Contrasena.get() == 'Contrasena':
                txt_Contrasena.delete(0, 'end')
                txt_Contrasena.config(show="*")

        def on_leave(e):
            txt_Contrasena = e.widget
            if txt_Contrasena.get() == '':
                txt_Contrasena.insert(0, 'Contrasena')
                txt_Contrasena.config(show="")

        txt_Contrasena = Entry(frame, textvariable=Datos().set_contrasena, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
        txt_Contrasena.place(x=25,y=370)
        txt_Contrasena.insert(0, 'Contrasena')
        txt_Contrasena.bind('<FocusIn>', on_enter)
        txt_Contrasena.bind('<FocusOut>', on_leave)
        Frame(frame, width=350, height=2, bg='black').place(x=25,y=397)

        Button(frame, width=39, pady=7, text='Guardar', bg='#57a1f8', fg='white', border=0, command=lambda:nuevo_estudiante()).place(x=45,y=430)

        def nuevo_estudiante():
            nombre = txt_Nombre.get()
            apellido = txt_Apellido.get()
            sexo = txt_Sexo.get()
            usuario = txt_Usuario.get()
            contrasena = txt_Contrasena.get()

                # Comprobar si todos los campos están llenos
            if nombre and apellido and usuario and contrasena:
                cursor = connection.cursor()

            # Insertar el nuevo profesor en la base de datos
            try:
                cursor.execute("INSERT INTO alumnos (nombre, apellido, sexo, usuario, contrasena, fk_id_profesores) VALUES (?, ?, ?, ?, ?, ?)", (nombre, apellido, sexo, usuario, contrasena, id_profesor_global))
                connection.commit()
                messagebox.showinfo("Registro Exitoso", "El alumno ha sido registrado correctamente.")
                # Cerrar la ventana de registro después de registrar al profesor
                llenar_tabla()
                new_student.destroy()
            except pyodbc.Error as e:
                messagebox.showerror("Error", "Ocurrió un error al registrar al alumno.")

            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")
    
    def agregar_calificaciones():
        
        global login
        global img

        add_calificaciones=Toplevel(login)
        add_calificaciones.title( ' Agregar Calificaciones ' )
        add_calificaciones.geometry('925x600+300+200')
        add_calificaciones.configure(bg="#fff" )
        add_calificaciones.resizable (False, False)
        utl.centrar_ventana( add_calificaciones, 925, 600)

        img = PhotoImage(file='source/img/add-calificaciones.png')
        Label(add_calificaciones, image=img, bg='white').place(x=50,y=60)

        frame=Frame(add_calificaciones, width=400, height=550,bg='white')
        frame.place(x=480,y=25)

        heading=Label(frame, text='Agregar Calificaciones', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=5,y=5)

        def obtener_id_alumnos():
            cursor = connection.cursor()
            cursor.execute("SELECT id_alumnos FROM alumnos WHERE id_alumnos NOT IN (SELECT DISTINCT id_alumnos FROM calificaciones) AND fk_id_profesores = ?", (id_profesor_global,))            
            ids = cursor.fetchall()
            return [id[0] for id in ids]
        

        #ID
        ids_alumnos = obtener_id_alumnos()
        txt_fk_id_alumnos  = ttk.Combobox(frame, values=ids_alumnos, textvariable=Datos().set_fk_id_alumnos, width=20, font=('Microsoft YaHei UI Light',11))
        txt_fk_id_alumnos .place(x=85,y=100)
        txt_fk_id_alumnos .insert(0, 'Id de alumnos')

        #Primer examen
        def on_enter(e):
            txt_Primer_examen.delete(0, 'end')

        def on_leave(e):
            name = txt_Primer_examen.get()
            if name == '':
                txt_Primer_examen.insert(0, 'Primer examen')

        txt_Primer_examen = Entry(frame, textvariable=Datos.set_primer_examen, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
        txt_Primer_examen.place(x=20,y=170)
        txt_Primer_examen.insert(0, 'Primer examen')
        txt_Primer_examen.bind('<FocusIn>', on_enter)
        txt_Primer_examen.bind('<FocusOut>', on_leave)
        Frame(frame, width=350, height=2, bg='black').place(x=20,y=197)

       #Segundo examen
        def on_enter(e):
            txt_Segundo_examen.delete(0, 'end')

        def on_leave(e):
            name = txt_Segundo_examen.get()
            if name == '':
                txt_Segundo_examen.insert(0, 'Segundo examen')

        txt_Segundo_examen = Entry(frame, textvariable=Datos.set_segundo_examen, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
        txt_Segundo_examen.place(x=20,y=250)
        txt_Segundo_examen.insert(0, 'Segundo examen')
        txt_Segundo_examen.bind('<FocusIn>', on_enter)
        txt_Segundo_examen.bind('<FocusOut>', on_leave)
        Frame(frame, width=350, height=2, bg='black').place(x=20,y=277)

        #Tercer examen
        def on_enter(e):
            txt_Tercer_examen.delete(0, 'end')

        def on_leave(e):
            name = txt_Tercer_examen.get()
            if name == '':
                txt_Tercer_examen.insert(0, 'Tercer examen')

        txt_Tercer_examen = Entry(frame, textvariable=Datos.set_tercer_examen, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
        txt_Tercer_examen.place(x=20,y=330)
        txt_Tercer_examen.insert(0, 'Tercer examen')
        txt_Tercer_examen.bind('<FocusIn>', on_enter)
        txt_Tercer_examen.bind('<FocusOut>', on_leave)
        Frame(frame, width=350, height=2, bg='black').place(x=20,y=357)

        # Examen final
        def on_enter(e):
            txt_Examen_final.delete(0, 'end')

        def on_leave(e):
            name = txt_Examen_final.get()
            if name == '':
                txt_Examen_final.insert(0, 'Examen Final')

        txt_Examen_final = Entry(frame, textvariable=Datos.set_examen_final, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
        txt_Examen_final.place(x=20,y=410)
        txt_Examen_final.insert(0, 'Examen Final')
        txt_Examen_final.bind('<FocusIn>', on_enter)
        txt_Examen_final.bind('<FocusOut>', on_leave)
        Frame(frame, width=350, height=2, bg='black').place(x=20,y=437)

        Button(frame, width=39, pady=7, text='Agregar', bg='#57a1f8', fg='white', border=0, command=lambda:nuevo_calificacion()).place(x=45,y=474)

        def nuevo_calificacion():
            id_alumno = txt_fk_id_alumnos.get()
            primer_examen = txt_Primer_examen.get()
            segundo_examen = txt_Segundo_examen.get()
            tercer_examen = txt_Tercer_examen.get()
            examen_final = txt_Examen_final.get()

             # Comprobar si todos los campos están llenos
            if id_alumno and primer_examen and segundo_examen and tercer_examen and examen_final:
                cursor = connection.cursor()

            # Insertar el nuevo profesor en la base de datos
            try:
                cursor.execute("INSERT INTO calificaciones (id_alumnos, Primer_examen, Segundo_examen, Tercer_examen, Examen_final) VALUES (?, ?, ?, ?, ?)", (id_alumno, primer_examen, segundo_examen, tercer_examen, examen_final))
                connection.commit()
                messagebox.showinfo("Registro Exitoso", "Las calificaciones ha sido registradas correctamente.")
                llenar_tabla()
                # Cerrar la ventana de registro después de registrar al profesor
                add_calificaciones.destroy()
            except pyodbc.Error as e:
                messagebox.showerror("Error", "Ocurrió un error al registrar las calificaciones.")

            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        add_calificaciones.mainloop()
   
    #Funciones para mostrar y ocultar el boton de editar
    def ocultar_boton():
        btnModificar.grid_remove()
        btnEliminar.grid_remove()

    def mostrar_boton():
        btnModificar.grid()
        btnEliminar.grid()

    #aqui se invoca el metodo de llenar la tabla y se termina la ejecucion.
    llenar_tabla()
    ocultar_boton()
    ventana.mainloop()

def ventana_register():

    global register_window
    global login
    global img

    #login.destroy()

    def registrar_profesor():
        # Obtener los datos ingresados por el usuario
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        usuario = entry_usuario.get()
        contrasena = entry_contrasena.get()

        # Comprobar si todos los campos están llenos
        if nombre and apellido and usuario and contrasena:
            cursor = connection.cursor()

            # Insertar el nuevo profesor en la base de datos
            try:
                cursor.execute("INSERT INTO profesores (nombre, apellido, usuario, contrasena) VALUES (?, ?, ?, ?)", (nombre, apellido, usuario, contrasena))
                connection.commit()
                messagebox.showinfo("Registro Exitoso", "El profesor ha sido registrado correctamente.")
                # Cerrar la ventana de registro después de registrar al profesor
                register_window.destroy()
            except pyodbc.Error as e:
                messagebox.showerror("Error", "Ocurrió un error al registrar al profesor.")

        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    register_window = Toplevel(login)
    register_window.title("Registro de Nuevo Profesor")
    register_window.geometry('925x500+300+200')
    register_window.configure(bg="#fff" )
    register_window.resizable (False, False)
    #utl.centrar_ventana(register_window, 925, 500)

    img = PhotoImage(file='source/img/Add.png')
    Label(register_window, image=img, border=0 ,bg='white').place(x=40,y=45)

    frame2=Frame(register_window, width=350, height=450,bg='white')
    frame2.place(x=480,y=30)

    heading2=Label(frame2, text='Registrar Profesor', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
    heading2.place(x=46,y=1)


    # Campos para ingresar los datos del nuevo profesor

    #nombre
    def on_enter(e):
        entry_nombre = e.widget
        if  entry_nombre.get() == 'Nombre':
             entry_nombre.delete(0, 'end')

    def on_leave(e):
        entry_nombre = e.widget
        if  entry_nombre.get() == '':
             entry_nombre.insert(0, 'Nombre')
    entry_nombre = Entry(frame2, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
    entry_nombre.place(x=25,y=80)
    entry_nombre.insert(0, 'Nombre')
    entry_nombre.bind('<FocusIn>', on_enter)
    entry_nombre.bind('<FocusOut>', on_leave)
    Frame(frame2, width=350, height=2, bg='black').place(x=25,y=107)

    #apellido
    def on_enter(e):
        entry_apellido = e.widget
        if  entry_apellido.get() == 'Apellido':
             entry_apellido.delete(0, 'end')

    def on_leave(e):
        entry_apellido = e.widget
        if  entry_apellido.get() == '':
             entry_apellido.insert(0, 'Apellido')
    entry_apellido = Entry(frame2, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
    entry_apellido.place(x=25,y=150)
    entry_apellido.insert(0, 'Apellido')
    entry_apellido.bind('<FocusIn>', on_enter)
    entry_apellido.bind('<FocusOut>', on_leave)
    Frame(frame2, width=350, height=2, bg='black').place(x=25,y=207)

    #usuario
    def on_enter(e):
        entry_usuario = e.widget
        if entry_usuario.get() == 'Usuario':
            entry_usuario.delete(0, 'end')

    def on_leave(e):
        entry_usuario = e.widget
        if entry_usuario.get() == '':
            entry_usuario.insert(0, 'Usuario')
    entry_usuario = Entry(frame2, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
    entry_usuario.place(x=25,y=230)
    entry_usuario.insert(0, 'Usuario')
    entry_usuario.bind('<FocusIn>', on_enter)
    entry_usuario.bind('<FocusOut>', on_leave)
    Frame(frame2, width=350, height=2, bg='black').place(x=25,y=257)

    #Contrasena
    def on_enter(e):
        entry_contrasena = e.widget
        if entry_contrasena.get() == 'Contrasena':
            entry_contrasena.delete(0, 'end')
            entry_contrasena.config(show="*")

    def on_leave(e):
        entry_contrasena = e.widget
        if entry_contrasena.get() == '':
            entry_contrasena.insert(0, 'Contrasena')
            entry_contrasena.config(show="")

    entry_contrasena = Entry(frame2, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
    entry_contrasena.place(x=25,y=310)
    entry_contrasena.insert(0, 'Contrasena')
    entry_contrasena.bind('<FocusIn>', on_enter)
    entry_contrasena.bind('<FocusOut>', on_leave)
    Frame(frame2, width=350, height=2, bg='black').place(x=25,y=337)

    Button(frame2, width=39, pady=7, text='Guardar', bg='#57a1f8', fg='white', border=0, command=registrar_profesor).place(x=45,y=370)

def ventana_login():

    global login
    global register_window
    global ventana

    def validar_login():
        global nombre_profesor
        global id_profesor_global  # Agrega esta línea al comienzo de la función
        
        # Obtener los datos ingresados por el usuario
        usuario = user.get()
        contrasena = code.get()
        tipo_usuario = user_type.get()

        cursor = connection.cursor()

        # Realizar la consulta SQL para buscar el usuario ingresado
        cursor.execute("SELECT id_profesores, usuario, contrasena, nombre, apellido FROM profesores WHERE usuario = ?", (usuario,))
        resultado_profesor = cursor.fetchone()

        cursor.execute("SELECT usuario, contrasena, nombre, apellido, id_alumnos FROM alumnos WHERE usuario = ?", (usuario,))
        resultado_alumno = cursor.fetchone()

        # Comprobar si se encontró el usuario
        if tipo_usuario == "Profesor" and resultado_profesor:
            id_profesor, usuario_bd, contrasena_bd, nombre, apellido = resultado_profesor
            if contrasena == contrasena_bd:
                nombre_profesor = nombre + " " + apellido  # Almacena el nombre del profesor en la variable global
                id_profesor_global = id_profesor  # Asigna el id_profesor a la variable global
                abrir_ventana_principal()
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
        elif tipo_usuario == "Estudiante" and resultado_alumno:
            usuario_bd, contrasena_bd, nombre, apellido, id_alumno = resultado_alumno
            if contrasena == contrasena_bd:
                # Almacena el nombre y el id del estudiante en las variables globales
                nombre_estudiante = nombre + " " + apellido
                id_estudiante_global = id_alumno
                abrir_ventana_estudiante(id_estudiante_global, nombre_estudiante)
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    login = Tk()
    login.title( ' Login ' )
    login.geometry('925x500+300+200')
    login.configure(bg="#fff" )
    login.resizable (False, False)
    utl.centrar_ventana(login, 925, 500)

    img = PhotoImage(file='source/img/login.png')
    Label(login, image=img, bg='white').place(x=50,y=35)

    frame=Frame(login, width=350, height=350,bg='white')
    frame.place(x=480,y=70)

    heading=Label(frame, text='Iniciar Sesion', fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=80,y=5)

    # Agregar un Radiobutton para seleccionar el tipo de usuario
    user_type = StringVar()
    user_type.set("Profesor")
    profesor_radio = Radiobutton(frame, text="Profesor", fg='black',bg='white', font=('Microsoft YaHei UI Light',11), variable=user_type, value="Profesor")
    profesor_radio.place(x=75,y=204)
    estudiante_radio = Radiobutton(frame, text="Alumno", fg='black',bg='white', font=('Microsoft YaHei UI Light',11), variable=user_type, value="Estudiante")
    estudiante_radio.place(x=175,y=204)

    def on_enter(e):
        user = e.widget
        if user.get() == 'Usuario':
            user.delete(0, 'end')

    def on_leave(e):
        user = e.widget
        if user.get() == '':
            user.insert(0, 'Usuario')

    #User
    user = Entry(frame, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
    user.place(x=25,y=80)
    user.insert(0, 'Usuario')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=350, height=2, bg='black').place(x=25,y=107)

    #Password
    def on_enter(e):
        code = e.widget
        if code.get() == 'Contrasena':
            code.delete(0, 'end')
            code.config(show="*")

    def on_leave(e):
        code = e.widget
        if code.get() == '':
            code.insert(0, 'Contrasena')
            code.config(show="")


    code = Entry(frame, width=25, fg='black',bg='white', border=0, font=('Microsoft YaHei UI Light',11))
    code.place(x=25,y=150)
    code.insert(0, 'Contrasena')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=350, height=2, bg='black').place(x=25,y=177)

    #Button
    Button(frame, width=39, pady=7, text='Iniciar Sesion', bg='#57a1f8', fg='white', border=0, command=validar_login).place(x=44,y=270)

    # label=Label(frame, text='No tienes una cuenta?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    # label.place(x=75,y=270)

    # sign = Button(frame, width=7,text='Registrate', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=ventana_register)
    # sign.place(x=210,y=270)

    login.mainloop()
# Llamada a la función para mostrar la ventana de inicio de sesión al inicio
if __name__ == "__main__":
    ventana_login()