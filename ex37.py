import random
import time

# Funció on expliquem què passa
def intro():
    print ("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
""")

# Funció on demanem a quin talaiot volem anar
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Funció que ens indica si compartiran el menjar o serem nosaltres el seu àpat
def trobada(canviTalaiot):
    print("T'estas apropant al talaiot...")
    time.sleep(2)
    print("Està fosc i és tenebrós...")
    time.sleep(2)
    print("Un gran gegant salta davant teu, t'agafa i ...\n")
    time.sleep(2)
    gegantamic = random.randint(1, 2)
    if canviTalaiot == str(gegantamic):
        print("Et convida a menjar...")
        return True  # Ha guanyat un punt
    else:
        print("Se't menja d'un mos...ÑAMÑAMÑAM")
        return False  # Ha perdut

# Funció principal amb sistema de punts
print("Benvingut al joc dels gegants!\n")
partidaNova = "si"

while partidaNova.lower() in ["s", "si"]:
    intro()
    punts = 0  # Inicialitzem els punts
    continuar = True
    while continuar:
        nTalaiot = canviTalaiot()
        if trobada(nTalaiot):
            punts += 1
            print(f"Has guanyat un punt! Punts actuals: {punts}\n")
        else:
            print(f"Joc acabat! Has aconseguit {punts} punts.\n")
            continuar = False
    partidaNova = input("Vols tornar a jugar? Introdueixi si o no: ")
    print("\n")

