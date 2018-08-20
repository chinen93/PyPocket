#
# IMPORTS
#
import Configuration

#
# CONSTANTS
#


#
# CODE
#

class RetrieveParam:
    """
    A class to manage parameters to retrieve pockets
    """

    def __init__(self):
        """
        Create a new parameters manager
        """
        self.contentType = Configuration.RET_PARAM_CONTENT_TYPE
        self.count       = Configuration.RET_PARAM_COUNT
        self.detailType  = Configuration.RET_PARAM_DETAIL_TYPE
        self.favorite    = Configuration.RET_PARAM_FAVORITE
        self.search      = Configuration.RET_PARAM_SEARCH
        self.sort        = Configuration.RET_PARAM_SORT
        self.state       = Configuration.RET_PARAM_STATE
        self.tag         = Configuration.RET_PARAM_TAG
        self.since       = Configuration.RET_PARAM_SINCE
    # __init__()


    def data(self):
        """
        I return a dict with all parameters to pass to the API
        """
        data = {}
        param = vars(self)
        keys = param.keys()

        for key in keys:
            if param[key] is not None:
                data[key] = param[key]

        return data
    # data()


# RetrieveParam
