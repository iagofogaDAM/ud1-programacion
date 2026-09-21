salariobruto = float(input("Introduce el salario bruto: "))
irpf = float(input("Introduce el porcentaje de IRPF: "))
print("El salario neto es: ", salariobruto - (salariobruto * irpf / 100))
