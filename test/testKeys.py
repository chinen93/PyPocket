#
# IMPORTS
#
import sys
sys.path.append('../src/')

import unittest

import Configuration
from Keys import Keys

#
# CONSTANTS
#


#
# CODE
#

class testKeys(unittest.TestCase):
    
    def testShouldGetKeys(self):
        """Should get keys from file"""

        keys = Keys()
        self.assertEqual(keys.consumerKey, None)
        self.assertEqual(keys.accessToken, None)
        
        Configuration.FILE = "TEST_KEYS_EXIST"
        keys.getKeys()

        # done?
        self.assertEqual(keys.consumerKey, "12345")
        self.assertEqual(keys.accessToken, "12345")
    # testShouldGetKeys()
    
# testKeys
