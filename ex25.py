# Funció crear_punts tal com la teníem
def crear_punts(llista):
    for numero in llista:
        print("." * numero)

# Funció que dibuixa una imatge utilitzant crear_punts
def dibuixa_triangle():
    """
    Dibuixa un triangle amb punts a la pantalla
    """
    # Cada número indica quants punts hi haurà a cada línia
    llista_punts = [1, 2, 3, 4, 5]
    crear_punts(llista_punts)

# Prova de la funció
dibuixa_triangle()