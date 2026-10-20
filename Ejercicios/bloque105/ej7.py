
def convertir_temperatura(grados, a_fahrenheit=False):
    if a_fahrenheit:
        gradosf = float(grados * 9 / 5) + 32
        print(gradosf, "°F")
    else:
        gradosc = float(grados - 32) * 5 / 9
        print(gradosc, "°C")


grados = float(input("Dame unos grados: "))
convertir_temperatura(grados)

