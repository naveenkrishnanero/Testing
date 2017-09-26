import unittest
from prime import is_prime,print_next_prime


class PrimeTestCase(unittest.TestCase):
    """ Tests for primes.py """

    def test_is_five_prime(self):
        """ Is five sucessfully determined to be a prime?"""
        self.assertTrue(is_prime(5))

    def test_is_four_not_prime(self):
        """ Testing whether 4 is prime or not"""
        self.assertFalse(is_prime(4))

    def test_is_zero_prime(self):
        """Testing whether zero is a prime number or not"""
        self.assertFalse(is_prime(0))

    def test_is_negative_number_prime(self):
        """Testing whether a negative number is prime or not"""
        self.assertFalse(is_prime(-4))
        
if __name__ == "__main__":
    unittest.main()

