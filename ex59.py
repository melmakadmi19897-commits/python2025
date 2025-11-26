# Programa per mostrar el patró de números

for i in range(5, 0, -1):  # Comença des de 5 fins a 1
    for j in range(i, 0, -1):  # Comença des de i fins a 1
        print(j, end=' ')
    print()  # Salt de línia després de cada fila