from tests.unit_test import IrValidatorTests
from irvalidator import national_id_validator


class NationalIdTest(IrValidatorTests):
    def test_validate_national_id__return_is_valid(self):
        result = national_id_validator(self.national_id_number)
        self.assertEqual(result, True)

    def test_validate_national_id__return_is_invalid(self):
        result = national_id_validator(self.incorrect_national_id_number)
        self.assertEqual(result, False)

    def test_validate_national_id_without_zero__return_is_valid(self):
        result = national_id_validator(self.national_id_number_without_zero)
        self.assertEqual(result, True)

    def test_validate_national_id_without_zero__return_is_invalid(self):
        result = national_id_validator(self.incorrect_national_without_zero)
        self.assertEqual(result, True)
