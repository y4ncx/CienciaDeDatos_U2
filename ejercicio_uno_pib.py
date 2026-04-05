import numpy as np

# Datos del PIB 
pib = np.array([4.5, 3.2, 2.8, 1.4, -7.0, 10.6, 7.3, 3.5, 1.2, 0.6])

print("--- 1. Crecimiento del PIB en Colombia ---")
# Media del crecimiento 
media_pib = np.mean(pib)
print(f"Media del crecimiento: {media_pib:.2f}%")

# Año con mayor crecimiento y valor mínimo 
anio_max_pib = np.argmax(pib) + 1  # +1 para hablar de "Año 1, Año 2..." en lugar de índice 0
max_pib = np.max(pib)
min_pib = np.min(pib)
print(f"Año con mayor crecimiento: Año {anio_max_pib} ({max_pib}%)")
print(f"Valor mínimo de crecimiento: {min_pib}%")

# Efecto del dato negativo 
pib_sin_outlier = pib[pib >= 0]
media_sin_outlier = np.mean(pib_sin_outlier)
print(f"Efecto del dato negativo: Baja drásticamente el promedio nacional. Sin el -7.0%, la media sería {media_sin_outlier:.2f}% en lugar de {media_pib:.2f}%.")

# Años con crecimiento positivo 
anios_positivos = np.sum(pib > 0)
print(f"Años con crecimiento positivo: {anios_positivos}")
print("\n")