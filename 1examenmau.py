# -*- coding: utf-8 -*-
"""
Created on Sat May 20 23:14:18 2023

@author: Arelii Manuel
"""


import re
import cx_Oracle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



usuario = 'sys'
contraseña = '123Areli#'
host = 'localhost'
puerto = '1521'
sid = 'orcl'

con = f'{usuario}/{contraseña}@{host}:{puerto}/{sid}'

try:
    conexion = cx_Oracle.connect(con, mode=cx_Oracle.SYSDBA)
except cx_Oracle.Error as error:
    print("Error al conectar a Oracle:", error)



def resetear():
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    

def validar_contrasena(contrasena):
    ex = "^#(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{4}@(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{4}&$"
    return re.match(ex, contrasena)


def materia():
    # Ocultar la ventana actual
    window.withdraw()

    # Crear una nueva ventana
    logueado = Toplevel(window)

    logueado.title("Examen")
    logueado.geometry("1250x400")
    logueado.configure(bg='#A7BFE8')
   
    # Agregar contenido a la nueva ventana
    label = Label(logueado, text="★ B I E N V E N I D O ★" ,font=("arial"),foreground=("#EC6EAD"))
    label.pack(pady=10)
    incname_label.place(x=230, y=10)
    
    label11 = Label(logueado, text="ღ ღ ღ ღ ღ ღ" ,font=("arial"),foreground=("#EC6EAD"))
    label11.pack(pady=10)
    incname_label.place(x=230, y=10)
    
    cursor = conexion.cursor()

    # Obtener los datos de la tabla
    cursor.execute("SELECT * FROM materias")
    datos = cursor.fetchall()


    # Cerrar la conexión a la base de datos
    cursor.close()

    # Crear la tabla
    tabla = ttk.Treeview(logueado, columns=("ID", "Nombre", "Semestre","Periodo","Carrera"))
    tabla.pack()
    
    #Limpiar la tabla
    for i in tabla.get_children():
        tabla.delete(i)

    # Insertar los datos en la tabla
    for dato in datos:
        tabla.insert("", "end", values=dato)
    
    # Definir las columnas
    tabla.heading("#0", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Semestre", text="Semestre")
    tabla.heading("Periodo", text="Periodo")
    tabla.heading("Carrera", text="Carrera")
    
    
    # Definir el ancho de las columnas
    tabla.column("#0", width=50)
    tabla.column("Nombre", width=80)
    tabla.column("Semestre", width=80)
    tabla.column("Periodo", width=80)
    tabla.column("Carrera", width=80)
    

    titulo1 = Label(logueado, text="☞☞☞☞☞" ,font=("arial"),foreground=("#EC6EAD"))
    titulo1.pack(pady=10)
    titulo1.place(x=910, y=125)
    titulo = Label(logueado, text="AGREGAR ☞" ,font=("arial"),foreground=("#EC6EAD"))
    titulo.pack(pady=10)
    titulo.place(x=910, y=145)
    titulo22 = Label(logueado, text="MATERIA ☞" ,font=("arial"),foreground=("#EC6EAD"))
    titulo22.pack(pady=10)
    titulo22.place(x=910, y=165)
    titulo33 = Label(logueado, text="☞☞☞☞☞" ,font=("arial"),foreground=("#EC6EAD"))
    titulo33.pack(pady=10)
    titulo33.place(x=910, y=185)
    
    Labelp = Label(logueado, text="Nombre de la materia:" ,font=("arial"),foreground=("#834d9b"))
    Labelp.pack()
    Labelp.place(x=1050, y=30)
    CajaNom = Entry(logueado)
    CajaNom.pack(pady=10)
    CajaNom.place(x=1050, y=60)
    
    
    Labelpre = Label(logueado, text="Semestre:" ,font=("arial"),foreground=("#834d9b"))
    Labelpre.pack()
    Labelpre.place(x=1050, y=90)
    CajaPre = Entry(logueado)
    CajaPre.pack(pady=10)
    CajaPre.place(x=1050, y=120)
    
    Labels = Label(logueado, text="Periodo:" ,font=("arial"),foreground=("#834d9b"))
    Labels.pack()
    Labels.place(x=1050, y=150)
    CajaSto = Entry(logueado)
    CajaSto.pack(pady=10)
    CajaSto.place(x=1050, y=180)
    
    Labelpro = Label(logueado, text="Carrera:" ,font=("arial"),foreground=("#834d9b"))
    Labelpro.pack()
    Labelpro.place(x=1050, y=210)
    CajaPro = Entry(logueado)
    CajaPro.pack(pady=10)
    CajaPro.place(x=1050, y=240)
    
    
    
    def guardarM():
        nombre_m = CajaNom.get()
        semestre = CajaPre.get()
        periodo = CajaSto.get()
        carrera = CajaPro.get()
        
        
        if nombre_m == "" or semestre == "" or periodo == "" or carrera == "" :
            messagebox.showerror('Error', 'Campos vacios vacios')
        else:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO materias (nombre_m, semestre, periodo, carrera) VALUES (:nombre_m, :semestre, :periodo, :carrera)",
                       {'nombre_m': nombre_m, 'semestre': semestre, 'periodo': periodo, 'carrera': carrera})

            conexion.commit()
            
            cursor.close()
            
            messagebox.showinfo("Éxito", "Se guardo correctamente")
            logueado.destroy()
            materia()
    
    
    def guardar_cambios():
        # Obtener el registro seleccionado
        seleccionado = tabla.focus()
        if seleccionado:
            # Obtener los valores editados
            valores = tabla.item(seleccionado)["values"]
            nuevo_valor1 = CajaNom.get()
            nuevo_valor2 = CajaPre.get()
            nuevo_valor3 = CajaSto.get()
            nuevo_valor4 = CajaPro.get()
            
    
            # Actualizar los valores en la base de datos
            cursor = conexion.cursor()
            cursor.execute("UPDATE materias SET nombre_m=:valor1, semestre=:valor2, periodo=:valor3, carrera=:valor4 WHERE id_materia=:id", 
                           {"valor1": nuevo_valor1, "valor2": nuevo_valor2, "valor3": nuevo_valor3, "valor4": nuevo_valor4, "id": valores[0]})
            conexion.commit()
            cursor.close()
            
            messagebox.showinfo("Éxito", "Se guardo correctamente")
    
            # Actualizar la tabla
            logueado.destroy()
            materia()
        
    def eliminar_registro():
        # Obtener el registro seleccionado
        seleccionado = tabla.focus()
        if seleccionado:
            # Obtener el ID del registro seleccionado
            id_registro = tabla.item(seleccionado)["values"][0]

            cursor = conexion.cursor()
            cursor.execute("DELETE FROM materias WHERE id_materia = :id", {"id": id_registro})
            conexion.commit()
            cursor.close()

            messagebox.showinfo("Éxito", "Se borro correctamente")
            # Actualizar la tabla
            logueado.destroy()
            materia()
    
    
    
    # Agregar un botón para volver a la ventana anterior
    botonG = Button(logueado, text="Registrar", command=guardarM)
    botonG.pack(pady=10)
    botonG.place(x=710, y=280)

    def regresar():
        # Mostrar la ventana anterior
        window.deiconify()

        # Cerrar la ventana actual
        logueado.destroy()
        
        
    # Agregar un botón para volver a la ventana anterior
    boton_volver = Button(logueado, text="Cerrar sesión", command=regresar)
    boton_volver.pack(pady=10)
    boton_volver.place(x=10, y=10)

    boton_m = Button(logueado, text="Modificar", command=guardar_cambios)
    boton_m.pack(pady=10, side=LEFT)
    boton_m.place(x=780, y=280)
    
    boton_e = Button(logueado, text="Eliminar", command=eliminar_registro)
    boton_e.pack(pady=10, side=LEFT)
    boton_e.place(x=850, y=280)



