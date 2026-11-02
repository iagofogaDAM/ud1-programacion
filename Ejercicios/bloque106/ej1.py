def division_controlada():
    num1 = int(input("Dame el primer número: "))
    num2 = int(input("Dame el segundo número: "))
    while True:
        try:
            print (num1 / num2)
            break
        except ZeroDivisionError:
            print ("Numero no valido")
            break
        except ValueError:
            print ("Caracter no valido")
            break

division_controlada()