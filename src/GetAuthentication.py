#
# IMPORTS
#
# import configuration            
import requests
import webbrowser

from Keys import Keys


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
    accessToken = response.json()["access_token"]
    
    # return the authentication key
    return accessToken
# authenticate()


def main():
    """
    I get an authentication key from a consumer key
    """

    # Get keys
    keys = Keys()

    # If keys' file don't exist:
    if not keys.getKeys():

        # Ask for the consumer key
        keys.consumerKey = input("Enter the consumer key: ")

        # Authenticate it
        print("Authenticating consumer key")
        keys.accessToken = authenticate(keys.consumerKey)

        # Update the keys' file
        keys.saveKeys()

    # Print keys to user
    keys.printKeys()
# main()

if __name__ == '__main__':
    main()
else:
    raise "This script should be called as a single program"




