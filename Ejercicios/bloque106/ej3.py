def doble_numero() :
#Añado bucle para que repita si no es un numero 
# Funcionaría igual sin el , pero el continue y el break habria que eliminarlo  
    while True:
        try:
            num = float(input("Dame un numero: "))
        except ValueError:
            print("Eso no es un numero valido")
            continue
        else :
            doble = (num * 2)
            print("El doble de tu numero es: ",doble)
            break
doble_numero()
