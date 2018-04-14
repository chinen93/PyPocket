#
# Documentation:
# PyPocket
# Python3 
#


#
# IMPORTS
#
import configuration
import requests


#
# CONSTANTS
#
HEADERS = {"content-type": "application/json; charset=UTF-8",
           "X-Accept": "application/json"}
URL_MODIFY = "https://getpocket.com/v3/send"
URL_RETRIEVE = "https://getpocket.com/v3/get"


#
# CODE
#
def getKeys():
    """
    I get the consumer and authentication keys from a file
    """
    
    try:
        # Open file to read
        fo = open(configuration.FILE, "r")
        line = fo.readline()
        
        # Close file
        fo.close()
        
    # Can not split keys
    except:
        print("Keys couldn't be found. Try creating them with GetAuthentication.py")
        exit

    # Remove special characters
    line = line.replace("\n", "")

    # Split keys
    keys = line.split(";")
    consumerKey = keys[0]
    authenticateKey = keys[1]

    # return keys
    return consumerKey, authenticateKey
# getKeys()


def getPockets(consumerKey, authenticateKey):
    """
    I retrieve the pockets saved
    """

    # Data to pass to server.
    data = {"consumer_key": consumerKey, 
            "access_token": authenticateKey}

    # try: Get the response from the server.
    try:
        response = requests.post(URL_RETRIEVE, headers=HEADERS, json=data)
    
    # Error: Print error message and leave.
    except:
        print("Problem to authenticate")
        exit

    print(response.text)
# getPockets()


def main():
    """
    I am the main function
    """
    consumerKey, authenticateKey = getKeys()
    getPockets(consumerKey, authenticateKey)
# main()


if __name__ == "__main__":
    main()
else:
    raise "This script should be called as a single program"


# PyPocket end
