G=[]
H=[]
#Entrada
x = int(input("ingrese el numero de jugadores"))

while True:
    y = input("ingrese su nombre")
    G.append(y)
    z=int(input("ingrese numero de cartillas"))
    H.append(z)
    if len(G) == x and len(H) == z:
        break

suma = 0 
for fila in H:
    suma = suma + fila

pozo = suma * 5
