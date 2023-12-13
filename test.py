import unittest
import io
from unittest.mock import patch
from script import JeuJustePrix

class TestJeuJustePrix(unittest.TestCase):

    @patch('builtins.input', side_effect=['-5'])
    def test_jeu_juste_prix_nombre_negatif(self, mock_input):
        jeu = JeuJustePrix()

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            try:
                essai = int(input())
            except ValueError:
                print("Veuillez entrer un nombre valide.")

            resultat = jeu.deviner(essai)
            print(resultat)

        self.assertTrue("Veuillez entrer un nombre valide." in mock_stdout.getvalue(), "Le jeu n'a pas indiqué une erreur pour un nombre négatif.")

    @patch('builtins.input', side_effect=[-5])  # Simule l'entrée d'un nombre négatif
    def test_jeu_juste_prix_nombre_negatif_patch(self, mock_input):
        jeu = JeuJustePrix()

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            essai = int(input())
            resultat = jeu.deviner(essai)
            print(resultat)

        self.assertTrue("Veuillez entrer un nombre valide." in mock_stdout.getvalue(), "Le jeu n'a pas indiqué une erreur pour un nombre négatif.")

    @patch('builtins.input', return_value='True')  # Simule l'entrée d'une chaîne contenant 'True'
    def test_jeu_juste_prix_boolean(self, mock_input):
        jeu = JeuJustePrix()

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            resultat = jeu.deviner(input())
            print(resultat)

        self.assertTrue("Veuillez entrer un nombre valide." in mock_stdout.getvalue(), "Le jeu n'a pas indiqué une erreur pour un booléen.")

    @patch('builtins.input', side_effect=['50', '75', '88', '90', '92', '91'])
    def test_jeu_juste_prix(self, mock_input):
        jeu = JeuJustePrix()
        for _ in range(6):
            try:
                essai = int(input())
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue

            resultat = jeu.deviner(essai)
            print(resultat)

            if "Veuillez entrer un nombre valide." in resultat:
                break

            if "Bravo" in resultat:
                self.assertTrue("Bravo" in resultat.strip(), "Le jeu n'a pas indiqué la victoire.")
                break

    @patch('builtins.input', side_effect=['50', '75', '88', '90', '92', '91'])
    def test_jeu_juste_prix_affichage_niveau(self, mock_input):
        jeu = JeuJustePrix()

        niveau_attendu = None

        for _ in range(6):
            try:
                essai = int(input())
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue

            resultat = jeu.deviner(essai)
            print(resultat)

            if "Veuillez entrer un nombre valide." in resultat:
                break

            if "Bravo" in resultat:
                niveau_attendu = jeu.get_niveau()
                self.assertIsNotNone(niveau_attendu, "Le niveau n'a pas été attribué.")
                print(f"Niveau attendu : {niveau_attendu}")

                # Capture la sortie standard pour vérifier si le niveau est affiché
                with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                    self.assertIn(f"Niveau : {niveau_attendu}", mock_stdout.getvalue(), "Le niveau du joueur n'a pas été affiché.")
                
                break

if __name__ == '__main__':
    unittest.main()
