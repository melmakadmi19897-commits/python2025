# Definim la funció
def nums_que_comencen_per(llista_noms, lletra):
    """
    Retorna el nombre de noms que comencen per la lletra indicada.
    """
    comptador = 0
    lletra = lletra.lower()  # fem la comparació case-insensitive
    for nom in llista_noms:
        if nom.lower().startswith(lletra):
            comptador += 1
    return comptador

# Programa principal
noms = ["Anna", "Pere", "Albert", "Maria", "Ana", "Joan"]

lletra = input("Introdueix la lletra a comprovar: ")

resultat = nums_que_comencen_per(noms, lletra)
print(f"Noms que comencen per '{lletra}': {resultat}")