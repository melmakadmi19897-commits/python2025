# Definim la funció
def nums_que_comencen_per(llista_noms):
    """
    Retorna el nombre de noms que comencen per 'a' o 'A'.
    """
    comptador = 0
    for nom in llista_noms:
        if nom.lower().startswith('a'):
            comptador += 1
    return comptador

# Proves de la funció
noms = ["Anna", "Pere", "Albert", "Maria", "ana", "Joan"]
print(nums_que_comencen_per(noms))  # 3 (Anna, Albert, ana)

# Una altra prova
noms2 = ["Marc", "Jordi", "Marta"]
print(nums_que_comencen_per(noms2)) # 0