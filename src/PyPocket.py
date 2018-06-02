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
from ModifyParam import ModifyParam


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

    # Error: Couldn't get response, exit.
    except:
        print("Problem to authenticate")
        exit()

    # try: Get the list of itens from pocket.
    try:
        print(response.json()['since'])
        pocket_items = response.json()['list']

    # Error: Couldn't get data from server response, exit.
    except:
        print(response)
        print("Problem with retrieved data")
        exit()

    # Create a list with only the things that are needed.
    items = []

    # Foreach item from pocket items.
    for pocket_item in pocket_items:

        # Get the item.
        details = pocket_items[pocket_item]

        # Create Pocket Item.
        pocketItem = PocketItem(details)

        # Put the item with only the needed descriptions on the return list.
        items.append(pocketItem)

    return items
# getJsonPockets()



def removeTagFromItem(keys, items):
    """
    I remove a tag from the item
    """
    
    # Create post data and put the keys to access the API.
    data = {}
    data["consumer_key"] = keys.consumerKey
    data["access_token"] = keys.accessToken

    # Create parameter manager.
    modifyParam = ModifyParam()

    # Add action to remove tag.
    for item in items:
        modifyParam.tags_remove(item, Configuration.RET_PARAM_TAG)

    # Put actions into the post data.
    data["actions"] = modifyParam.actions

    # print(data)

    # try: Get the response from the server.
    try:
        response = requests.post(URL_MODIFY, headers=HEADERS, json=data)

    # Error: Couldn't get response, exit.
    except:
        print("Problem to remove tags")
        exit()

    # Exit normaly.
    print("Items were updated")
    
# removeTagFromItem()



def main():
    """
    I am the main function
    """

    # Get keys
    keys = Keys()

    # If keys' file don't exist: abort program.
    if not keys.getKeys():
        print("Keys couldn't be loaded!")
        exit()

    # Parameters for retrieving itens from pocket.
    retrieveParam = RetrieveParam()
    data = retrieveParam.data()

    # Get items from Pocket API.
    items = getJsonPockets(keys, data)
    
    # Save each item to the file.
    for item in items:
        item.saveToFile(Configuration.FILENAME_TO_SAVE)

    # Use the Pocket API to remove the retrieve tag.
    removeTagFromItem(keys, items)

    # print(items)
# main()


if __name__ == "__main__":
    main()
else:
    raise "This script should be called as a single program"


# PyPocket end
