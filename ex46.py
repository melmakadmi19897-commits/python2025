# Programa per mostrar els dígits parells d'un número

# Entrada del número
while True:
    try:
        numero = int(input("Introdueix un número enter: "))
        break
    except ValueError:
        print("Entrada invàlida. Introdueix un número enter.")

# Convertim el número a cadena i filtrem els dígits parells
digits_parells = [d for d in str(abs(numero)) if int(d) % 2 == 0]

# Mostrar resultat
if digits_parells:
    print(f"Dígits parells de {numero}: {' '.join(digits_parells)}")
else:
    print(f"No hi ha dígits parells a {numero}.")
