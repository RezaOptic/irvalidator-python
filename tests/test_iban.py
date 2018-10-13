from tests.unit_test import IrValidatorTests
from irvalidator import iban_validator


class IbanTest(IrValidatorTests):
    def test_validate_iban__return_is_valid(self):
        result = iban_validator(self.iban_number)
        self.assertEqual(result, True)

    def test_validate_iban__return_is_invalid(self):
        result = iban_validator(self.incorrect_iban_number)
        self.assertEqual(result, False)
