def calculadora():
    print("=== CALCULADORA ===")
    print("Operacions disponibles:")
    print(" +  Suma")
    print(" -  Resta")
    print(" *  Multiplicació")
    print(" /  Divisió")
    print(" ** Exponenciació")
    print(" %  Mòdul")
    print(" // Divisió sencera")
    print("====================")

    num1 = float(input("Introdueix el primer número: "))
    operacio = input("Introdueix l'operació: ")
    num2 = float(input("Introdueix el segon número: "))

    if operacio == "+":
        resultat = num1 + num2
    elif operacio == "-":
        resultat = num1 - num2
    elif operacio == "*":
        resultat = num1 * num2
    elif operacio == "/":
        if num2 == 0:
            return "Error: divisió per zero!"
        resultat = num1 / num2
    elif operacio == "**":
        resultat = num1 ** num2
    elif operacio == "%":
        if num2 == 0:
            return "Error: mòdul amb zero!"
        resultat = num1 % num2
    elif operacio == "//":
        if num2 == 0:
            return "Error: divisió sencera entre zero!"
        resultat = num1 // num2
    else:
        return "Operació no vàlida!"

    return f"Resultat: {resultat}"


# Programa principal
print(calculadora())