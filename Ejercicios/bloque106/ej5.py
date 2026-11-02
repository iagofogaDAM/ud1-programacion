anio_nacimiento = int(input("Dime tu año de nacimiento : "))
anio_actual = int(input("Dime el año actual : "))
                  
def calcular_edad(anio_nacimiento: int, anio_actual: int) -> int:
    if anio_nacimiento > anio_actual:
          raise ValueError
    
    try:
        edad = (anio_actual - anio_nacimiento)
        print("Tu edad es : ",edad)      
    except TypeError:
            print("Los años deben ser números enteros.")
        

calcular_edad(anio_nacimiento , anio_actual)
    
    

