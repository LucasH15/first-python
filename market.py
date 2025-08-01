import sys

liste = []

while True:
    print("Choisissez parmi les 5 options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")
    choice = input("👉🏻 Votre choix : ")

    if choice.isdigit() and int(choice) >= 1 and int(choice) <= 5:
        choice = int(choice)
        if choice == 1:
            liste.append(input("Entrez le nom d'un élément à ajouter à la liste de course : "))
            print(f"L'élément {liste[-1]} a bien été ajouté à la liste.")
        if choice == 2:
            toDelete = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
            if toDelete in liste:
                liste.remove(toDelete)
                print(f"L'élément {toDelete} a bien été supprimé de la liste.")
            else:
                print(f"L'élément {toDelete} n'est pas dans la liste.")
        if choice == 3:
            if len(liste) == 0:
                print("Votre liste ne contient aucun élément.")
            else:
                print("Voici le contenu de votre liste :")
                for i, elem in enumerate(liste):
                    print(f"{i + 1}. {elem}")
        if choice == 4:
            liste.clear()
            print("La liste a été vidée de son contenu.")
        if choice == 5:
            print("A bientôt !")
            sys.exit()
    print("-----------------------------------")