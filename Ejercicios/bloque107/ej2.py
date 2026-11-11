# Ejercicio 2. Piedra, papel, tijera a mejor de 5
# Programa una partida de piedra, papel o tijera contra la máquina que se juega a mejor de 5 rondas: gana la partida quien primero llegue a 3 victorias. Una ronda que termina en empate no suma ningún punto y la partida continúa.
# Tras cada ronda, muestra el marcador con el mensaje "Marcador: Tú <n> - Máquina <m>". Al terminar, muestra el mensaje "Has ganado la partida" o "Ha ganado la máquina", según corresponda.
# Usa random para la jugada de la máquina (por ejemplo, random.randint(1, 3), asociando cada número a una jugada).


# 3 variables con  sus posibilidades de ganar
# bucle 1-6 para 5 rondas
# el que llegue a 3 rondas gana
# la maquina elige aleatoriamente con random.randint(1, 3)
import random
piedra = "1"
papel = "2"
tijera = "3"

def piedrapapertijera():
    marcj1 = 0
    marcai = 0
    while True:
        eleccion = input("1.Piedra - 2-Papel - 3.Tijera: ")
        eleccion_machine = str((random.randint(1, 3)))
        if eleccion != piedra and eleccion != papel and eleccion != tijera :
            print("Eso no es una eleccion valida")
        else:
            if eleccion == piedra and eleccion_machine == piedra:
                print("Empate , prueba de nuevo")
            elif eleccion == piedra and eleccion_machine == papel:
                print("Gana la maquina")
                marcai = (marcai+1)
            elif eleccion == piedra and eleccion_machine == tijera:
                print("Gana el  jugador 1")
                marcj1 = (marcj1+1)
            elif eleccion == papel and eleccion_machine == piedra:
                print("Gana el  jugador 1")
                marcj1 = (marcj1+1)
            elif eleccion == papel and eleccion_machine == papel:
                print("Empate , prueba de nuevo")
            elif eleccion == papel and eleccion_machine == tijera:
                print("Gana la maquina")
                marcai = (marcai+1)
            elif eleccion == tijera and eleccion_machine == piedra:
                print("Gana la maquina")
                marcai = (marcai+1)
            elif eleccion == tijera and eleccion_machine == papel:
                print("Gana el  jugador 1")
                marcj1 = (marcj1+1)
            elif eleccion == tijera and eleccion_machine == tijera:
                print("Empate , prueba de nuevo")
            print("El marcador actual es: ",marcj1 ,"-", marcai)

        if marcai == 3:
            print ("Ha ganado la máquina")
            return
        elif marcj1 == 3:
            print ("Has ganado la partida")
            return
   

piedrapapertijera()

