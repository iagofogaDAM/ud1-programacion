# Programa un simulador de caja con un menú en bucle con tres opciones:

# a) Añadir producto
# c) Cerrar ticket
# s) Salir 

# Las opciones:

# Añadir un producto debe pedir nombre y precio. A continuación, debe sumar el precio al ticket actual,
#  mostrando el total acumulado y el número de artículos.
# Cerrar el ticket debe mostrar el total final y reiniciar los acumuladores a cero.
# Salir termina el programa.
# Organiza el código, por lo menos, en las funciones anadir_producto y cerrar_ticket. 
# Con las herramientas que tienes hasta ahora te bastan variables acumuladoras
# (total y número de artículos). 
# Cuando veamos listas más adelante, podrás ampliarlo para recordar también el nombre de cada producto 
# del ticket.


def añadir_producto():
    nombre = input("Dime el nombre del producto : ")
    precio = float(input("Dime el precio del producto : asdfa"))
    return precio


def cerrar_ticket(total,articulos):
    print("Has comprado ",articulos, "articulos")
    print("El precio total es de :",total,"€")

def cajasim():
    articulos = 0
    total = 0
    while True:
        cliente = input("Que deseass hacer?: a) Añadir producto , c) Cerrar Ticket , s) Salir")
        if cliente == "a":
            precio = añadir_producto()
            total = (precio + total)
            articulos = (articulos + 1)            
        elif cliente == "c":
            ticket = cerrar_ticket(total,articulos)
        elif cliente == "s":
            break

cajasim()
