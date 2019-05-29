import time
while True:

    G=[]
    H=[]
    #Entrada
    x = int(input("\nIngrese el numero de jugadores: "))

    while True:
        y = input("\nIngrese su nombre: ")
        G.append(y)
        while True:
            z= int(input("\nIngrese numero de cartillas: "))
            if z <= 3:
                H.append(z)
                break
        if len(G) == x:
            break

    suma = 0 
    for fila in H:
        suma = suma + fila

    pozo = suma*5



    import random
    n = []
    m = []
    for i in range(1,81):
        n.append(i)

    print("\nMENU\nOPCION 1: Mostrar resumen\nOPCION 2: Reiniciar juego\nOPCION 3: Finalizar juego\nOPCION 4: Mostrar pozo ganado\nOPCION 5: Presione 5 para continuar el juego")



    while True:
        a = random.choice(n)
        m.append(a)
        n.remove(a) 

        if len(m)>=1:

            while True:
                opcion = int(input("\nIngrese el numero de la opcion elegida: "))
                print("\nMENU\nOPCION 1: Mostrar resumen\nOPCION 2: Reiniciar juego\nOPCION 3: Finalizar juego\nOPCION 4: Mostrar pozo ganado\nOPCION 5: Presione 5 para continuar el juego")
                if(1<=opcion<=5):
                    break

            if opcion==1:
                print("\nResumen: ",m)
            elif opcion==2:
                print("\nReiniciando el programa")
            elif opcion==3:
                print("\nFinalizando juego")
            elif opcion==4:
                print("\nPozo ganado: ",pozo, " soles")
            else:
                print("\n>>>>>>>>>> Bolilla elegida: ",a, " <<<<<<<<<<")

        if(opcion==5):
            continue
        if(opcion==3 and opcion==2):
            break  
    
if(opcion==2):
    quit
