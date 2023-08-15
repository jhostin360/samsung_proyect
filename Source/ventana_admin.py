from tkinter import *
from tkinter import ttk
import tkinter as tk
import util.generic as utl
from tkinter import LabelFrame, PhotoImage, Label, Frame, messagebox



def ventana_admin():

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

    Label(tab1, text='Estos son los Profesores en el tab 1', width=164, height=15, bg='white').pack()
    Label(tab2, text='Estos son los Estudiantes en el tab 2', width=164, height=15, bg='white').pack()
    Label(tab3, text='Estas son las Calificaciones en el tab 3', width=164, height=15, bg='white').pack()

    # Configurar pesos para que frame3 ocupe el espacio restante
    ventana_admin.grid_rowconfigure(0, weight=1)
    ventana_admin.grid_rowconfigure(1, weight=1)
    ventana_admin.grid_columnconfigure(0, weight=1)
    ventana_admin.grid_columnconfigure(1, weight=1)

    ventana_admin.mainloop()