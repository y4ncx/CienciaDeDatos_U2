import statistics

puntajes = [250,270,300,290,310,280,260,275,295,305,
            310,280,270,260,250,300,320,310,295,285]

media  = statistics.mean(puntajes)
moda   = statistics.mode(puntajes)
maximo = max(puntajes)
minimo = min(puntajes)
sobre_media = sum(1 for x in puntajes if x > media)

print(f"Media:   {media:.2f}")
print(f"Moda:    {moda}")
print(f"Máximo:  {maximo}")
print(f"Mínimo:  {minimo}")
print(f"Sobre la media: {sobre_media} estudiantes")