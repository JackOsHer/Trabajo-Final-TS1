
while True:
#Declaramos los arreglos donde se guardaran el numero de cartillas y los jugadores ademas  el menu opcion 
    G=[]
    H=[]
    menu = ("\nMENU\nOPCION 1: Mostrar resumen\nOPCION 2: Reiniciar juego\nOPCION 3: Finalizar juego\nOPCION 4: Mostrar pozo ganado\nOPCION 5: Presione 5 para continuar el juego\nOPCION 6: BINGO")
    #Entrada de jugadore y numero de cartillas 
    while True:
        x = int(input("\nIngrese el numero de jugadores: "))
        if x>1:
            break
        elif x ==1 : 
            print("consiguete un amigo mas campeon ")
        else:
            print("Numero ingresado no es válido")
    
    while True:
        while True:
            y = input("\nIngrese su nombre: ")
            if G.count(y) == 0:
                G.append(y)
                break
            else:
                print("Nombre ya registrado :(,elija otro :D")
        while True:
            z= int(input("\nIngrese numero de cartillas: "))
            if 0 < z <= 3:
                H.append(z)
                break
            else:
                print("Ah excedido el número de cartillas permitidas")
                
        if len(G) == x:
            break
#hallamos el pozo de sera acreedor el ganador del bingo
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

#a

    while True:
        
        if len(m)>=0:

            while True:
                opcion = int(input("\nIngrese el número de la opcion elegida: "))
                print(menu)
                if(1<=opcion<=6):
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
            elif opcion==5:
                a = random.choice(n)
                m.append(a)
                n.remove(a)
                print("\n>>>>>>>>>> Bolilla elegida: ",a, " <<<<<<<<<<")
            else:
                if len(m)>=15:
                    print("FELICITACIONES,usted ha ganado el Bingo")
                    print("EL POZO GANADO ES DE ", pozo)
                else:
                    print("Aun no se han sacado 15 bolillas :c")
        
        if(opcion==5):
            continue
        if(opcion==2 or opcion==3):
            break  
     
    if(opcion==3):
        break
        
    if(opcion==6):
        break
    
#Hay talento, solo falta apoyarlo.
print(pozo)