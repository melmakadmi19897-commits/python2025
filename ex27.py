# Definim la funció
def paraula_mes_llarga(llista_paraules):
    """
    Retorna la paraula amb més caràcters d'una llista de paraules.
    """
    if not llista_paraules:  # Comprovem si la llista està buida
        return None

    mes_llarga = llista_paraules[0]
    for paraula in llista_paraules:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula
    return mes_llarga

# Proves de la funció
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))  # "Paraula"
print(paraula_mes_llarga(["a", "ab", "abc", "abcd"]))           # "abcd"
print(paraula_mes_llarga(["x", "y", "z"]))                      # "x" (totes iguals)
print(paraula_mes_llarga([]))                                   # None