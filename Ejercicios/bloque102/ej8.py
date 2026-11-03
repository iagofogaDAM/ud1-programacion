quilometrosrecorridos = float(input("Introduce la cantidad de kilómetros recorridos: "))
preciodelcombustible = float(input("Introduce el precio del combustible: "))
consumo = float(input("Introduce el consumo (l/100 km): "))
litros = quilometrosrecorridos * consumo / 100
coste = litros * preciodelcombustible
print("El gasto en combustible es: ", coste)
