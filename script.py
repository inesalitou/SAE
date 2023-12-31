import random

class JeuJustePrix:
    def __init__(self):
        # Correction : Utiliser la même plage que dans le test
        self.nombre_a_deviner = random.randint(1, 100)
        self.tentative = 0
        self.niveau = None

    def deviner(self, essai):
        try:
            # Tentative de conversion en entier
            essai = int(essai)

            if essai < 0:
                return "Veuillez entrer un nombre valide."

            self.tentative += 1

            if essai < self.nombre_a_deviner:
                return "Trop bas. Essayez à nouveau."
            elif essai > self.nombre_a_deviner:
                return "Trop haut. Essayez à nouveau."
            else:
                self.attribuer_niveau()
                return f"Bravo ! Vous avez deviné le juste prix en {self.tentative} tentatives. Niveau : {self.niveau}"

        except ValueError:
            # Si la conversion en entier échoue, vérifier s'il s'agit de "True" ou "False"
            if essai.lower() in ['true', 'false']:
                return "Veuillez entrer un nombre valide."
            else:
                return "Veuillez entrer un nombre valide."

    def attribuer_niveau(self):
        if self.tentative <= 5:
            self.niveau = "Expert"
        elif self.tentative <= 10:
            self.niveau = "Medium"
        else:
            self.niveau = "Nul"

    def get_niveau(self):
        return self.niveau

if __name__ == "__main__":
    jeu = JeuJustePrix()
    print("Bienvenue au Jeu du Juste Prix!")

    while True:
        essai = input("Devinez le nombre (entre 1 et 100, 'exit' pour quitter) : ")
        if essai.lower() == 'exit':
            break

        resultat = jeu.deviner(essai)
        print(resultat)

        if "Bravo" in resultat:
            break
