#
# Documentation:
# PyPocket
# Python3 
#


#
# IMPORTS
#
import Configuration
import requests

from Keys import Keys
from RetrieveParam import RetrieveParam
from PocketItem import PocketItem


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


def getJsonPockets(keys, data):
    """
    I retrieve the pockets saved
    """

    # Data to pass to server.
    data["consumer_key"] = keys.consumerKey
    data["access_token"] = keys.accessToken

    print(data)

    # try: Get the response from the server.
    try:
        response = requests.post(URL_RETRIEVE, headers=HEADERS, json=data)

    # Error: Print error message and leave.
    except:
        print("Problem to authenticate")
        exit

    # Get the list of itens from pocket
    pocket_items = response.json()['list']

    # Create a list with only the things that are needed
    items = []

    # Foreach item from pocket items
    for pocket_item in pocket_items:

        # Get the item
        details = pocket_items[pocket_item]

        # Create Pocket Item
        pocketItem = PocketItem(details)

        # Put the item with only the needed descriptions on the return list
        items.append(pocketItem)

    return items
# getJsonPockets()


def main():
    """
    I am the main function
    """

    # Get keys
    keys = Keys()

    # If keys' file don't exist: abort program
    if not keys.getKeys():
        print("Keys couldn't be loaded!")
        exit()

    # Parameters for retrieving itens from pocket
    retrieveParam = RetrieveParam()
    data = retrieveParam.data()

    items = getJsonPockets(keys, data)

    print(items)
# main()


if __name__ == "__main__":
    main()
else:
    raise "This script should be called as a single program"


# PyPocket end
