n = int(input("¿Cuántas filas quieres?: "))

num1 = 0
num2 = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num1, end=" ")

        resultado = num1 + num2
        num1 = num2
        num2 = resultado

    print()



  