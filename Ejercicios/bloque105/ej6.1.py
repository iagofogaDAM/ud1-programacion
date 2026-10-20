
def es_nombre_valido(nombre):

    # Verifica que la cadena está vacía
    if nombre == "":
        print("No es un nombre válido")
        return False

    # Verifica que la cadena no tienen números
    for letra in nombre:
        if letra.isdigit():
            print("No es un nombre válido")
            return False

    longitud = len(nombre)
    # Verifica que la cadena no 
    for letra in nombre: 
        if not letra.isspace():
            print("No es un nombre válido")
            return True
        
    return False
  
 
nombre = input("Dame un nombre válido: ")

while not es_nombre_valido(nombre):
    nombre = input("Dame un nombre válido: ")

edad = int(input("Dame tu edad: "))
email = input("Dame tu email: ")


