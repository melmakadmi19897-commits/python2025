from abc import ABC, abstractmethod

# -------------------------
# Classe base Animal
# -------------------------
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        print(f"{self.especie} fa un crit especial!")

# -------------------------
# Subclasses
# -------------------------
class Cavall(Animal):
    def xerrar(self):
        print("El cavall rebla!")
    def mourem(self):
        print("El cavall galopa!")

class Dofi(Animal):
    def xerrar(self):
        print("El dofí xiula!")
    def mourem(self):
        print("El dofí neda ràpid!")

class Abella(Animal):
    def xerrar(self):
        print("L'abella fa buzz!")
    def mourem(self):
        print("L'abella vola!")
    def picar(self):
        print("L'abella pica!")

class Humà(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        print(f"{self.nom} parla!")

    def mourem(self):
        print(f"{self.nom} camina o corre!")

class Fiet(Humà):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares  # Llista de noms dels pares

    def nompares(self):
        print(f"Els pares de {self.nom} són: {', '.join(self.pares)}")

class Centaure(Cavall, Humà):
    def xerrar(self):
        print("El centaure parla i relinxa alhora!")
    def mourem(self):
        print("El centaure galopa i camina alhora!")

# -------------------------
# Classe xou (independent)
# -------------------------
class Xou:
    def xerrar(self):
        print("Xou crida!")

    def mourem(self):
        print("Xou es mou!")

    def quisoc(self):
        print("Xou fa un truc especial!")

# -------------------------
# Creació d'objectes
# -------------------------
elements = [
    Cavall("Cavall", 5),
    Dofi("Dofí", 3),
    Abella("Abella", 1),
    Humà("Humà", 30, "Joan"),
    Fiet("Humà", 10, "Fiet", ["Anna", "Pere"]),
    Centaure("Centaure", 25, "Cent"),
    Xou()
]

# -------------------------
# Bucle que crida els mètodes comuns
# -------------------------
for element in elements:
    print(f"\n--- {type(element).__name__} ---")
    element.xerrar()
    element.mourem()
    element.quisoc()
    # Mètodes addicionals específics
    if isinstance(element, Abella):
        element.picar()
    if isinstance(element, Fiet):
        element.nompares()
