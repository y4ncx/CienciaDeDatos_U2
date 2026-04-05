import numpy as np

# Datos del ejercicio 10:
# 'Inflación anual ( % )'.
inflacion = np.array([ 3.8, 3.2, 3.5, 2.9, 1.6, 5.6, 9.3, 13.1 ])

# Media y Mediana --
# 'np.mean' = Calcula la media.
# 'np.median' = Calcula la mediana.
media = np.mean(inflacion)
mediana = np.median(inflacion)

# Año con inflacion más alta --
# 'np.argmax' = Devuelve la posicion donde
#   se encuentra el numero más alto.
# 'np.max' = Calcula el numero más alto.
año_max = np.argmax(inflacion) + 1
valor_max = np.max(inflacion)

# Años por debajo del promedio --
# 'np.sum(condición)' = Cuenta cuantos cumplen con la condicion,
#   similar a un 'SUMAR.SI.CONJUNTO' en excel.
debajo_prom = np.sum(inflacion < media)

# Impacto del valor más alto --
# 'np.delete' = Elimina elementos de una arreglo y devuelve
#   uno nuevo.
sin_max = np.delete(inflacion, np.argmax(inflacion))
media_sin_max = np.mean(sin_max)

# -- Resultados Impresos --
print("--- 10. Inflación anual ( % ) ---")
print("Media:", media)
print("Mediana:", mediana)
print("Año con inflacion más alta:", año_max, "con", valor_max)
print("Años por debajo del promedio:", debajo_prom)
print("Media sin el valor más alto:", media_sin_max)