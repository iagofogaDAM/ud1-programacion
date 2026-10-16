def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


n = int(input("Dime el número : "))

if n >= 2:
    if es_primo(n):
        print("Es primo")
    else:
        print("No es primo")
else:
    print("Número no válido")

# MUESTRA LOS NÚMEROS PRIMOS ENTRE 2 Y EL LÍMITE

lim = int(input("Dame el límite para que te diga los números primos : "))

for j in range(2, lim + 1):
    if es_primo(j):
        print(j)

#BUCLE HASTA QUE USUARIO INTRODUZCA CERO 

while True:
    num = int(input("Dame el número que quieras saber si es primo o 0 para cortar el bucle : "))
    if num == 0:
        break
    if es_primo(num):
        print("Es primo")
    else:
        print("No es primo")