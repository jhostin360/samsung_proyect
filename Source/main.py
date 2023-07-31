from tkinter import *
from tkinter import ttk
from Conexion import *
from tkinter import messagebox
from Datos import *
import util.generic as utl
import time
import locale
from tkinter import Tk, Label, Frame

nombre_profesor = ""
img = None

def update_clock(label):
    locale.setlocale(locale.LC_TIME, "es_ES")
    now = time.strftime("%A %H:%M:%S")
    label.configure(text=now)
    label.after(1000, lambda: update_clock(label))

def abrir_ventana_principal():
    global login  # Indicar que estamos usando la variable global
    login.withdraw()  # Oculta la ventana de inicio de sesión
    ventana_principal()  # Muestra la ventana principal

def ventana_principal():
    global nombre_profesor
    #abrir ventana principal
    ventana=Tk()
    ventana.title("Gestion de Estudiantes - PROFESORES")
    ventana.geometry("1100x650")
    utl.centrar_ventana(ventana, 1100, 650)
    ventana.resizable(width=0, height=0)

    # Header
    header_frame = Frame(ventana, bg='#57a1f8', height=100)
    header_frame.pack(fill='x')

    header_content = Frame(header_frame, bg='#57a1f8')
    header_content.pack(fill='both', expand=True)

    header_label_left = Label(header_content, text=f"Bienvenido, {nombre_profesor}", font=('Arial', 16), fg='white', bg='#57a1f8')
    header_label_left.pack(side='left', padx=10, pady=10)

    current_time_label = Label(header_content, text="", font=('Arial', 16), fg='white', bg='#57a1f8')
    current_time_label.pack(side='right', padx=10, pady=10)

    # Actualizar la hora cada segundo
    update_clock(current_time_label)

    #Instancias
    cursor = connection.cursor()

    #marco que encierra el primer formulario y la tabla
    marco= LabelFrame(ventana, text="Formulario de estudiantes")
    marco.place(x=50,y=80, width=1000, height=500)

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

    #botones
    #btnEliminar = Button(marco, text="Eliminar", bg='#dc3545', font=('Times', 13), fg="#fff", command=lambda:eliminar_estudiante())
    btnEliminar = Button(marco, width=17, pady=7, text='Eliminar', bg='#dc3545', fg='white', border=0, command=lambda:eliminar_estudiante())
    btnEliminar.grid(column=0, row=7, pady=5, padx=5)

    #btnNuevo = Button(marco, text="Agregar", bg='#0d6efd', font=('Times', 13), fg="#fff", command=lambda:agregar())
    btnNuevo = Button(marco, width=17, pady=7, text='Agregar', bg='#57a1f8', fg='white', border=0, command=lambda:agregar())
    btnNuevo.grid(column=1, row=7, pady=5, padx=5)

    #btnModificar = Button(marco, text="Modificar alumno", font=('Times', 13), bg='#198754', fg="#fff", command=lambda:editar_estudiantes())
    btnModificar = Button(marco, width=17, pady=7, text='Modificar alumno', bg='#198754', fg='white', border=0, command=lambda:editar_estudiantes())
    btnModificar.grid(column=2, row=7, pady=5, padx=5)

    #btnLimpiar = Button(marco, text="Limpiar Campos", font=('Times', 13), bg='#ffc107', fg="#fff", command=lambda:vaciar_inputs())
    btnLimpiar = Button(marco, width=17, pady=7, text='Limpiar Campos', bg='#ffc107', fg='white', border=0, command=lambda:vaciar_inputs())
    btnLimpiar.grid(column=3, row=7, pady=5, padx=5)

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
        sql = "SELECT alumnos.id_alumnos, nombre, apellido, sexo, Primer_examen, Segundo_examen, Tercer_examen, Examen_final, (Primer_examen + Segundo_examen + Tercer_examen + Examen_final) / 4 as Promedio FROM alumnos LEFT JOIN calificaciones ON alumnos.id_alumnos = calificaciones.id_alumnos"
        cursor.execute(sql)
        filas = cursor.fetchall()
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

    def agregar():
        ventana_agregar()

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
        txt_Nombre =Entry(marco, textvariable=Datos().set_nombre)
        txt_Nombre.grid(column=1, row=1)

        lbl_Apellido =Label(marco, text="Apellido").grid(column=0, row=2, padx=5, pady=5)
        txt_Apellido =Entry(marco, textvariable=Datos().set_apellido)
        txt_Apellido.grid(column=1, row=2)

        lbl_Sexo =Label(marco, text="Sexo").grid(column=0, row=3, padx=5, pady=5)
        txt_Sexo =ttk.Combobox(marco, values=["Hombre", "Mujer"],  textvariable=Datos().set_sexo)
        txt_Sexo.grid(column=1, row=3)
        txt_Sexo.current(0)

        lbl_Usuario =Label(marco, text="Usuario").grid(column=0, row=4, padx=5, pady=5)
        txt_Usuario =Entry(marco, textvariable=Datos().set_usuario)
        txt_Usuario.grid(column=1, row=4)

        lbl_Contrasena =Label(marco, text="Contraseña").grid(column=0, row=5, padx=5, pady=5)
        txt_Contrasena =Entry(marco, textvariable=Datos().set_contrasena)
        txt_Contrasena.grid(column=1, row=5)

        #botones marco 1
        btnNuevo = Button(marco, text="Agregar", command=lambda:nuevo_estudiante())
        btnNuevo.grid(column=0, row=6, pady=5, padx=5)

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
                cursor.execute("INSERT INTO alumnos (nombre, apellido, sexo, usuario, contrasena) VALUES (?, ?, ?, ?, ?)", (nombre, apellido, sexo, usuario, contrasena))
                connection.commit()
                messagebox.showinfo("Registro Exitoso", "El alumno ha sido registrado correctamente.")
                # Cerrar la ventana de registro después de registrar al profesor
                llenar_tabla()
                register_window.destroy()
            except pyodbc.Error as e:
                messagebox.showerror("Error", "Ocurrió un error al registrar al alumno.")

            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")



        #marco 2

        #labels
        marco_2= LabelFrame(ventana_2, text="Calificaciones del estudiante")
        marco_2.place(x=50,y=300, width=400, height=250)

        def obtener_id_alumnos():
            cursor = connection.cursor()
            cursor.execute("SELECT id_alumnos FROM alumnos WHERE id_alumnos NOT IN (SELECT DISTINCT id_alumnos FROM calificaciones)")
            ids = cursor.fetchall()
            return [id[0] for id in ids]

        lbl_id_calificaciones =Label(marco_2, text="Id").grid(column=0, row=0, padx=5, pady=5)
        txt_id_calificaciones =Entry(marco_2, textvariable=Datos().set_id_calificaciones)
        txt_id_calificaciones.grid(column=1, row=0)

        lbl_fk_id_alumnos = Label(marco_2, text="Id_alumnos").grid(column=0, row=0, padx=5, pady=5)
        ids_alumnos = obtener_id_alumnos()
        txt_fk_id_alumnos = ttk.Combobox(marco_2, values=ids_alumnos, textvariable=Datos().set_fk_id_alumnos)
        txt_fk_id_alumnos.grid(column=1, row=0)

        lbl_Primer_examen =Label(marco_2, text="Primer Examen").grid(column=0, row=1, padx=5, pady=5)
        txt_Primer_examen =Entry(marco_2, textvariable=Datos.set_primer_examen)
        txt_Primer_examen.grid(column=1, row=1)

        lbl_Segundo_examen =Label(marco_2, text="Segundo Examen").grid(column=0, row=2, padx=5, pady=5)
        txt_Segundo_examen =Entry(marco_2, textvariable=Datos.set_segundo_examen)
        txt_Segundo_examen.grid(column=1, row=2)

        lbl_Tercer_examen =Label(marco_2, text="Tercer Examen").grid(column=0, row=3, padx=5, pady=5)
        txt_Tercer_examen =Entry(marco_2, textvariable=Datos.set_tercer_examen)
        txt_Tercer_examen.grid(column=1, row=3)

        lbl_Examen_final =Label(marco_2, text="Examen Final").grid(column=0, row=4, padx=5, pady=5)
        txt_Examen_final =Entry(marco_2, textvariable=Datos.set_examen_final)
        txt_Examen_final.grid(column=1, row=4)

        #botones marco 2
        btnNuevo = Button(marco_2, text="Agregar", command=lambda:nuevo_calificacion())
        btnNuevo.grid(column=0, row=5, pady=5, padx=5)

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
                register_window.destroy()
            except pyodbc.Error as e:
                messagebox.showerror("Error", "Ocurrió un error al registrar las calificaciones.")

            else:
                messagebox.showerror("Error", "Por favor, complete todos los campos.")

        ventana.mainloop()

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
    Frame(frame2, width=350, height=2, bg='black').place(x=25,y=177)

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
    
    def validar_login():
        global nombre_profesor
        # Obtener los datos ingresados por el usuario
        usuario = user.get()
        contrasena = code.get()

        cursor = connection.cursor()

        # Realizar la consulta SQL para buscar el usuario ingresado
        cursor.execute("SELECT usuario, contrasena, nombre, apellido FROM profesores WHERE usuario = ?", (usuario,))
        resultado = cursor.fetchone()

        # Comprobar si se encontró el usuario
        if resultado:
            usuario_bd, contrasena_bd, nombre, apellido = resultado
            if contrasena == contrasena_bd:
                nombre_profesor = nombre + " " + apellido  # Almacena el nombre del profesor en la variable global
                abrir_ventana_principal()
            else:
                messagebox.showerror("Error", "Contraseña incorrecta")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    login=Tk()
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

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
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
    Button(frame, width=39, pady=7, text='Iniciar Sesion', bg='#57a1f8', fg='white', border=0, command=validar_login).place(x=44,y=204)
    label=Label(frame, text='No tienes una cuenta?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=75,y=270)

    sign = Button(frame, width=7,text='Registrate', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=ventana_register)
    sign.place(x=210,y=270)

    login.mainloop()
# Llamada a la función para mostrar la ventana de inicio de sesión al inicio
ventana_login()