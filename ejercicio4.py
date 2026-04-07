import statistics

cafe = [14.2, 13.8, 14.5, 13.3, 12.6, 13.9, 11.5, 12.8, 14.0, 13.4]

media   = statistics.mean(cafe)
mediana = statistics.median(cafe)
mayor   = max(cafe)
menor   = min(cafe)
año_mayor = cafe.index(mayor) + 1
año_menor = cafe.index(menor) + 1
sobre_13   = sum(1 for x in cafe if x > 13)

print(f"Media:   {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Mayor producción: año {año_mayor} ({mayor})")
print(f"Menor producción: año {año_menor} ({menor})")
print(f"Años sobre 13M: {sobre_13}")