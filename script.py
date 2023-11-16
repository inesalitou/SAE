import random

class JeuJustePrix:
    def __init__(self):
        # Correction : Utiliser la même plage que dans le test
        self.nombre_a_deviner = random.randint(1, 100)
        self.tentative = 0

    def deviner(self, essai):
        self.tentative += 1

        if essai < self.nombre_a_deviner:
            return "Trop bas. Essayez à nouveau."
        elif essai > self.nombre_a_deviner:
            return "Trop haut. Essayez à nouveau."
        else:
            return f"Bravo ! Vous avez deviné le juste prix en {self.tentative} tentatives."

if __name__ == "__main__":
    jeu = JeuJustePrix()
    print("Bienvenue au Jeu du Juste Prix!")

    while True:
        try:
            essai = int(input("Devinez le nombre (entre 1 et 100) : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        resultat = jeu.deviner(essai)
        print(resultat)

        if "Bravo" in resultat:
            break
