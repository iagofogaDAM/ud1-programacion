nsegundos = int(input("Introduce el número de segundos: "))
print("Equivalente en horas: ", nsegundos // 3600)
print("Equivalente en minutos y segundos: ", nsegundos // 60, ":", nsegundos % 60)
print("Minutos:", (nsegundos % 3600) // 60)