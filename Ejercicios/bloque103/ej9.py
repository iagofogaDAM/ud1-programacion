turn1 = input("JUGADOR 1 - PIEDRA PAPEL O TIJERA! : ")
turn2 = input("JUGADOR 2 - PIEDRA PAPEL O TIJERA! : ")

if turn1 == turn2 :
    print ("INICIA DE NUEVO")
elif turn1 == "PIEDRA" and turn2 == "PAPEL":
    print ("GANA JUGADOR 2")
elif turn1 == "PAPEL" and turn2 == "PIEDRA":
    print ("GANA JUGADOR 1")
elif turn1 == "PAPEL" and turn2 == "TIJERA":
    print ("GANA JUGADOR 2")
elif turn1 == "PIEDRA" and turn2 == "TIJERA":
    print ("GANA JUGADOR 1")
elif turn1 == "TIJERA" and turn2 == "PAPEL":
    print ("GANA JUGADOR 1")
elif turn1 == "TIJERA" and turn2 == "PIEDRA":
        print ("GANA JUGADOR 2")
else : 
    print ("PERO TI ERES BURRO OU QUE!!!")