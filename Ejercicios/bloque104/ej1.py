print ("1.Sumar")
print ("2.Restar")
print ("3.Salir")

while  True :
    opc = input("Elige entre: 1 , 2 o 3 : ")
    if opc == "1" :
        a = int(input("Dame el primer número"))
        b = int(input("Dame el segundo número"))
        x = (a+b)
        print ("Tu suma es ",x )
    elif opc == "2" :
        a = int(input("Dame el primer número"))
        b = int(input("Dame el segundo número"))
        c = (a-b)
        print ("Tu resta es ",c )
    elif opc == "3" :
         print ("SALIENDO!")
         break
    else :
         print ("ErRor 404 , USA UNA OPCIÓN VALIDA")   
    