# Funció per demanar un número dins un rang
def demanar_numero(missatge, minim, maxim):
    while True:
        try:
            numero = int(input(missatge))
            if numero < minim or numero > maxim:
                print(f"El número ha d'estar entre {minim} i {maxim}. Torna-ho a provar.")
            else:
                return numero
        except ValueError:
            print("Entrada invàlida. Introdueix un número enter.")

# Entrada del número
num = demanar_numero("Introdueix un número per la taula de multiplicar (1-20): ", 1, 20)

# Imprimir la taula de multiplicar
print(f"\nTaula de multiplicar del {num}:")
for i in range(1, 11):  # multiplicadors de 1 a 10
    print(f"{num} x {i} = {num * i}")
