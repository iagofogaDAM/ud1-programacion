numero = int(input("Introduce un número entero positivo: "))

r = 0

while numero > 0:
    r += numero % 10
    numero //= 10

print("La suma es:", r)
