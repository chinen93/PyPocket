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
        self.contentType = Configuration.RETRIEVE_PARAM_CONTENT_TYPE
        self.count = Configuration.RETRIEVE_PARAM_COUNT
        self.detailType = Configuration.RETRIEVE_PARAM_DETAIL_TYPE
        self.favorite = Configuration.RETRIEVE_PARAM_FAVORITE
        self.search = Configuration.RETRIEVE_PARAM_SEARCH
        self.sort = Configuration.RETRIEVE_PARAM_SORT
        self.state = Configuration.RETRIEVE_PARAM_STATE
        self.tag = Configuration.RETRIEVE_PARAM_TAG
        self.since = Configuration.RETRIEVE_PARAM_SINCE
    # __init__()


    def data(self):
        """
        I return a dict with all parameters to pass to the API
        """
        param = vars(self)
        keys = param.keys()

        for key in keys:
            if param[key] is None:
                param.pop(key)
        
        return param
        
    # data()


# RetrieveParam
