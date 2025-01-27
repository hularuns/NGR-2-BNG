import unittest
from ngr_to_bng.converter import convert_ngr_to_bng
from ngr_to_bng.ngr_lookup import ngr_lookup
from ngr_to_bng.validation import NGRCodeError, NGRCoordLengthError

class TestValidation(unittest.TestCase):
        
    def test_convert_six_digit(self):
        result = convert_ngr_to_bng("SP158749")
        self.assertEqual(result, (415800, 274900))
    
    def test_convert_seven_digit(self): 
        self.assertRaises(NGRCoordLengthError, convert_ngr_to_bng, "SP1587493")
        
    def test_convert_invalid_string(self): 
        self.assertRaises(TypeError, convert_ngr_to_bng, "SP158a93")
        
    def test_convert_spaces_valid_string(self):
        result = convert_ngr_to_bng("TA 06545 408 02 ")
        self.assertEqual(result, (506545 , 440802))

if __name__ == "__main__":
    unittest.main()