# Programa per calcular edats i mostrar-les tabulades

# Entrada de l'any actual
any_actual = int(input("Introdueix l'any actual: "))

# Creem llistes buides per noms i anys de naixement
noms = []
anys_naixement = []

# Entrada de dades de 4 persones
for i in range(4):
    nom = input(f"Introdueix el nom de la persona {i+1}: ")
    any_naix = int(input(f"Introdueix l'any de naixement de {nom}: "))
    noms.append(nom)
    anys_naixement.append(any_naix)

# Mostrar la capçalera
print("\nNom\t\tData naixement\tAnys que farà aquest any")
print("-" * 45)

# Calcular i mostrar dades de cada persona
for i in range(4):
    edat = any_actual - anys_naixement[i]
    print(f"{noms[i]:<12}{anys_naixement[i]:<16}{edat}")
