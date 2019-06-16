import time

while True:

    G=[]
    H=[]
    menu = ("\nMENU\nOPCION 1: Mostrar resumen\nOPCION 2: Reiniciar juego\nOPCION 3: Finalizar juego\nOPCION 4: Mostrar pozo ganado\nOPCION 5: Presione 5 para continuar el juego")
    #Entrada
    while True:
        x = int(input("\nIngrese el numero de jugadores: "))
        if x>0:
            break
        else:
            print("Numero ingresado no es válido")
    
    while True:
        y = input("\nIngrese su nombre: ")
        G.append(y)
        while True:
            z= int(input("\nIngrese numero de cartillas: "))
            if 0 < z <= 3:
                H.append(z)
                break
            else:
                print("Ah excedido el número de cartillas permitidas")
                
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

    print(menu)



    while True:
        
        if len(m)>=0:

            while True:
                opcion = int(input("\nIngrese el número de la opcion elegida: "))
                print(menu)
                if(1<=opcion<=5):
                    break
                else:
                    print("\n> > > Opcion inválida < < <")

            if opcion==1:
                print("\nResumen: ",m)
            elif opcion==2:
                print("\nReiniciando el programa")
                print("\n_____________________________________________________________")
                print("\n>>>>>>>>>>>>>>>>>>>>>>NUEVO JUEGO<<<<<<<<<<<<<<<<<<<<<")
                print("\n_____________________________________________________________")    
            elif opcion==3:
                print("\nFinalizando juego")
                print("\n_____________________________________________________________")
                print("\n>>>>>>>>>>>>>>>>>>>>>>GAME OVER<<<<<<<<<<<<<<<<<<<<<")
                print("\n_____________________________________________________________")
            elif opcion==4:
                print("\n_____________________________________________________________")
                print("\nPOZO GANADO: ",pozo, " SOLES")
                print("\n_____________________________________________________________")
            else:
                a = random.choice(n)
                m.append(a)
                n.remove(a)
                print("\n>>>>>>>>>> Bolilla elegida: ",a, " <<<<<<<<<<")
        
        if(opcion==5):
            continue
        if(opcion==2 or opcion==3):
            break  
     
    if(opcion==3):
        break
#Hay talento, solo falta apoyarlo.