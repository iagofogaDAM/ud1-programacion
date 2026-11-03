import math
coeficientea = float(input("Introduce el coeficiente a: "))
coeficienteb = float(input("Introduce el coeficiente b: "))
coeficientec = float(input("Introduce el coeficiente c: "))
raiz = math.sqrt(coeficienteb**2 - 4*coeficientea*coeficientec)
x1 = (-coeficienteb + raiz) / (2 * coeficientea)
x2 = (-coeficienteb - raiz) / (2 * coeficientea)
print("Soluciones:", x1, x2) 