import random

# Funció per generar el codi aleatori de 4 xifres
def generar_codi():
    return [random.randint(0, 9) for _ in range(4)]

# Funció per comprovar l'endevinalla
def comprovar_codi(codi_secret, intent):
    encertats = 0  # nombres en la posició correcta
    coincidencia = 0  # nombres correctes però en posició diferent

    codi_secret_copy = codi_secret.copy()
    intent_copy = intent.copy()

    # Primer comprovem els encertats (mateixa posició i número)
    for i in range(4):
        if intent_copy[i] == codi_secret_copy[i]:
            encertats += 1
            # Marquem com a utilitzat
            codi_secret_copy[i] = intent_copy[i] = -1

    # Comprovem coincidències (mateix número però posició diferent)
    for i in range(4):
        if intent_copy[i] != -1 and intent_copy[i] in codi_secret_copy:
            coincidencia += 1
            # Marquem com a utilitzat
            codi_secret_copy[codi_secret_copy.index(intent_copy[i])] = -1

    return encertats, coincidencia

# Programa principal
print("Benvingut a MasterMind simplificat!")
print("Has d'endevinar un codi de 4 xifres (0-9).")

codi_secret = generar_codi()
intents = 0

while True:
    entrada = input("Introdueix un codi de 4 xifres: ")
    if len(entrada) != 4 or not entrada.isdigit():
        print("Codi invàlid. Introdueix exactament 4 xifres.")
        continue

    intent = [int(x) for x in entrada]
    intents += 1

    encertats, coincidencia = comprovar_codi(codi_secret, intent)

    if encertats == 4:
        print(f"Enhorabona! Has endevinat el codi {codi_secret} en {intents} intents.")
        break
    else:
        print(f"{encertats} xifres estan en la posició correcta, {coincidencia} xifres coincideixen però en posició diferent.\n")