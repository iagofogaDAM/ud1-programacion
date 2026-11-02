def procesar_edad(texto):
    try:
        num = int(texto)          
    except ValueError:
        print("Entrada no válida")
        print("Tu texto:", texto) # ← el parámetro original
        return None
    else:
        doble = num * 2
        print("El doble es:", doble)
        return doble
    finally:
        print("Intento de conversión finalizado")

 

procesar_edad("doce")
procesar_edad("25")

            
