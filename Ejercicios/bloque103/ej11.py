l1 = int(input("Dame un lado del triangulo"))
l2 = int(input("Dame otro lado del triangulo"))
l3 = int(input("Dame otro lado del triangulo"))

if l1 > l2 and l1 > l3 :
    c = l1
    a = l2
    b = l3 
if l2 > l1 and l2 > l3 :
    c = l2
    a = l1
    b = l3  
if l3 > l2 and l3 > l1 :
    c = l3
    a = l1
    b = l2  

if (a * a) + (b * b) == (c * c):
    print ("Es un triangulo rectangulo")
else :
    print ("No es un triangulo rectangulo")