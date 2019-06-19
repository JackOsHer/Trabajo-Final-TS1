
while True:
#Declaramos los arreglos donde se guardaran el nombre de los jugadores
# y el número de cartillas q compraran, ademas del Menu
    G=[]
    H=[]
    menu = ("\nMENU\nOPCION 1: Mostrar resumen\nOPCION 2: Reiniciar juego\nOPCION 3: Finalizar juego\nOPCION 4: Mostrar pozo ganado\nOPCION 5: Presione 5 para continuar el juego\nOPCION 6: BINGO")
    
    # REGISTRO DE JUGADORES 
    while True:
        x = input("\nIngrese el numero de jugadores: ")

        try:
            x=int(x)
            if x>1:
                break
            elif x ==1 : 
                print("Consíguete un amigo más campeón D: ")
            else:
                print("Número ingresado no es válido")

        except(ValueError):
            print("Debe ingresar un número, no una letra")        

    
    while True:
        while True:
            y = input("\nIngrese su nombre: ")
            if G.count(y) == 0:
                G.append(y)
                break
            else:
                print("Nombre ya registrado :c. Elija otro :D")


        while True:
            z= input("\nIngrese numero de cartillas: ")

            try:
                z=int(z)

                if 0 < z <= 3:
                    H.append(z)
                    break
                elif z<0:
                    print("Número inválido")
                elif z==0:
                    print("Vamos amigo, compre 1 al menos")
                else:
                    print("Ah excedido el número de cartillas permitidas")

            except(ValueError):
                print("Debe ingresar un número, no una letra")

        if len(G) == x:
            break
# Hallamos el pozo que sera acreedor el ganador del bingo
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

# Inicio del juego

    while True:
        
        if len(m)>=0:

            while True:
                opcion = input("\nIngrese el número de la opcion elegida: ")
                print(menu)
                try:
                    opcion=int(opcion)
                    if(1<=opcion<=6):
                        break
                    else:
                        print("\n> > > Opcion inválida < < <")
                except(ValueError):
                    print("\n>>>>> Debe ingresar un número, no una letra <<<<<")

            if opcion==1:
                print("\nResumen: ",m)
            elif opcion==2:
                print("\n_____________________________________________________________")
                print("\nReiniciando el programa...")
                print("\n_____________________________________________________________")
                print("\n>>>>>>>>>>>>>>>>>>>>>>NUEVO JUEGO<<<<<<<<<<<<<<<<<<<<<")
                print("\n_____________________________________________________________")    
            elif opcion==3:
                print("\n_____________________________________________________________")
                print("\nFinalizando juego...")
                print("\n_____________________________________________________________")
                print("\n>>>>>>>>>>>>>>>>>>>>>>GAME OVER<<<<<<<<<<<<<<<<<<<<<")
                print("\nGRACIAS POR JUGAR :D ")
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
                    print("\n_____________________________________________________________")
                    print("\nFELICITACIONES,usted ha ganado el Bingo")
                    print("\nEL POZO GANADO ES DE: ", pozo, " NUEVOS SOLES")
                    print("\n_____________________________________________________________")
                    print("\n>>>>>>>>>>>>>>>>>>>>>>GAME OVER<<<<<<<<<<<<<<<<<<<<<")
                    print("\nGRACIAS POR JUGAR :D ")
                    print("\n_____________________________________________________________")
                else:
                    print("\nAún no se han sacado 15 bolillas :c. Continúe jugando")
        
        if len(m)==15:
            print("\nAlguien ah debido de ganar ya! :D")
            print("\n_____________________________________________________________")
            print("\n>>>>>>>>>>>>>>>>>>>>>>GAME OVER<<<<<<<<<<<<<<<<<<<<<")
            print("\nGRACIAS POR JUGAR :D ")
            print("\n_____________________________________________________________")
            break

        if(opcion==5):
            continue
        if(opcion==2 or opcion==3 or (opcion==6 and len(m)>=15)):
            break  
     
    if(opcion==3 or (opcion==6 and len(m)>=15) or len(m)==15):
        break
          
#Hay talento, solo falta apoyarlo.