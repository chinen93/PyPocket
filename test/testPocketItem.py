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
        details = {}
        details["authors"]        = None
        details["excerpt"]        = None
        details["favorite"]       = None
        details["given_title"]    = None
        details["given_url"]      = None
        details["has_image"]      = None
        details["has_video"]      = None
        details["images"]         = None
        details["is_article"]     = None
        details["item_id"]        = None
        details["resolved_id"]    = None
        details["resolved_title"] = "TEST TITLE"
        details["resolved_url"]   = "TEST URL"
        details["status"]         = None
        details["videos"]         = None
        details["word_count"]     = None
        details["tags"]           = []

        self.pocket = PocketItem(details)
    # setUp()


    def tearDown(self):
        """Tear Down things for every test"""
        pass
    # tearDown()
    

    def testToString(self):
        """Should return a string to be inserted into a file"""

        string = self.pocket.toString()
        
        self.assertEqual(string, "* TEST TITLE\n  [[TEST URL]]")
    # testToString()
    
# unitPocketItem
