gravedad = 9.8
altura_inicial = 13
tiempo = float(input("Ingrese el tiempo en segundos: "))

altura = (altura_inicial - 0.5 * gravedad * tiempo ** 2)
print("La altura del objeto después de", tiempo, "segundos es:", altura, "metros.")