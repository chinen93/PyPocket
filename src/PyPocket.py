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

from PocketLogger import pocketLogger

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

    pocketLogger.info(data)

    # try: Get the response from the server.
    try:
        response = requests.post(URL_RETRIEVE, headers=HEADERS, json=data)

    # Error: Couldn't get response, exit.
    except:
        pocketLogger.error("Problem to authenticate")
        exit()

    # try: Get the list of itens from pocket.
    try:
        pocketLogger.debug(response.json()['since'])
        pocket_items = response.json()['list']

    # Error: Couldn't get data from server response, exit.
    except:
        pocketLogger.debug(response)
        pocketLogger.error("Problem with retrieved data")
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
    pocketLogger.debug(data)

    # try: Get the response from the server.
    try:
        response = requests.post(URL_MODIFY, headers=HEADERS, json=data)

    # Error: Couldn't get response, exit.
    except:
        pocketLogger.error("Problem to remove tags")
        exit()

    # Exit normaly.
    pocketLogger.info("Items updated")
    
# removeTagFromItem()


def main():
    """
    I am the main function
    """

    # Get keys
    keys = Keys()

    # If keys' file don't exist: abort program.
    if not keys.getKeys():
        pocketLogger.info("Keys couldn't be loaded!")
        exit()

    # Parameters for retrieving itens from pocket.
    retrieveParam = RetrieveParam()
    data = retrieveParam.data()

    # Get items from Pocket API.
    items = getJsonPockets(keys, data)

    # If there's no itens to be saved exit
    if len(items) == 0:
        pocketLogger.info("No itens to be saved")
        exit()
    
    # Save each item to the file.
    for item in items:
        item.saveToFile(Configuration.FILENAME_TO_SAVE)

    # Use the Pocket API to remove the retrieve tag.
    removeTagFromItem(keys, items)

    # log items
    pocketLogger.debug(items)
# main()


if __name__ == "__main__":
    main()
else:
    raise "This script should be called as a single program"


# PyPocket end
