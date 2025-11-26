# Funció per comprovar si un número és primer
def es_primer(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Llista per guardar els números primers
primers = []

# Busquem els primers entre 1 i 100
for numero in range(1, 101):
    if es_primer(numero):
        primers.append(numero)

# Mostrem els primers i la seva quantitat
print("Números primers entre 1 i 100:")
print(primers)
print(f"Hi ha {len(primers)} números primers entre 1 i 100.")
