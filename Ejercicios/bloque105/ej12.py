def resumen_numeros(a, b, c, d, e):
    #ELIGE EL MAYOR DE LOS 5 NUMEROS
    maxi = max(a,b,c,d,e)
    #ELIGE EL MENOR DE LOS 5 NUMEROS
    mini = min(a,b,c,d,e)
    #SUMA EL VALOR ABSOLUTO DE LOS 5 NUMEROS
    absu = (abs(a)+abs(b)+abs(c)+abs(d)+abs(e))
    #IMPRIME LOS VALORES
    print (maxi , mini ,absu)
resumen_numeros(1,5,-7,9,2)