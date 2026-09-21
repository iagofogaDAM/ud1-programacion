import math
coeficientea = float(input("Introduce el coeficiente a: "))
coeficienteb = float(input("Introduce el coeficiente b: "))
coeficientec = float(input("Introduce el coeficiente c: "))
print("El resultado es: ", (-coeficienteb + math.sqrt(coeficienteb**2 - 4*coeficientea*coeficientec)) / (2 * coeficientea))   