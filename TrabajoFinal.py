G=[]
H=[]
#Entrada
x = int(input("ingrese el numero de jugadores: "))

while True:
    y = input("ingrese su nombre: ")
    G.append(y)
    z= int(input("ingrese numero de cartillas: "))
    if z <=3:
        H.append(z)
    else:
        z = int(input("Ingrese numero de cartillas: "))
    if len(G) == x:
        break

suma = 0 
for fila in H:
    suma = suma + fila

pozo = suma * 5

print(pozo)