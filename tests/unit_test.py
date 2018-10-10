import unittest


class IrValidatorTests(unittest.TestCase):
    def setUp(self):
        self.card_number = "6104337856782725"
        self.incorrect_card_number = "610433785678275"
        self.iban_number = "IR062960000000100324200001"
        self.incorrect_iban_number = "IR062960000000100324200021"


if __name__ == "__main__":
    unittest.main()
