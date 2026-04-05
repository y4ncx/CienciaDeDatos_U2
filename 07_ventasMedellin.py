# Importamos libreria para hacer calculos
import statistics
import time

ventas = [45, 50, 48, 60, 55, 52, 70, 65, 58, 62, 59, 75]

# Calculamos la media y la mediana de ventas

media_ventas = sum(ventas) / len(ventas)

mediana_ventas = statistics.median(ventas)

# Identificamos el mes con mas ventas

mes_mas_ventas = ventas.index(max(ventas)) + 1  # +1 para ajustar al número de mes

# Calculamos cuantos meses superaron los 60

mes_mayores_60 = sum(1 for venta in ventas if venta > 60) # Bucle que recorre el array y genera un 1 por cada mes cuya venta haya sido > 60

print("===========================================")
print("=====  Analisis de Ventas En Medellin =====")
print("===========================================")
print()
print()

time.sleep(1)

print("Datos : ", ventas)

time.sleep(2)
print()

print("Respuestas a las preguntas:")

time.sleep(2)
print()

print("1. La media de ventas es: ", media_ventas)

time.sleep(2)
print()

print("2. La mediana de ventas es: ", mediana_ventas)

time.sleep(2)
print()

print("3. El mes con mas ventas es el mes: ", mes_mas_ventas)

time.sleep(2)
print()

print("4. El numero de meses que superaron los 60 es: ", mes_mayores_60)

time.sleep(2)
print()

print("Muchas gracias")
print()
print()
print()