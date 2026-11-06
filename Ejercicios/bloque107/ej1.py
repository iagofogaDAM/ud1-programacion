#Adivina los digitos
#Bucle de peticiones hasta llegar a 6
#Numero Secreto que hay que recorrer(in range)
#Cada vez que numero sea igual saltamos de posicion y muestra mensaje
# "¡Correcto! Llevas <n> dígitos acertados."
#Cada vez que numero sea diferente no saltamos de posicion y muestra mensaje
#"Incorrecto. Te quedan <n> intentos."

def ahorcado_numerico():
    nsecreto = int(input("Dime un número con el que jugar: "))
    intento = 1
    acertados = 0
    fallos = 0
    usados = []
    primero = str(((nsecreto // 1000) % 10))
    segundo = str(((nsecreto // 100) % 10))
    tercero = str(((nsecreto // 10) % 10))
    cuarto = str(((nsecreto // 1) % 10))

    for i in range(1,7):
        print ("Intento",intento , "de 6")
        n = input("¡A JUGAR!.Dame un numero")
        while n in usados:
            print("Ese número ya lo has probado, prueba otro")
            n = input("Dame un numero")
        usados.append(n)
        if n == primero:
            print("Acierto! El numero",n,"esta en el número secreto , Posicion 1")
            acertados = (acertados + 1)
            intento = (intento + 1)
            print ("Te quedan ",(6 - intento + 1 ),"intentos")
        elif n == segundo:
                    print("Acierto! El numero",n,"esta en el número secreto , Posicion 2")
                    acertados = (acertados + 1)
                    intento = (intento + 1)
                    print ("Te quedan ",(6 - intento + 1 ),"intentos")
                    
        elif n == tercero:
                    print("Acierto! El numero",n,"esta en el número secreto , Posicion 3")
                    acertados = (acertados + 1)
                    intento = (intento + 1)
                    print ("Te quedan ",(6 - intento + 1 ),"intentos")
                    
        elif n == cuarto:
                    print("Acierto! El numero",n,"esta en el número secreto , Posicion 4")
                    acertados = (acertados + 1)
                    intento = (intento + 1)
                    print ("Te quedan ",(6 - intento + 1),"intentos")
                    
        else:
            print("El numero no esta en el numero secreto")
            fallos = (fallos + 1)
            intento = (intento + 1)
            print ("Te quedan ",(6 - intento + 1 ),"intentos")
    if acertados >= 4:
           print("¡Has ganado!.")
    else:
           print("Has perdido")
        
ahorcado_numerico()
