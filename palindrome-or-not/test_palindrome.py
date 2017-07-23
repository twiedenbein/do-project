import unittest
from palindrome import palindrome_or_not

class TestPal(unittest.TestCase):
    def setUp(self):
        pass

    def test_true_phrases(self):
        self.assertTrue(palindrome_or_not("A Santa at Nasa."))
        self.assertTrue(palindrome_or_not("Are we not drawn onward to new era?"))
        self.assertTrue(palindrome_or_not("Lager, sir, is regal."))
        self.assertTrue(palindrome_or_not("Olson is in Oslo."))

    def test_false_phrases(self):
        self.assertFalse(palindrome_or_not("This is obviously not a palindrome, is it?"))

if __name__ == '__main__':
    unittest.main()
