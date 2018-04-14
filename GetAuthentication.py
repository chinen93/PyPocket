#
# IMPORTS
#
import configuration
import requests
import webbrowser


#
# CONSTANTS
#
CONSUMER_KEY = ""
HEADERS = {"content-type": "application/json; charset=UTF-8",
           "X-Accept": "application/json"}
REDIRECT_URL = "https://www.google.com"
URL_AUTHORIZE = "https://getpocket.com/v3/oauth/authorize"
URL_REQUEST = "https://getpocket.com/v3/oauth/request"
URL_LOGIN =  "https://getpocket.com/auth/authorize"

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
        response = requests.post(URL_REQUEST, headers=HEADERS, json=data)
    
    # Error: Print error message and leave.
    except:
        print("Problem to Request")
        exit
    
    # Get request token
    request_token = response.json()["code"]

    # Create the url to authorize the pocket account
    url = URL_LOGIN
    url += "?request_token=" + request_token
    url += "&redirect_uri=" + REDIRECT_URL

    # Open the URL in the browser
    webbrowser.open(url)

    # Get the request token from the callback
    request_token_callback = response.json()["code"]

    # Data with consumer key and request token
    data = {"consumer_key": consumerKey,
            "code": request_token_callback}

    # try: Convert the request token into a pocket access token
    try:
        response = requests.post(URL_AUTHORIZE, headers=HEADERS, json=data)
    
    # Error: Print error message and leave.
    except:
        print("Problem to Authorize")
        exit
    
    # Get authentication key
    authenticationKey = response.json()["access_token"]

    # Save it into a file
    saveKeys(consumerKey, authenticationKey)
    
    # return the authentication key
    return authenticationKey
# authenticate()



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

        # Remove special characters
        line = line.replace("\n", "")
        
        # Split keys
        keys = line.split(";")
        consumerKey = keys[0]
        authenticateKey = keys[1]
        
    # Can not split keys
    except:
        consumerKey = input("Enter the consumer key: ")
        authenticateKey = None

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
        authenticateKey = authenticate(consumerKey)

    # End program
    print(consumerKey, authenticateKey)
# main()


def saveKeys(consumerKey, authenticateKey):
    """
    I save the consumer and authentication key to a file
    """

    success = True

    try:
        # Open file to read
        fo = open(configuration.FILE, "w")
        fo.write(consumerKey)
        fo.write(";")
        fo.write(authenticateKey)

        # Close file
        fo.close()
        
    # Can not write
    except:
        success = False

    return success

# saveKeys()


if __name__ == '__main__':
    main()
else:
    raise "This script should be called as a single program"




