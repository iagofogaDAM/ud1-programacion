def saludar(nombre, formal=False):
    if formal == False:
        print("Hola",nombre)
    else :
        print("Buenos días,",nombre)

saludar("paco",True)
saludar("paco")