secret = "secret"

for palabra in range(5):
    palabra = input("Dime la palabra que piensas que es: ")

    if palabra == secret:
        print("¡Acertaste!")
        break
else:
    print("Has perdido")