a = int(input("Dame un lado del triangulo"))
b = int(input("Dame otro lado del triangulo"))
c = int(input("Dame el ultimo lado del triangulo"))

if a == b and a == c :
    print ("Es un triangulo equilatero")
elif a == b or a == c or b==c :
    print ("Es un triangulo isosceles")
elif a <= 0 or b <= 0 or c <=0 :
    print ("No es un triangulo valido")
else :
    print ("Es un triangulo escaleno")