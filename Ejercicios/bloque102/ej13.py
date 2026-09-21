edad_texto = input("Dime tu edad: ")
altura_texto = input("Dime tu altura en metros: ")
peso_texto = input("Dime tu peso en kg: ")

edad = int(edad_texto)
altura = float(altura_texto)
peso = float(peso_texto)

mayoredad = edad >= 18


imc = (peso) / (altura ** 2)

print("Edad:", edad)
print("Altura:", altura)
print("Es mayor:", mayoredad)
print("IMC:", imc)

