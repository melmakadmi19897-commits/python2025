# Programa per calcular la suma dels quadrats amb passos de 4

# Entrada del número
while True:
    try:
        n = int(input("Introdueix un número menor de 100: "))
        if n >= 100:
            print("El número ha de ser menor de 100. Torna-ho a provar.")
        else:
            break
    except ValueError:
        print("Entrada invàlida. Introdueix un número enter.")

# Inicialitzem la suma
suma_quadrats = 0

# Recorrem els números de n cap avall amb pas -4
for i in range(n, -1, -4):
    suma_quadrats += i**2
    print(f"{i}^2 = {i**2}")

# Mostrem el resultat final
print(f"Suma dels quadrats: {suma_quadrats}")