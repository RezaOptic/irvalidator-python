from tests.unit_test import IrValidatorTests
from irvalidator import card_validate


class CardsTest(IrValidatorTests):
    def test_validate_card__return_is_valid(self):
        result = card_validate(self.card_number)
        self.assertEqual(result["is_valid"], True)
        self.assertEqual(result["name"], "بانک ملت")

    def test_validate_card_with_wrong_card_number_len__return_is_not_valid(self):
        result = card_validate(self.incorrect_card_number)
        self.assertEqual(result["is_valid"], False)

    def test_validate_card_with_wrong_card_number__return_is_not_valid(self):
        result = card_validate(self.incorrect_card_number)
        self.assertEqual(result["is_valid"], False)
