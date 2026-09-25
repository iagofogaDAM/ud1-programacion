hep = int(input("Dime las horas de estancia en el parking: "))


if hep <= 1:
    print ("GRATIS!")
elif hep > 1 and hep <= 4 :
    print (hep * 1.50 , "€")
elif hep == 4  :
    print (6 , "€")
else :
    print ((6 + (hep-4) *1) ,"€", "Caaarallo. Pasaches media vida aqui, seica non tes casa ouuu!")