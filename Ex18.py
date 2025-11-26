def ex18(c):
    v = "aeiouAEIOUáàéèíìóòúùÁÀÉÈÍÌÓÒÚÙ"
    if c in v:
        return True
    else:
        return False
    
# Programa principal 
c = input("Escriure un caràcter per a provar si és o no vocal:")
print(ex18(c))