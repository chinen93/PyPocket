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
class Keys:
    """
    A class to manage keys
    """

    def __init__(self):
        """
        Create a new keys manager with the correct keys or None if
        them don't exist.
        """

        self.consumerKey = None
        self.accessToken = None
    # __init__()


    def hasKeys(self):
        """
        Check if the keys exist.

        :returns: True if the class has the keys to access the Pocket API.
        :rtype: Boolean
        """
        return self.accessToken != None
        
    # hasKeys()



    def getKeys(self):
        """
        I get the keys to access the Pocket API.

        :returns: True if got the keys, False otherwise.
        :rtype: Boolean
        """

        try:
            # Open file to read
            with open(Configuration.FILE, "r") as fo:
                line = fo.readline()

            # Remove special characters
            line = line.replace("\n", "")
        
            # Split keys
            keys = line.split(";")
            self.consumerKey = keys[0]
            self.accessToken = keys[1]
        
            # Can not split keys
        except:
            self.consumerKey = None
            self.accessToken = None

        # return whether it was successful or not
        return self.hasKeys()

    # getKeys()


    def printKeys(self):
        """
        I print the keys
        """
        print(self.consumerKey, self.accessToken)
    
    # printKeys()


    def saveKeys(self):
        """
        I save the keys to access the Pocket API.

        :returns: True if saved the keys, False otherwise.
        :rtype: Boolean
        """
        success = True

        try:
            # Open file to read
            with open(Configuration.FILE, "w") as fo:
                fo.write(self.consumerKey)
                fo.write(";")
                fo.write(self.authenticateKey)

        except:
            # Can not write
            success = False

        return success
    # saveKeys()

# class()
    

