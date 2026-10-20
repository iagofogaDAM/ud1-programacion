nombre = "abc"

for letra in nombre:

    print(letra)



def es_nombre_valido(nombre):
    longitud = len(nombre)
    # Verifica que la cadena no 
    for letra in nombre: 
        if not letra.isspace():
            print("No es un nombre válido")
            return True
    
    return False
