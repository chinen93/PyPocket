#
# IMPORTS
#
from os.path import expanduser

#
# CONSTANTS
#

# Where to get and save the keys to be used on this script
HOME = expanduser("~/")

FILE_TO_SAVE = "pocketItems.org"
FILENAME_TO_SAVE = HOME + FILE_TO_SAVE

FILE = "pocketKeys.txt"
FILENAME = HOME + FILE

# Retrieve params
RET_PARAM_CONTENT_TYPE = None
RET_PARAM_COUNT        = None
RET_PARAM_DETAIL_TYPE  = None
RET_PARAM_FAVORITE     = None
RET_PARAM_SEARCH       = None
RET_PARAM_SORT         = None
RET_PARAM_STATE        = "all"
RET_PARAM_TAG          = "export emacs"
RET_PARAM_SINCE        = None
#
# CODE
#


