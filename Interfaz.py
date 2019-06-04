# Importamos librerias
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

# Definimos las funciones
def saludar():
    print("Hola "+nombre.get())

def obtener():
    messagebox.showinfo("Mensaje","Hola "+nombre.get()+"\nUsted ha comprado "+str(cartilla.get())+" cartillas")

def error():
    messagebox.showwarning("Ups...","Lo sentimos la interfaz aun no esta terminada")

ventana= Tk()

# Definimos las variables
nombre = StringVar()
cartilla = IntVar()

#Diseño de la Interfaz
ventana.geometry('350x250')
ventana.title("BINGO!!!")
etiqueta = Label(ventana, text="Bienvenidos al Bingo")
etiqueta.pack()

ttk.Button(ventana, text='Salir', command=ventana.destroy).pack(side=BOTTOM)

# Interfaz: Ventanas Label y TextField

etiqueta1 = Label(ventana, text="Nombre del Jugador: ").place(x=40, y=30)
nombre_etiqueta = Entry(ventana, textvariable=nombre).place(x=180, y=30)

etiqueta2 = Label(ventana, text="Numero de Cartillas: ").place(x=40, y=60)
cartilla_etiqueta = Entry(ventana, textvariable=cartilla).place(x=180, y=60)

# Interfaz: Botones

boton1 = Button(ventana, text="Saludo personalizado", command=obtener).place(x=120, y=100)
boton2 = Button(ventana, text="Iniciar juego", command=error).place(x=140, y=130)

etiqueta.mainloop()