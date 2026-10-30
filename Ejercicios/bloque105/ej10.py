def calcular_propina(cuenta, porcentaje=10, personas=1):
    total = cuenta * (1 + porcentaje / 100)
    return total / personas

print (calcular_propina(cuenta=300))
print (calcular_propina(cuenta=50 , personas=3))
print (calcular_propina(cuenta=800 , personas=15 , porcentaje=25))