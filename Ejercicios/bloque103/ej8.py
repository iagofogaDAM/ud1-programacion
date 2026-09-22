a = int(input("Dame un lado del triangulo"))
b = int(input("Dame otro lado del triangulo"))
c = int(input("Dame el ultimo lado del triangulo"))

if a == b and a == c :
    print ("Es un triangulo equilatero")
elif a == b or a == c or b==c :
    print ("Es un triangulo isosceles")
else :
    print ("Es un triangulo escaleno")