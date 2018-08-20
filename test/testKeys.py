#
# IMPORTS
#
import sys
sys.path.append('../src/')

import unittest

import Configuration
from Keys import Keys
from random import randint

#
# CONSTANTS
#
FILE_SAVE_KEYS = "SAVE_KEYS"
FILE_WITH_VALID_KEYS = "VALID_KEYS"
FILE_WITH_INVALID_KEYS = "INVALID_KEYS"
FILE_WITH_NO_KEYS = "NO_KEYS"


#
# CODE
#

class testKeys(unittest.TestCase):

    def setUp(self):
        """Set up things for every test"""

        # Create key manager to test
        self.keys = Keys()

    # setUp()


    def tearDown(self):
        """Tear Down things for every test"""
        pass
    # tearDown()


    def testShouldCreateEmptyKeysManager(self):
        """Should create empty keys manager"""

        self.assertEqual(self.keys.consumerKey, None)
        self.assertEqual(self.keys.accessToken, None)
    # testShouldCreateEmptyKeysManager()


    def testShouldFailToGetKeysFromInvalidFile(self):
        """Should fail to get keys from invalid file"""

        # Change file where will get keys from
        Configuration.FILENAME = FILE_WITH_INVALID_KEYS

        # Get keys from this file
        self.keys.getKeys()

        # Assert things
        self.assertEqual(self.keys.consumerKey, None)
        self.assertEqual(self.keys.accessToken, None)
    # testShouldFailToGetKeysFromInvalidFile()


    def testShouldFailToGetKeysFromAnywhere(self):
        """Should fail to get keys from anywhere"""

        # Change file where will get keys from
        Configuration.FILENAME = FILE_WITH_NO_KEYS

        # Get keys from this file
        self.keys.getKeys()

        # Assert things
        self.assertEqual(self.keys.consumerKey, None)
        self.assertEqual(self.keys.accessToken, None)
    # testShouldFailToGetKeysFromAnywhere()


    def testShouldGetKeys(self):
        """Should get keys from file"""

        # Change file where will get keys from
        Configuration.FILENAME = FILE_WITH_VALID_KEYS
        
        # Get keys from this file
        self.keys.getKeys()

        # Assert things
        self.assertEqual(self.keys.consumerKey, "12345")
        self.assertEqual(self.keys.accessToken, "12345")
    # testShouldGetKeys()


    def testShouldSaveKeys(self):
        """Should save keys"""
        
        # Change file where will get keys from
        Configuration.FILENAME = FILE_SAVE_KEYS

        # Get keys from this file
        self.keys.getKeys()

        # Create random number to test and save it as keys
        keysToSave = randint(0,1000)

        # Assert that number chosen is different from stored key 
        self.assertNotEqual(self.keys.consumerKey, keysToSave)
        self.assertNotEqual(self.keys.accessToken, keysToSave)

        # Put random number into keys slots
        self.keys.consumerKey = keysToSave
        self.keys.accessToken = keysToSave

        # Save and retrieve keys from file
        self.keys.saveKeys()
        self.keys.getKeys()

        # Assert that keys is equal to the random number
        self.assertEqual(self.keys.consumerKey, str(keysToSave))
        self.assertEqual(self.keys.accessToken, str(keysToSave))
    # testShouldSaveKeys()

# testKeys
