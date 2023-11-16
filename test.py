import unittest
from unittest.mock import patch
from script import JeuJustePrix

class TestJeuJustePrix(unittest.TestCase):

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

            if "Bravo" in resultat:
                break

        # L'assertion suivante est correcte pour le bon script
        self.assertTrue("Bravo" in resultat.strip(), "Le jeu n'a pas indiqué la victoire.")

if __name__ == '__main__':
    unittest.main()