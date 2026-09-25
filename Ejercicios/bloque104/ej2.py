intentos = 0

while True :
    num = int(input("Dame un numero entero positivo"))
    if num <=0 :
        print ("NO ES VÁLIDO")
        intentos == (intentos + 1)
        continue
    else :
        print ("Numero Valido")
        break

