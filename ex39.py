# Programa per comprovar rimes
def comprovar_rima(paraula1, paraula2):
    # Convertim a minúscules per evitar problemes de majúscules
    p1 = paraula1.lower()
    p2 = paraula2.lower()

    if len(p1) < 2 or len(p2) < 2:
        return "Una o ambdues paraules són massa curtes per rimar."

    # Comparació de les darreres 3 lletres
    if len(p1) >= 3 and len(p2) >= 3 and p1[-3:] == p2[-3:]:
        return "Rimen perfectament (3 darreres lletres coincideixen)."
    # Comparació de les darreres 2 lletres
    elif p1[-2:] == p2[-2:]:
        return "Rimen una mica (2 darreres lletres coincideixen)."
    else:
        return "No rimen."

# Entrada de l'usuari
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

# Comprovació de rima
resultat = comprovar_rima(paraula1, paraula2)
print(resultat)