def loguear():
    usu = username_entry.get()
    con = password_entry.get()
    
    if usu == "" or con == "":
        messagebox.showerror('Error', 'Campos vacios, revisar')
    elif validar_contrasena(con) == None:
        messagebox.showerror('Error', 'La contraseña no cumple')
    else:
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM profesores1 WHERE usuario=:u AND contrasena=:p",
                       {'u': usu, 'p': con})
        result = cursor.fetchone()
        cursor.close()

        if result:
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            materia()
        else:
            messagebox.showerror("Error", "Usuario y/o contraseña incorrectos.")
       
        
      
        
#Ventana para regsitrar a cajero
def registrarP():
    
    window.withdraw()
    
    # Crear una nueva ventana
    registrar = Toplevel(window)

    registrar.title("Registrar")
    registrar.geometry("330x400")
    registrar.configure(bg='#7BC6CC')
    registrar.resizable(0,0)
    
    # Agregar contenido a la nueva ventana
    label = Label(registrar, text="★ R E G I S T R A R S E ★",font=("arial"),foreground=("#834d9b"))
    label.pack(pady=10)
    label.place(x=80, y=10)
    
    
    labelnom = Label(registrar, text="Nombre:",font=("arial"),foreground=("#f2709c"))
    labelnom.pack()
    labelnom.place(x=30, y=60)
    nombre = Entry(registrar) #Caja de texto
    nombre.pack(pady=10)
    nombre.place(x=30, y=90)
    
    labelapp = Label(registrar, text="Apellido P:",font=("arial"),foreground=("#f2709c"))
    labelapp.pack()
    labelapp.place(x=30, y=120)
    apep = Entry(registrar) #Caja de texto
    apep.pack(pady=10)
    apep.place(x=30, y=150)
    
    labelapm = Label(registrar, text="Apellido M:",font=("arial"),foreground=("#f2709c"))
    labelapm.pack()
    labelapm.place(x=30, y=180)
    apem = Entry(registrar) #Caja de texto
    apem.pack(pady=10)
    apem.place(x=30, y=210)
    
    labelusu = Label(registrar, text="Usuario:",font=("arial"),foreground=("#f2709c"))
    labelusu.pack()
    labelusu.place(x=30, y=240)
    usua = Entry(registrar) #Caja de texto
    usua.pack(pady=10)
    usua.place(x=30, y=270)
    
    labelcon = Label(registrar, text="Contraseña:",font=("arial"),foreground=("#f2709c"))
    labelcon.pack()
    labelcon.place(x=30, y=300)
    contra = Entry(registrar, show="*") #Caja de texto
    contra.pack(pady=10)
    contra.place(x=30, y=330)
    

    def guardar():
        nom = nombre.get()
        apellidop = apep.get()
        apellidom = apem.get()
        usuario = usua.get()
        contrasenia = contra.get()
        
        if nom == "" or apellidop == "" or apellidom == "" or usuario == "" or contrasenia == "":
            messagebox.showerror('Error', 'Hay campos vacios, revisalos')
        elif validar_contrasena(contrasenia) == None:
            messagebox.showerror('Error', 'La contraseña no cumple, intenta de nuevo')
        else:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO profesores1 (nombre, apellido_p, apellido_m, usuario, contrasena) VALUES (:nombre, :apellido_p, :apellido_m, :usuario, :contrasenia)",
                       {'nombre': nom, 'apellido_p': apellidop, 'apellido_m': apellidom, 'usuario': usuario, 'contrasenia': contrasenia})

            conexion.commit()
            
            cursor.close()
            
            messagebox.showinfo("Éxito", "Se registro profesor.")
    
    

    def regresar():
        # Mostrar la ventana anterior
        window.deiconify()

        # Cerrar la ventana actual
        registrar.destroy()
        
    
    # Agregar un botón para volver a la ventana anterior
    boton_volver = Button(registrar, text="Registrar", command=guardar)
    boton_volver.pack(pady=10)
    boton_volver.place(x=250, y=150)
    
    
    boton_v = Button(registrar, text="Regresar", command=regresar)
    boton_v.pack(pady=10)
    boton_v.place(x=250, y=200)
    
    
    

