import random

def lanzar_dado(caras=6):
    return random.randint(1, caras)


print("6 caras:", lanzar_dado())

print("20 caras:", lanzar_dado(20))