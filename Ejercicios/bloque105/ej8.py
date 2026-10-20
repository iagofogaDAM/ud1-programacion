def pedir_entero_positivo(numero):
    while True:
        if numero < 0 :
            print ("E")
            return True
        else :
            return False

numero = (int(input("Dame un número")))
pedir_entero_positivo(numero)
