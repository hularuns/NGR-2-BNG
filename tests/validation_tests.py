import unittest
from ngr_to_bng.validation import validate_ngr_input, NGRCodeError, NGRCoordLengthError

class TestValidation(unittest.TestCase):
    def test_valid_ngr_input(self):
        result = validate_ngr_input("SP123456")
        self.assertEqual(result, True)
    
    def test_invalid_prefix(self):
        self.assertRaises(NGRCodeError, validate_ngr_input, "XX1234")
    
    def test_invalid_length(self):
        self.assertRaises(NGRCoordLengthError, validate_ngr_input, "SP123")
    
    def test_invalid_chars(self):
        self.assertRaises(TypeError, validate_ngr_input, "SP1234567x")
        

if __name__ == "__main__":
    unittest.main()