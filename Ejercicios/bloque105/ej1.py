n = float(input("Dime el número de horas : "))

def calcular_importe(horas):
    if n <= 1 :
        print ("gratis")
    elif n > 1 and n <= 4 :
        precio = (n * 1.50)
        print ("Importe a pagar:",precio,"€")
    elif n > 4:
        precio = (6+((n-4)))
        print ("Importe a pagar:",precio,"€")   
    else :
        print () 
calcular_importe(n)