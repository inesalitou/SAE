import unittest
import io
from unittest.mock import patch
from script import JeuJustePrix

class TestJeuJustePrix(unittest.TestCase):

    @patch('builtins.input', side_effect=['-5'])
    def test_jeu_juste_prix_nombre_negatif(self, mock_input):
        jeu = JeuJustePrix()
        
        # Capture la sortie standard pour vérifier le message d'erreur
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            try:
                essai = int(input())
            except ValueError:
                print("Veuillez entrer un nombre valide.")

            resultat = jeu.deviner(essai)
            print(resultat)

        self.assertTrue("Veuillez entrer un nombre valide." in mock_stdout.getvalue(), "Le jeu n'a pas indiqué une erreur pour un nombre négatif.")
        

    @patch('builtins.input', side_effect=['50', '75', '88', '90', '92', '91'])
    def test_jeu_juste_prix(self, mock_input):
        jeu = JeuJustePrix()
        for _ in range(6):
            try:
                essai = int(input())
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                # Si l'entrée n'est pas un nombre, on continue la boucle
                continue

            resultat = jeu.deviner(essai)
            print(resultat)

            # Si on détecte l'erreur, on arrête le test
            if "Veuillez entrer un nombre valide." in resultat:
                break

            if "Bravo" in resultat:
                self.assertTrue("Bravo" in resultat.strip(), "Le jeu n'a pas indiqué la victoire.")
                break

if __name__ == '__main__':
    unittest.main()
