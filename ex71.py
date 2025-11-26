def llegir_fitxer(nom_fitxer):
    """
    Llegeix el contingut d'un fitxer i el retorna com una llista de línies.
    Controla errors si el fitxer no existeix o si hi ha algun problema en obrir-lo.
    """
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            contingut = fitxer.readlines()  # Llegeix totes les línies
        return contingut
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return None
    except IOError:
        print(f"Error: Problema obrint o llegint el fitxer '{nom_fitxer}'.")
        return None

# Prova de la funció
nom_fitxer = "exemple.txt"
linies = llegir_fitxer(nom_fitxer)
if linies is not None:
    print("Contingut del fitxer:")
    for linia in linies:
        print(linia.strip())  # Elimina salts de línia addicionals
