# Ejercicio 4. Combate por turnos
# Programa un combate simplificado entre dos personajes, 
# jugador y enemigo, cada uno con 20 puntos de vida.
# En cada turno, el jugador ataca primero (resta al enemigo un daño aleatorio entre 3 y 8) y, 
# si el enemigo sigue con vida, contraataca (resta al jugador un daño aleatorio entre 2 y 6).

# Muestra la vida de ambos tras cada turno y repite hasta que uno de los dos llegue a 0 o menos,
# mostrando entonces el mensaje "Ha ganado el jugador" o "Ha ganado el enemigo", según corresponda.

# Extrae el ataque a una función atacar(dano_min, dano_max) que devuelva el daño causado para no
# repetir la misma lógica dos veces.

import random
def atacar(dano_min,dano_max):
   dano = random.randint(dano_min,dano_max)
   return dano
    
def lucha():
    jug1 = 20
    maq = 20
    print("A luchar!")
    while True:
        input("Pulsa Enter para el siguiente turno...")
        if jug1 > 0 and maq > 0:
            maq = (maq - atacar(3,8))
            print("La vida del enemigo es: ", maq)
            if maq <= 0 :
                print("Ha ganado el jugador")
                return
            else:
                print("Maquina Contraataca")
                jug1 = (jug1 - atacar(2,6))
                print("Tu vida es : ", jug1)
        else:
            if jug1 <= 0 :
                print("Ha ganado el enemigo")
                return

lucha()