# Definim la funció
def lenp(frase):
    """
    Retorna una llista amb la longitud de cada paraula de la frase.
    """
    paraules = frase.split()  # Separa la frase en paraules
    longituds = list(map(len, paraules))  # Aplica len a cada paraula
    return longituds

# Proves de la funció
frase1 = "Hola món Python és genial"
print(lenp(frase1))  # [4, 3, 6, 2, 5]

frase2 = "Aquest és un exemple"
print(lenp(frase2))  # [6, 2, 2, 7]