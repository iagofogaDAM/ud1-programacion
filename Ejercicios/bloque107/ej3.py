# Ejercicio 3. Adivina el número con pistas
# Programa el clásico "adivina el número": genera un 
# número secreto aleatorio entre 1 y 100 y deja que el jugador vaya proponiendo números, 
# indicando tras cada intento si el número secreto es "más alto" o "más bajo", hasta que acierte.
# Al final, muestra cuántos intentos ha necesitado. 
# Extrae la generación del número y la comprobación de cada intento a funciones propias.

# Generar numero aleatorio con randit
# si el numero es mas alto indicarlo y lo mismo con lo contrario para ir acercandose al numero
# contador de intentos
# funcion generacion de numero y funcion comprobacion intento


import random
def gennum():
    secnum = random.randint(1, 100)
    return secnum

def compronum():
    intento = 1
    secnum = gennum()
    while True:
        num = int(input("Dame un numero entre el uno y el 100 : "))
        if num == secnum:
            print("Felicidades , has encontrado el numero secreto!")
            print("Has necesitado", intento, "intentos")
            return
        else:
            if num < secnum :
                print("El numero secreto es mas alto")
                intento = intento + 1
            elif num > secnum :
                print("El numero secreto es mas bajo")
                intento = intento + 1

compronum()




