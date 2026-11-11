
# Programa un concurso con 3 preguntas de cultura general fijas en el código 
# (cada una con su respuesta correcta guardada aparte, por ejemplo respuesta_1 = "Santiago").
# Para cada pregunta, muéstrala indicando que se responda en minúsculas,
#  lee la respuesta del usuario y compárala con la correcta. 
# Lleva la cuenta de aciertos con una variable acumuladora y,
#  al final, muestra el mensaje:

# "Sigue practicando" para 0 aciertos.
# "Flojo, pero algo es algo" para 1 acierto.
# "Nada mal" para 2 aciertos.
# "¡Perfecto!" para 3 aciertos.

def concurso():
    aciertos = 0
    respuesta_1 = "iphone"
    r1 = input("Cual es el telefono movil de la marca apple?(en minúsculas) : ")
    if r1 == respuesta_1:
        aciertos = (aciertos + 1)
    else :
        print("MAL")
    respuesta_2 = "nevado"
    r2 = input("Cual es el nombre del perro de ShinChan?(en minúsculas) : ")
    if r2 == respuesta_2:
        aciertos = (aciertos + 1)
    else :
        print("MAL")
    respuesta_3 = "amancio"
    r3 = input("Quien es el dueño de Zara?(en minúsculas) : ")
    if r3 == respuesta_3:
        aciertos = (aciertos + 1)
    else:
        print("MAL")

    if aciertos == 0:
        print("Sigue practicando")
    elif aciertos == 1:
        print("Flojo, pero algo es algo")
    elif aciertos == 2:
        print("Nada mal")
    elif aciertos == 3:
        print("¡Perfecto!")

concurso()
    
    
