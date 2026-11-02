def reintento_hasta_positivo():
    while True:
        try:
            num = int(input("Dame un numero entero positivo: "))
        except ValueError:
            print ("El valor introducido no es in numero entero intentalo de nuevo: ")
            continue
        if num < 0 :
            print ("No es un numero positivo, intentalo de nuevo: ")
            continue
        else :
            print("Tu número es : ", num)
            break

reintento_hasta_positivo()
                          
