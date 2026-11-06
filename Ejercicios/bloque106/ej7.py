def calcular_descuento_irpf(sueldo_bruto: float | int, irpf: int) -> float:

    if not isinstance(sueldo_bruto, (int, float)):
        print ("Error: Debes introducir numeros: ")
        raise TypeError
    if sueldo_bruto < 0 :
        print("Error: Los datos introducidos no son validos")
        raise ValueError
    if irpf < 0 :
            print("Error: Los datos introducidos no son validos")
            raise ValueError
    else:
        try:
            descuento = sueldo_bruto * (irpf / 100)
            print(sueldo_bruto * (irpf / 100))
        finally:
            return sueldo_bruto * irpf / 100
    
 
 
 
 
salario = int(input("Dame tu sueldo bruto: ")) 
irpf = int(input("Y tu irpf: "))  
calcular_descuento_irpf(salario , irpf)
calcular_descuento_irpf("1500",15)