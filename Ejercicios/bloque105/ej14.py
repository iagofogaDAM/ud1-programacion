#LA FUNCION CALCULA EL PRECIO TOTAL DE UNA COMPRA , 
#ASI COMO EL PRECIO ANTES DE DESCUENTO Y DESPUES PERO SIN IMPRIMIR DICHO VALOR 
def calcular_precio_final(precio: float, cantidad: int, descuento: float = 0) -> float:
    tot = (precio * cantidad)
    des = (tot * (descuento / 100))
    total = (precio * cantidad - des)
    print ("El precio total es: ", total)

calcular_precio_final(3 , 7 , 10)
calcular_precio_final(3 , 7)