def pedir_entero_positivo():
    while True:
        numero = int(input("Dame un número: "))
        if numero > 0:
            return numero
        print("Dame un número entero que sea positivo")

numero = pedir_entero_positivo()
print("Tu número:", numero)
