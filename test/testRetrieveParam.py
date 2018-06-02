#
# IMPORTS
#
import sys
sys.path.append('../src/')

import unittest

import Configuration
from RetrieveParam import RetrieveParam

#
# CONSTANTS
#


#
# CODE
#

class testRetrieveParam(unittest.TestCase):

    def setUp(self):
        """Set up things for every test"""


    # setUp()

    def tearDown(self):
        """Tear Down things for every test"""
        pass
    # tearDown()


    def testNoData(self):
        """Should return nothing"""

        Configuration.RET_PARAM_CONTENT_TYPE = None
        Configuration.RET_PARAM_COUNT        = None
        Configuration.RET_PARAM_DETAIL_TYPE  = None
        Configuration.RET_PARAM_FAVORITE     = None
        Configuration.RET_PARAM_SEARCH       = None
        Configuration.RET_PARAM_SORT         = None
        Configuration.RET_PARAM_STATE        = None
        Configuration.RET_PARAM_TAG          = None
        Configuration.RET_PARAM_SINCE        = None

        rp = RetrieveParam()

        ret = rp.data()
        self.assertEqual(ret, {})
    # testNoData()


    def testData(self):
        """Should return some data"""

        Configuration.RET_PARAM_CONTENT_TYPE = 1
        Configuration.RET_PARAM_COUNT        = 2
        Configuration.RET_PARAM_DETAIL_TYPE  = None
        Configuration.RET_PARAM_FAVORITE     = None
        Configuration.RET_PARAM_SEARCH       = None
        Configuration.RET_PARAM_SORT         = None
        Configuration.RET_PARAM_STATE        = None
        Configuration.RET_PARAM_TAG          = None
        Configuration.RET_PARAM_SINCE        = None

        rp = RetrieveParam()

        ret = rp.data()

        self.assertEqual(len(ret)           , 2)
        self.assertEqual(ret["contentType"] , 1)
        self.assertEqual(ret["count"]       , 2)
    # testData()

# testRetrieveParam
