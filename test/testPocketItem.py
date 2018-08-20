# https://docs.python.org/3/library/unittest.html#assert-methods
########################################################################

#
# IMPORTS
#
import sys
sys.path.append('../src/')

import unittest

from PocketItem import PocketItem

#
# CONSTANTS
#


#
# CODE
#

class unitPocketItem(unittest.TestCase):

    def setUp(self):
        """Set up things for every test"""
        self.details = {}
        self.details["authors"]        = None
        self.details["excerpt"]        = None
        self.details["favorite"]       = None
        self.details["given_title"]    = None
        self.details["given_url"]      = None
        self.details["has_image"]      = None
        self.details["has_video"]      = None
        self.details["images"]         = None
        self.details["is_article"]     = None
        self.details["item_id"]        = None
        self.details["resolved_id"]    = None
        self.details["resolved_title"] = "TEST TITLE"
        self.details["resolved_url"]   = "TEST URL"
        self.details["status"]         = None
        self.details["videos"]         = None
        self.details["word_count"]     = None
        self.details["tags"]           = []
    # setUp()


    def tearDown(self):
        """Tear Down things for every test"""
        pass
    # tearDown()


    def testShouldToString(self):
        """Should return a string to be inserted into a file"""
        pocket = PocketItem(self.details)

        string = pocket.toString()

        self.assertEqual(string, "* TEST TITLE\n  [[TEST URL]]\n")
    # testShouldToString()


    def testShouldToStringWithTags(self):
        """Should return a string to be inserted into a file"""
        self.details["tags"] = ["TEST_TAGS1", "TEST_TAGS2"]
        pocket = PocketItem(self.details)

        string = pocket.toString()

        self.assertEqual(string, 
                         "* TEST TITLE :TEST_TAGS1:TEST_TAGS2:\n  [[TEST URL]]\n")
    # testShouldToStringWithTags()


    def testShouldToStringWithTagsWithSpaces(self):
        """Should return a string to be inserted into a file"""
        self.details["tags"] = ["TEST TAGS1", "TEST TAGS2"]
        pocket = PocketItem(self.details)

        string = pocket.toString()

        self.assertEqual(string, 
                         "* TEST TITLE :TEST_TAGS1:TEST_TAGS2:\n  [[TEST URL]]\n")
    # testShouldToStringWithTagsWithSpaces()


    def testShouldCreateItemEvenWithNotAllParameters(self):
        """Should create item even with not all parameters"""

        del(self.details["resolved_title"])
        pocket = PocketItem(self.details)

        self.assertIsInstance(pocket, PocketItem)
    # testShouldCreateItemEvenWithNotAllParameters()


# unitPocketItem
