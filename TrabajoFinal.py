G=[]
H=[]
#Entrada
x = int(input("ingrese el numero de jugadores: "))

while True:
    y = input("ingrese su nombre: ")
    G.append(y)
    while True:
        z= int(input("ingrese numero de cartillas: "))
        if z <= 3:
            H.append(z)
            break
    if len(G) == x:
        break

suma = 0 
for fila in H:
    suma = suma + fila

pozo = suma * 5



import random
n = []
m = []
for i in range(1,81):
    n.append(i)

print("MENU\nOPCION 1: Mostrar resumen\nOPCION 2: Reiniciar juego\nOPCION 3: Finalizar juego\nOPCION 4: Mostrar pozo ganado")
op1 = "OPCION 1: Mostrar resumen"
op2 = "OPCION 2: Reiniciar juego"
op3 = "OPCION 3: Finalizar juego"
op4 = "OPCION 4: Mostrar pozo ganado"

while True:
    a = random.choice(n)
    m.append(a)
    n.remove(a)
    respuesta = int(input("Presione 5 para continuar el juego: "))
    print("Bolilla elegida: ",a)
    if len(m)>=15:
        while True:
            print("MENU\nOPCION 1: Mostrar resumen\nOPCION 2: Reiniciar juego\nOPCION 3: Finalizar juego\nOPCION 4: Mostrar pozo ganado")
            opcion = int(input("Ingrese el numero de la opcion elegida: "))
            if(1<=opcion<=4):
                break
        if opcion==1:
            print("Resumen: ",m)
        elif opcion==2:
            print("Reiniciando el programa")
        elif opcion==3:
            print("Finalizando juego")
        else:
            print("Pozo ganado: ")
    if(respuesta==5):
        continue
