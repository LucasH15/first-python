while True:
    premier_nombre = input("Entrez un premier nombre : ")
    deuxieme_nombre = input("Entrez un deuxième nombre : ")

    if premier_nombre.isdigit() and deuxieme_nombre.isdigit():
        print(f"Le résultat de l'addition de {premier_nombre} avec {deuxieme_nombre} est égal à {int(premier_nombre) + int(deuxieme_nombre)}")
        break
    else:
        print("Veuillez entrer deux nombres valides")