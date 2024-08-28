# Calificaciones
calif_1 = 10
calif_2 = 7
calif_3 = 4

# % de las calificaciones
porc_1 = 0.15
porc_2 = 0.35
porc_3 = 0.50

# Cálculo del promedio
promedio_ponderado = (calif_1 * porc_1) + (calif_2 * porc_2) + (calif_3 * porc_3)
print(f"El promedio  de las calificaciones es: {promedio_ponderado}")

#----------------------------

# Matriz
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

# Corrección de la matriz
for fila in matriz:
    suma = sum(fila[:3])

    if fila[3] != suma:
        print(f"Corrigiendo fila {fila}")
        # Si no es igual, corregir el 4to valor
        fila[3] = suma
        print(f"Fila corregida: {fila}")
    else:
        print(f"Fila correcta: {fila}")

print("\nMatriz nueva:")
for fila in matriz:
    print(fila)

