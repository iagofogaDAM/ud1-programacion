def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


for valor in [0, 1, 2, 4, 5, 7, 10]:
    rec = factorial(valor)
    ite = factorial_iterativo(valor)
    igual = (rec - ite)
    if igual == 0:
        print(rec , ite , "son iguales")
    