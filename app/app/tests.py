from django.test import TestCase
from .calc import add, subtract, mult

# docker-compose run --rm app sh -c "python manage.py test"
# docker-compose build
# docker-compose run --rm app sh -c "python manage.py test && flake8"
# main command:
# docker-compose run app sh -c "python manage.py ... "


class CalcTest(TestCase):
    """Testing the calculation"""

    def test_add_numbers(self):
        """Testing adding numbers"""
        return self.assertEqual(add(3, 8), 11)

    def test_sub_numbers(self):
        """Testing subtracting numbers"""
        return self.assertEqual(subtract(7, 15), 8)

    def test_mult_numbers(self):
        """Testing numbers multiplication"""
        return self.assertEqual(mult(6, 4), 24)
