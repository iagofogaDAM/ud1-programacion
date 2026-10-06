n = int(input("Dime el número"))

def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

for j in range(2,n):
    if es_primo  :
        print (j)
    else :
        print (...)
c = int(input("Dime el número"))
es_primo(c)
