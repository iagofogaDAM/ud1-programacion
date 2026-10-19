def tirardado():
    import random
    n = random.randint(1, 6)
    return n
    

def tirar_dos_dados():
    dado1 = tirardado()
    dado2 = tirardado()
    return dado1,dado2

def jugar_ronda():
    dado1u,dado2u = tirar_dos_dados()
    dado1b,dado2b = tirar_dos_dados()
    print ("TUS DADOS SON : ",dado1u,dado2u) 
    print ("LOS DADOS DE LA BANCA SON :",dado1b,dado2b)
    dadosu = dado1u + dado2u
    dadosb = dado1b + dado2b
    if dadosu > dadosb :
        print (dadosu,"-",dadosb,"TU GANAS!!")
    elif dadosu < dadosb :
        print(dadosu,"-",dadosb,"GANA LA BANCA!")
    else :
        print(dadosu,"-",dadosb,"EMPATE!")

    

entrada = input("JUEGAS? : ")
if entrada == "SI" :
    jugar_ronda()
else :
    exit