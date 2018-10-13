import unittest


class IrValidatorTests(unittest.TestCase):
    def setUp(self):
        self.card_number = "6104337856782725"
        self.incorrect_card_number = "610433785678275"
        self.iban_number = "IR062960000000100324200001"
        self.incorrect_iban_number = "IR062960000000100324200021"
        self.national_id_number = "0111848806"
        self.national_id_number_without_zero = "111848806"
        self.incorrect_national_id_number = "0938099806"
        self.incorrect_national_without_zero = "7731689951"


if __name__ == "__main__":
    unittest.main()
