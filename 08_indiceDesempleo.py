import time

desempleo = [9.4, 10.5, 11.2, 15.9, 13.7, 12.1, 11.0, 10.3]

# Calcular la media del desempleo
media_desempleo = sum(desempleo) / len(desempleo)

# Calcular el año con mayor desempleo
max_year = desempleo.index(max(desempleo)) + 1  # +1 para ajustar al año

min_year = desempleo.index(min(desempleo)) + 1  # +1 para ajustar al año

year_higher_11 = sum(1 for rate in desempleo if rate > 11) # Bucle que recorre el array y genera un 1 por cada año cuya tasa de desempleo haya sido > 11

print("===========================================")
print("=====  Analisis Indices de  Desempleo =====")
print("===========================================")
print()
print()

time.sleep(1)

print("Datos : ", desempleo)
print()

time.sleep(2)

print("Respuestas a las preguntas:")
print()
time.sleep(2)

print("1. La media del desempleo es: ", media_desempleo)
print()
time.sleep(2)

print("2. El año con mayor desempleo es el año: ", max_year)
print()
time.sleep(2)

print("3. El año con menor desempleo es el año: ", min_year)
print()
time.sleep(2)

print("4. El numero de años que superaron el 11% de desempleo es: ", year_higher_11)
print()
time.sleep(2)

print("Muchas gracias")
print()
print()
print()