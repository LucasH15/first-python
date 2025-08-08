class Voiture:
    essence = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d'essence")

    def roule(self, km):
        nb_litres = (km * 5) / 100

        if nb_litres <= self.essence:
            self.essence -= nb_litres

            if self.essence < 10:
                print("Vous n'avez bientôt plus d'essence !")
        else:
            print("Vous n'avez plus d'essence, faites le plein !")

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")
