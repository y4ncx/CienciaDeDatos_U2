import numpy as np

# Datos del ejercicio 09:
# 'Caudal mensual del Río Magdalena ( m^3/s )'. 
caudal = np.array([ 7200, 7500, 8000, 7800, 7600, 7400, 7100, 6900, 6700, 7000, 7300, 7600 ])

# Media anual:
# 'np.mean()' calcula la media.
media = np.mean(caudal)

# Mes con mayor caudal:
# 'np.argmax()' calcula el indice del valor maximo.
mes_max = np.argmax(caudal) + 1 # '+1' porque los meses empiezan en 1.
max_valor = np.max(caudal)

# Mes con menor caudal
# 'np.argmin()' calcula el indice del valor minimo,
mes_min = np.argmin(caudal) + 1
min_valor = np.min(caudal)

# Meses que superan la media
# 'np.sum(condición)' cuenta cuantos cumplen con la condicion,
# similar a un 'SUMAR.SI.CONJUNTO' en excel.
meses_sup = np.sum(caudal > media)

# -- Resultados Impresos --
print("--- 09. Caudal mensual del Río Magdalena ( m^3/s ) ---")
print("Media anual:", media)
print("Mes con mayor caudal:", mes_max, "con", max_valor)
print("Mes con menor caudal:",mes_min, "con", min_valor)
print("Meses que superan la media:", meses_sup)