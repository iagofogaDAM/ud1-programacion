peso = float(input("Dime tu peso :"))
alt = float(input("Dime tu altura :"))
imc = (peso / alt * 2)

if imc < 18.5 :
 print ("Bajo peso")
elif imc >= 18.5 and imc < 24.9 :
 print ("Normal")
elif imc >= 25 and imc < 29.9 :
 print ("Sobrepeso")
elif imc > 30 :
 print ("Obesidad")