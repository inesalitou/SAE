import random

class JeuJustePrix:
    def __init__(self):
        # Modifions la plage pour que le nombre à deviner soit en dehors de la séquence d'essais dans le test
        self.nombre_a_deviner = random.randint(101, 200)
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
