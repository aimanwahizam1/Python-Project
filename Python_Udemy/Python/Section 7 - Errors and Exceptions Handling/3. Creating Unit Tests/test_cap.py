# ---------------------------------------------------------------------------- #
#                                 Unit Testing                                 #
# ---------------------------------------------------------------------------- #

# Here we will test the function in cap.py

# NOTE: Test the simple things first then complex

# NOTE: Need to import unittest and the script to be tested
import unittest
import cap

# Create a test class
# Inherit from unittest.TestCase
class TestCap(unittest.TestCase):

    # First instance of testing (simple)
    def test_one_word(self):
        text = "python"
        # Call the imported function to test
        result = cap.cap_text(text)
        # Test by checking if func output is EQUAL TO "Python"
        self.assertEqual(result, "Python")

    # Another test
    def test_multiple_words(self):
        text = "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result, "Monty Python")

if __name__ == "__main__":
    unittest.main()