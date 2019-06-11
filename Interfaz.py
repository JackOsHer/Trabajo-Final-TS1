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
    etiqueta3 = Label(ventana, text=">>>>>>>> BINGO <<<<<<<<",fg="red").place(x=90, y=190)

    etiqueta4 = Label(ventana, text="Mostrar Resumen:").place(x=80, y=220)
    etiqueta5 = Label(ventana, text="Reiniciar Juego:").place(x=80, y=255)
    etiqueta6 = Label(ventana, text="Finalizar Juego:").place(x=80, y=290)
    etiqueta7 = Label(ventana, text="Mostrar Pozo:").place(x=80, y=325)
    etiqueta8 = Label(ventana, text="Sacar Bolilla:").place(x=80, y=360)

    boton5 = Button(ventana, text="Seleccionar", command=resumen).place(x=200, y=220)
    boton6 = Button(ventana, text="Seleccionar", command=reiniciar).place(x=200, y=255)
    boton7 = Button(ventana, text="Seleccionar", command=finalizar).place(x=200, y=290)
    boton8 = Button(ventana, text="Seleccionar", command=mostrar_pozo).place(x=200, y=325)
    boton9 = Button(ventana, text="Seleccionar", command=seleccionar_bolilla).place(x=200, y=360)
    boton10 = Button(ventana, text="BINGO", command=ganar).place(x=250, y=410)

def ganar():
    ventana3 = Tk()
    etiqueta9 = Label(ventana3, text="FELICITACIONES, Usted ha ganado").place(x=50, y=20)
    ventana3.geometry('300x200')
    ventana3.title("BINGO!!!")
    Imagen = PhotoImage(file="bingo1.png").place(x=0, y=40)
    etiqueta10 = Label(ventana3, image=Imagen).place(x=0, y=50).pack()
    

def resumen():
    messagebox.showinfo("RESUMEN", str(m))

def reiniciar():
    m.clear()
    G.clear()
    H.clear()
    n.clear()
    messagebox.showinfo("Reiniciar Juego", "Juego Reiniciado Exitosamente")

def finalizar():
    messagebox.showinfo("Finalizar Juego", "GAME OVER, GRACIAS POR JUGAR")   
    ventana.destroy()

def mostrar_pozo():
    pozo = 0
    for i in H:
        pozo = pozo + int(i)
    pozo = pozo*5
    messagebox.showinfo("Mostrar Pozo", "El pozo es de "+ str(pozo)+" soles.")

def seleccionar_bolilla():
    a = random.choice(n)
    m.append(a)
    n.remove(a)
    messagebox.showinfo("BOLILLA", "Bolilla elegida: "+str(a))

def añadir_jugador():
    if int(cartilla.get())<4:
        G.append(nombre.get())
        H.append(cartilla.get())
    else:
        messagebox.showinfo("Mensaje", "Ah excedido el número de cartillas permitido")
    nombre.set("")
    cartilla.set("")
    
def mostrar_jugadores():
    messagebox.showinfo("Jugadores", str(G))
  

ventana= Tk()

# Definimos las variables
n = []
for i in range(1,81):
    n.append(i)
m = []


G = []
H = []
nombre = StringVar()
cartilla = StringVar()

#Diseño de la Interfaz (Ventana 1)
ventana.geometry('350x480')
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