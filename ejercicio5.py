import statistics

dengue = [12,15,14,20,18,17,19,25,22,18,16,14,13,15,21]

media   = statistics.mean(dengue)
mediana = statistics.median(dengue)
moda    = statistics.mode(dengue)
dia_max = dengue.index(max(dengue)) + 1
sobre_18 = sum(1 for x in dengue if x > 18)

print(f"Media:   {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda:    {moda}")
print(f"Día con más casos: día {dia_max} ({max(dengue)} casos)")
print(f"Días sobre 18 casos: {sobre_18}")