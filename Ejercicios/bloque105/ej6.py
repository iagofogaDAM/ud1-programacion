def es_nombre_valido(nombre):
    if nombre == "":
        print("No es un nombre válido")
        return False
    for letra in nombre:
        if letra.isspace() or letra.isdigit():
            print("No es un nombre válido")
            return False
    return True


nombre = input("Dame un nombre válido: ")
while not es_nombre_valido(nombre):
    nombre = input("Dame un nombre válido: ")

edad = int(input("Dame tu edad: "))
email = input("Dame tu email: ")

