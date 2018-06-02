# https://docs.python.org/3/library/unittest.html#assert-methods
########################################################################

#
# IMPORTS
#
import sys
sys.path.append('../src/')

import unittest
from ModifyParam import ModifyParam
from PocketItem import PocketItem

#
# CONSTANTS
#


#
# CODE
#

class unitTestClass(unittest.TestCase):

    def setUp(self):
        """Set up things for every test"""
        self.mp = ModifyParam()
    # setUp()


    def tearDown(self):
        """Tear Down things for every test"""
        pass
    # tearDown()


    def testShouldCreateAction(self):
        """Should create an action"""

        details = {
            "item_id": 1
        }
        pi = PocketItem(details)

        self.assertEqual(len(self.mp.actions), 0)

        self.mp._createAction(pi, "test")

        self.assertEqual(len(self.mp.actions), 1)
        self.assertEqual(self.mp.actions[0]["action"], "test")
        self.assertEqual(self.mp.actions[0]["item_id"], pi.item_id)
    # testShouldCreateAction()


    def testShouldCreateTagAction(self):
        """Should create a tag action"""

        details = {
            "item_id": 1,
            "tags": ("test", "test1")
        }
        pi = PocketItem(details)

        self.assertEqual(len(self.mp.actions), 0)

        self.mp._createTagAction(pi, "test")

        self.assertEqual(len(self.mp.actions), 1)
        self.assertEqual(self.mp.actions[0]["action"], "test")
        self.assertEqual(self.mp.actions[0]["item_id"], pi.item_id)

        for tag in details["tags"]:
            self.assertTrue(tag in self.mp.actions[0]["tags"])
    # testShouldCreateTagAction()

# unitTestClass
