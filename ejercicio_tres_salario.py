import numpy as np

# Datos de salarios 
salarios = np.array([737717, 781242, 828116, 877803, 908526, 1000000, 1160000, 1300000])

print("--- 3. Salario mínimo en Colombia ---")
# Media del salario 
media_salario = np.mean(salarios)
print(f"Media del salario: {media_salario:.2f} COP")

# Mediana del salario 
mediana_salario = np.median(salarios)
print(f"Mediana del salario: {mediana_salario:.2f} COP")

# Incremento máximo entre dos años consecutivos 
# np.diff resta el valor actual menos el anterior en todo el array
incrementos = np.diff(salarios)
max_incremento = np.max(incrementos)
print(f"Incremento máximo entre dos años consecutivos: {max_incremento} COP")

# Años que superan el promedio 
anios_superan_promedio = np.sum(salarios > media_salario)
print(f"Años que superan el promedio de salario: {anios_superan_promedio}")