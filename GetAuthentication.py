#
# IMPORTS
#
import requests

from os.path import expanduser

#
# CONSTANTS
#
CONSUMER_KEY = ""
FILENAME = "pocketKeys.txt"
HEADERS = {"content-type": "application/json; charset=UTF-8",
           "X-Accept": "application/json"}
HOME = expanduser("~/")
REDIRECT_URL = "https://www.google.com"
URL = "https://getpocket.com/v3/oauth/request"

#
# CODE
#
def authenticate(consumerKey):
    """
    I authenticate the consumer key
    """

    # Data to pass to server.
    data = {"consumer_key": consumerKey, 
            "redirect_uri": REDIRECT_URL}

    # try: Get the response from the server.
    try:
        response = requests.post(URL, headers=HEADERS, json=data)
    
    # Error: Print error message and leave.
    except:
        print("Problem to authenticate")
        exit
    
    # Save authentication key
    authentication_key = response.json()["code"]
    saveKeys(consumerKey, authentication_key)
# authenticate()



def getKeys():
    """
    I get the consumer and authentication keys from a file
    """
    
    try:
        # Open file to read
        fo = open(HOME + FILENAME, "r")
        line = fo.readline()
        
        # Close file
        fo.close()
        
    # Can not split keys
    except:
        consumerKey = input("Enter the consumer key: ")
        authenticateKey = None

    # Remove special characters
    line = line.replace("\n", "")

    # Split keys
    keys = line.split(";")
    consumerKey = keys[0]
    authenticateKey = keys[1]

    # return keys
    return consumerKey, authenticateKey
# getKeys()


def main():
    """
    I get an authentication key from a consumer key
    """

    # Get keys
    consumerKey, authenticateKey =  getKeys()

    # If authentication key does not exist: Authenticate consumer key
    if authenticateKey is None:
        print("Authenticating consumer key")

    # End program
    print(consumerKey, authenticateKey)
# main()


def saveKeys(consumerKey, authenticateKey):
    """
    I save the consumer and authentication key to a file
    """
    pass
# saveKeys()


if __name__ == '__main__':
    main()
else:
    raise "This script should be called as a single program"




