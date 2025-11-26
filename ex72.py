import os
from pathlib import Path

# 1️⃣ Crear directori Prova dins /home/cicles/AO
directori_base = Path("/home/cicles/AO")
directori_prova = directori_base / "Prova"
directori_prova.mkdir(parents=True, exist_ok=True)  # Crea el directori si no existeix

# 2️⃣ Canviar-se al directori creat
os.chdir(directori_prova)

# 3️⃣ Crear el fitxer Ex12.txt i escriure els noms dels companys
companys = ["Anna", "Pere", "Maria", "Joan", "Sofia"]  # Exemple de noms
with open("Ex12.txt", "w", encoding="utf-8") as fitxer:
    for nom in companys:
        fitxer.write(nom + "\n")

# 4️⃣ Obrir el fitxer per afegir els noms dels professors
professors = ["Sr. Ramis", "Sra. Torres"]  # Exemple de noms de professors
with open("Ex12.txt", "a", encoding="utf-8") as fitxer:
    for nom in professors:
        fitxer.write(nom + "\n")

# 5️⃣ Obrir finalment el fitxer i posar tot el seu contingut dins d'una llista
with open("Ex12.txt", "r", encoding="utf-8") as fitxer:
    llista_noms = [linia.strip() for linia in fitxer]  # strip() elimina salts de línia

# 6️⃣ Mostrar la llista final de noms
print(llista_noms)
