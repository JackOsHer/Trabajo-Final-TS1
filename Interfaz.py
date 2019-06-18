# Importamos librerias
import random
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

ventana= Tk()

## Definimos las variables
#Bolillas por sacar
n=[]
for i in range(1,81):
    n.append(i)
#Bolillas sacadas
m=[]

#Nombres de los jugadores
G=[]
H =[]
nombre = StringVar()
cartilla = StringVar()

# Definimos las funciones
def abrir_ventana2():
    if int(len(G))>1:
    #LABEL's
        etiqueta3 = Label(ventana, text=">>>>>>>> BINGO <<<<<<<<",fg="blue",bg="#48C9B0").place(x=90, y=190)
        etiqueta4 = Label(ventana, text=" Mostrar Resumen:",fg="#181446",bg="#48C9B0",wraplength=300).place(x=80, y=220)
        etiqueta5 = Label(ventana, text="Reiniciar Juego:",fg="#181446",bg="#48C9B0").place(x=80, y=255)
        etiqueta6 = Label(ventana, text="Finalizar Juego:",fg="#181446",bg="#48C9B0").place(x=80, y=290)
        etiqueta7 = Label(ventana, text="Mostrar Pozo:",fg="#181446",bg="#48C9B0").place(x=80, y=325)
        etiqueta8 = Label(ventana, text="Sacar Bolilla:",fg="#181446"  ,bg="#48C9B0").place(x=80, y=360)
        #Botones
        boton5 = Button(ventana, text="Seleccionar", command=resumen,activebackground="red").place(x=200, y=220)
        boton6 = Button(ventana, text="Seleccionar", command=reiniciar,activebackground="red").place(x=200, y=255)
        boton7 = Button(ventana, text="Seleccionar", command=finalizar,activebackground="red").place(x=200, y=290)
        boton8 = Button(ventana, text="Seleccionar", command=mostrar_pozo,activebackground="red").place(x=200, y=325)
        boton9 = Button(ventana, text="Seleccionar", command=seleccionar_bolilla,activebackground="red").place(x=200, y=360)
        boton10 = Button(ventana, text="BINGO", command=ganar,activebackground="#BABC28").place(x=250, y=410)
    else:
        messagebox.showinfo("Mensaje", "Debe de registrar al menos a 2 jugadores :D")

    
    
def ganar():
    if int(len(m))>=15:
        ventana3 = Tk()
        etiqueta9 = Label(ventana3, text="FELICITACIONES, Usted ha ganado",bg="#BABC28").place(x=50, y=20)
        ventana3.geometry('350x250')
        ventana3.title("BINGO!!!")
        ventana3.config(bg="#BABC28")
        etiqueta11 = Label(ventana3, text="POZO GANADO: ",bg="#BABC28").place(x=50, y=50) 
    
        pozo = 0
        for i in H:
            pozo = pozo + int(i)
        pozo = pozo*5
    
    else:
        messagebox.showinfo("Mensaje", "Aun no se han elegido 15  bolillas :D")

    etiqueta12 = Label(ventana3, text=(str(pozo)," NUEVOS SOLES"),bg="#BABC28").place(x=180, y=50)   
    ventana3.mainloop()

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
        messagebox.showinfo("Mensaje", "Jugador registrado exitosamente")
    else:
        messagebox.showinfo("Mensaje", "Ah excedido el número de cartillas permitido")
    nombre.set("")
    cartilla.set("")
    
def mostrar_jugadores():
    messagebox.showinfo("Jugadores", str(G))


#Diseño de la Interfaz (Ventana 1)
ventana.geometry('350x480')
ventana.title("BINGO!!!")
etiqueta = Label(ventana, text="Bienvenidos al Bingo",bg="#48C9B0")
etiqueta.pack()
ventana.config (bg="#48C9B0")
ttk.Button(ventana, text='Salir', command=ventana.destroy).pack(side=BOTTOM)


# Interfaz: Ventanas Label y TextField (Ventana1)

etiqueta1 = Label(ventana, text="Nombre del Jugador: ",bg="#48C9B0").place(x=40, y=30)
nombre_etiqueta = Entry(ventana, textvariable=nombre).place(x=180, y=30)

etiqueta2 = Label(ventana, text="Numero de Cartillas: ",bg="#48C9B0").place(x=40, y=60)
cartilla_etiqueta = Entry(ventana, textvariable=cartilla).place(x=180, y=60)


# Interfaz: Botones

boton2 = Button(ventana, text="Iniciar Juego", command=abrir_ventana2,activebackground="#369A8E").place(x=140, y=130)
boton3 = Button(ventana, text="Agregar Jugador", command=añadir_jugador,activebackground="#369A8E").place(x=60, y=90)
boton4 = Button(ventana, text="Mostrar Jugadores", command=mostrar_jugadores,activebackground="#369A8E").place(x=180, y=90)

ventana.mainloop()