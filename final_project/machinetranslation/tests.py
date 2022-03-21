import unittest
from translator import english_to_french, french_to_english
class test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("How are you ?"), "Comment es-tu?")
        self.assertNotEqual(english_to_french("What are you?"), "Qui êtes-vous?")

class test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Comment es-tu?"), "How are you?")
        self.assertNotEqual(french_to_english("Qui êtes-vous?"), "What are you?")


unittest.main()