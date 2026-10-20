
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
    letrasval = 0 
    
    # Verifica que la cadena no es todo espacios
    for letra in nombre: 
        if letra.isspace():
            letrasval = letrasval + 1
    
    if longitud > letrasval:
        return True
      
        
    return False
  
 
nombre = input("Dame un nombre válido: ")

while not es_nombre_valido(nombre):
    nombre = input("Dame un nombre válido: ")

edad = int(input("Dame tu edad: "))
email = input("Dame tu email: ")