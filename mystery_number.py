import random, sys

print("*** Le jeu du nombre mystère ***")
mystery_number = random.randint(0, 101)
nb_chance = 5
current_chance = 5

while True:
    print(f"Il te reste {current_chance} essais")
    number = input("Devine le nombre : ")

    if not number.isdigit():
        print("Veuillez entrer un nombre valide.")
    elif int(number) > mystery_number:
        print(f"Le nombre mystère est plus petit que {number}")
        current_chance -= 1
    elif int(number) < mystery_number:
        print(f"Le nombre mystère est plus grand que {number}")
        current_chance -= 1
    else:
        current_chance -= 1
        print(f"Bravo ! Le nombre mystère était bien {mystery_number} !")
        print(f"Tu as trouvé le nombre en {nb_chance - current_chance} essai")
        print("Fin du jeu.")
        sys.exit()

    if current_chance == 0:
        print(f"Dommage ! Le nombre mystère était {mystery_number}")
        print("Fin du jeu.")
        sys.exit()