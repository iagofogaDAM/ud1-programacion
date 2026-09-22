d = int(input("Dime un día"))
m = int(input("Dime un mes"))
a = int(input("Dime un año"))

bisiesto = (a % 4 == 0 and a % 100 != 0) or a % 400 == 0

if m < 1 or m > 12 :

    print ("Eso no es un més válido mongolo")

elif d < 1 :

    print ("Eso no es un día válido mongolo")

elif m == 2 and bisiesto and d > 29 :

    print ("Eso no es una fecha válida mongolo")

elif m == 2 and not bisiesto and d > 28 :

    print ("Eso no es una fecha válida mongolo")

elif m in [4, 6, 9, 11] and d > 30 :

    print ("Eso no es una fecha válida mongolo")

elif d > 31 :

    print ("Eso no es una fecha válida mongolo")

else :

    print ("Fecha valida")


    
    




