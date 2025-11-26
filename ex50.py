import random

# Funció per generar una llista de 20 elements aleatoris entre 1 i 100
def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]

# Funció per comprovar si hi ha duplicats
def hi_ha_duplicats(llista):
    """
    Retorna True si hi ha algun element duplicat a la llista,
    False en cas contrari.
    """
    return len(llista) != len(set(llista))

# Generem la llista
llista_aleatoria = llista_20_elements()
print("Llista generada:", llista_aleatoria)

# Comprovem si hi ha duplicats
if hi_ha_duplicats(llista_aleatoria):
    print("Hi ha elements duplicats.")
else:
    print("No hi ha elements duplicats.")
