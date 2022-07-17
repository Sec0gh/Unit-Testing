from isPositiveFunc import is_positive  
import unittest

# Inherit functionality from the TestCase class located in the unit test module.
class test_positive_func(unittest.TestCase):
   def test_basic(self):
      test_case = 5
      expected = f"{test_case} is a positive number." 
      self.assertEqual(is_positive(test_case), expected)    
   
   def test_negative(self):
      test_case = -4
      expected = f"{test_case} is a negative number." 
      self.assertEqual(is_positive(test_case), expected)
      
   def test_zero(self):
      test_case = 0
      expected = "It is zero." 
      self.assertEqual(is_positive(test_case), expected)      
      
# Run the test. 
if __name__ == "__main__":
   unittest.main()
