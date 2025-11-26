def majoria_edat(edat):
    if edat > 18:
        return "És major d'edat."
    elif edat < 18:
        return "No és major d'edat."
    else:
        return "Té exactament 18 anys."

# Programa que l’utilitza
edat = int(input("Introdueix la teva edat: "))
print(majoria_edat(edat))
