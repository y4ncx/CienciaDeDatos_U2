import numpy as np


# Datos de temperaturas en Bogotá 
temperaturas = np.array([14, 15, 14, 13, 13, 12, 12, 13, 14, 14, 15, 14])

print("--- 2. Temperaturas promedio en Bogotá ---")
# Media y mediana 
media_temp = np.mean(temperaturas)
mediana_temp = np.median(temperaturas)
print(f"Media: {media_temp:.2f}°C")
print(f"Mediana: {mediana_temp}°C")

# Moda usando NumPy 
valores, conteos = np.unique(temperaturas, return_counts=True)
moda_temp = valores[np.argmax(conteos)]
print(f"Moda (Temperatura más frecuente): {moda_temp}°C")

# Temperatura máxima y mínima
max_temp = np.max(temperaturas)
min_temp = np.min(temperaturas)
print(f"Temperatura máxima: {max_temp}°C | Mínima: {min_temp}°C")

# Meses por debajo de 14°C 
meses_frios = np.sum(temperaturas < 14)
print(f"Meses con temperatura por debajo de 14°C: {meses_frios}")
print("\n")