# Crear la ventana principal
window = Tk()
window.title("Inicio de sesión")
window.geometry("650x200")
window.configure(bg='#f4c4f3')
window.resizable(0,0)
window.eval('tk::PlaceWindow . center')


# Crear etiquetas y campos de entrada

incname_label = Label(window, text="★ I N I C I O  D E  S E S I Ó N ★" ,font=("arial"),foreground=("#3a7bd5"))
incname_label.pack(pady=5)
incname_label.place(x=230, y=10)
  
username_label = Label(window, text="Usuario:" ,font=("arial"),foreground=("#f2709c"))
username_label.pack(pady=5)
username_label.place(x=10, y=60)
username_entry = Entry(window) #Caja de texto
username_entry.pack(pady=10)
username_entry.place(x=80, y=60)

password_label = Label(window, text="Contraseña:" ,font=("arial"),foreground=("#f2709c"))
password_label.pack(pady=10)
password_label.place(x=300, y=60)
password_entry = Entry(window, show="*")  # Caja de texto, el texto se muestra como asteriscos
password_entry.place(x=400, y=60)

# Crear botón de inicio de sesión
login_button = Button(window, text="Iniciar sesión", command=loguear)
login_button.pack(pady=10)
login_button.place(x=200, y=110)

reset_button = Button(window, text="Resetear", command=resetear)
reset_button.pack(pady=10)
reset_button.place(x=550, y=60)

reg_button = Button(window, text="Registrarse", command=registrarP)
reg_button.pack(pady=10)
reg_button.place(x=300, y=110)


# Ejecutar el bucle principal de la ventana
window.mainloop()
