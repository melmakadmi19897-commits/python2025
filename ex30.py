# Programa per convertir binari a enter
binari = input("Introdueix un número binari: ")

try:
    enter = int(binari, 2)  # Convertim de base 2 a enter
    print(f"El número binari {binari} és {enter} en decimal.")
except ValueError:
    print("Error: el valor introduït no és un número binari vàlid.")
