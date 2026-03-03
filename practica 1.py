
print(range(3)) # genera rango de 0 al numero que le asignas.
# start, stop, step

for indice in range(len("hola")):
    print(indice, end= " -> ")
    print("hola"[indice])

for indice, elemento in enumerate("hola"): # enumerate crea tuplas que contienen indice y valor del objeto iterable que le pases
    print("indice", indice, "elemento", elemento)
    