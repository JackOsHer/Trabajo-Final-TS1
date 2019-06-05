# Importamos librerias
import random
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

# Definimos las funciones
def saludar():
    print("Hola "+nombre.get())

def obtener():
    messagebox.showinfo("Mensaje","Hola "+nombre.get()+"\nUsted ha comprado "+str(cartilla.get())+" cartillas")

def abrir_ventana2():
    ventana2 = Tk()
    ventana2.geometry('350x250')
    ventana2.title("BINGO!!!")
    etiqueta3 = Label(ventana2, text="Bienvenidos al Bingo")
    etiqueta3.pack()
    ttk.Button(ventana2, text='Salir', command=ventana2.destroy).pack(side=BOTTOM)

    etiqueta4 = Label(ventana2, text="Mostrar Resumen:").place(x=60, y=30)
    etiqueta5 = Label(ventana2, text="Reiniciar Juego:").place(x=60, y=60)
    etiqueta6 = Label(ventana2, text="Finalizar Juego:").place(x=60, y=90)
    etiqueta7 = Label(ventana2, text="Mostrar Pozo:").place(x=60, y=120)
    etiqueta8 = Label(ventana2, text="Sacar Bolilla:").place(x=60, y=150)

    boton5 = Button(ventana2, text="Seleccionar", command=seleccionar1).place(x=180, y=30)
    boton6 = Button(ventana2, text="Seleccionar", command=reiniciar).place(x=180, y=60)
    boton7 = Button(ventana2, text="Seleccionar", command=ventana2.detroy).place(x=180, y=90)
    boton8 = Button(ventana2, text="Seleccionar", command=calcular_pozo).place(x=180, y=120)
    boton9 = Button(ventana2, text="Seleccionar", command=seleccionar5).place(x=180, y=150)

def reiniciar():
    G.clear()
    H.clear()
        

def seleccionar1():
    messagebox.showinfo("RESUMEN", str(m))

def seleccionar5():
    a = random.choice(n)
    m.append(a)
    n.remove(a)
    messagebox.showinfo("BOLILLA", "Bolilla elegida: "+str(a))

def añadir_jugador():
    if int(cartilla.get()) <4:
        G.append(nombre.get())
        H.append(cartilla.get())
    else:
        messagebox.showinfo("Mensaje", "Ah excedido el número de cartillas permitidas")
    nombre.set("")
    cartilla.set("")
    
def mostrar_jugadores():
    messagebox.showinfo("Jugadores", str(G))

def calcular_pozo():
    pozo = 0
    for i in H:
        pozo = pozo + int(i)
    pozo = pozo*5

    messagebox.showinfo("Mensaje", "El pozo es de "+ str(pozo) + " soles")

  

ventana = Tk(useTk=0)

# Definimos las variables
n = []
for i in range(1,81):
    n.append(i)
m = []

A = 0
G = []
H = []
nombre = StringVar()
cartilla = StringVar()

#Diseño de la Interfaz (Ventana 1)
ventana.geometry('350x250')
ventana.title("BINGO!!!")
etiqueta = Label(ventana, text="Bienvenidos al Bingo")
etiqueta.pack()
ttk.Button(ventana, text='Salir', command=ventana.destroy).pack(side=BOTTOM)



# Interfaz: Ventanas Label y TextField (Ventana1)

etiqueta1 = Label(ventana, text="Nombre del Jugador: ").place(x=40, y=30)
nombre_etiqueta = Entry(ventana, textvariable=nombre).place(x=180, y=30)

etiqueta2 = Label(ventana, text="Numero de Cartillas: ").place(x=40, y=60)
cartilla_etiqueta = Entry(ventana, textvariable=cartilla).place(x=180, y=60)


# Interfaz: Botones

boton2 = Button(ventana, text="Iniciar Juego", command=abrir_ventana2).place(x=140, y=130)
boton3 = Button(ventana, text="Agregar Jugador", command=añadir_jugador).place(x=60, y=90)
boton4 = Button(ventana, text="Mostrar Jugadores", command=mostrar_jugadores).place(x=180, y=90)


etiqueta.mainloop()