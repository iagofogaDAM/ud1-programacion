pu = float(input("Dame el precio unitario : "))
ca = int(input("Dime la cantidad de articulos : "))
s = input("Eres socio? S/N :")
pi = (pu * ca)
if ca >= 3 and s == "N" :
    print (pi * 0.90)
elif ca >= 3 and s == "S":
     print (pi * 0.85)
elif ca < 3 and s == "S":
     print (pi * 0.95)
else :
     print ("NO HAY DESCUENTO!" , pi , "Hazte Socio Joder! ")

    