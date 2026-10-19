def es_nombre_valido(nombre):
    for letra in nombre:
        if letra.isspace():
            print("No es un nombre válido")
            return False
        elif letra.isdigit():
            print("No es un nombre válido")
            return False
        
    edad = int(input("Dame tu edad : "))
    email = input("Dame tu email : ")
    return True


nombre = input("Dame un nombre válido: ")
es_nombre_valido(nombre)
