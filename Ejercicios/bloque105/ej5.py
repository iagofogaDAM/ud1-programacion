a = int(input("Dame el primer número : "))
b = int(input("Dame el segundo número : "))
c = int(input("Dame el tercer número : "))

def estadisticas(a, b, c):
    minimo = min(a, b, c)
    maximo = max(a, b, c)
    media = (a + b + c)/3
    print(minimo,maximo,media)

estadisticas(a,b,c)