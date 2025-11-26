# Definim la funció
def comptar_vocals(paraula):
    """
    Retorna un diccionari amb el nombre de vegades que apareix cada vocal en la paraula.
    """
    vocals = "aeiou"
    conteig = {v: 0 for v in vocals}
    
    for car in paraula.lower():
        if car in vocals:
            conteig[car] += 1
    
    return conteig

# Proves de la funció
paraula = "Ratapinyada"
resultat = comptar_vocals(paraula)

print(f"Paraula: {paraula}")
for v in "aeiou":
    print(f"{v}: {resultat[v]}")