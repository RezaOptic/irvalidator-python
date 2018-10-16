from tests.unit_test import IrValidatorTests
from irvalidator import mobile_no_validator


class MobileNoTest(IrValidatorTests):
    def test_validate_mobile_no__return_is_valid(self):
        result = mobile_no_validator("ir", self.mobile_no)
        self.assertEqual(result, True)

    def test_validate_mobile_no__return_is_invalid(self):
        result = mobile_no_validator("ir", self.incorrect_mobile_no)
        self.assertEqual(result, False)
