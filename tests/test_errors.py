"""
    tests.tests_errors
    ~~~~~~~~~~~~~~~~~~

"""


from json.schema import load
from json.schema.exceptions import ValidationError
from . import TestCase, fixture


class TestErrors(TestCase):

    def test_check(self):
        validator = load(fixture('five.schema.json'))

        try:
            validator.validate({
                'creditcard': {
                    'provider': 'visa'
                }
            })
        except ValidationError as error:
            pass
        else:
            self.fail("shouldn't happen")

        try:
            validator.validate({
                'creditcard': {
                    'provider': 'mastercard',
                    'securitycode': 123
                }
            })
        except ValidationError as error:
            pass
        else:
            self.fail("shouldn't happen")
