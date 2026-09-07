recursos = ["computador","videobeam","salas"]
uso = [[0]*5 for _ in range(3)]

for i in range(3):
    for j in range(5):
        uso[i][j] = int(input(f"Ingrese el uso de {recursos[i]} el día {j+1}: "))

print(f"\nEl día con mayor uso de recursos es el día {dia_max} con un total de {max(totales_dia)} usos.")

for i, r in enumerate(recursos):
    print(f"\nEl recurso {r} tuvo un total de {totales_recurso[i]} usos en la semana.")
    
totales_dia = []
for dia in range(5):
    total = sum(uso[i][dia] for i in range(3))
    totales_dia.append(total)
    print(f"El total de usos el día {dia+1} es: {total}")
    
dia_max = totales_dia.index(max(totales_dia)) + 1
print(f"\nEl día con mayor uso de recursos es el día {dia_max} con un total de {max(totales_dia)} usos.")