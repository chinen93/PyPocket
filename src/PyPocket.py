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
import logging

from Keys import Keys
from RetrieveParam import RetrieveParam
from PocketItem import PocketItem
from ModifyParam import ModifyParam

import sys
from getopt import getopt

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
    pocketLogger.debug("Retrieve Params: ")
    pocketLogger.debug(data)

    # try: Get the response from the server.
    try:
        response = requests.post(URL_RETRIEVE, headers=HEADERS, json=data)

    # Error: Couldn't get response, exit.
    except:
        pocketLogger.error("Problem to authenticate")
        exit()

    # try: Get the list of itens from pocket.
    try:
        pocketLogger.debug("Since")
        pocketLogger.debug(response.json()['since'])

        pocket_items = response.json()['list']
        pocketLogger.debug("Response JSON")
        pocketLogger.debug(pocket_items)

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

    info = "{} items were retrieved"
    pocketLogger.info(info.format(len(items)))
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
    info = "Items updated. Tag '{}' was removed from every item"
    pocketLogger.info(info.format(Configuration.RET_PARAM_TAG))

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
    pocketLogger.debug(data)

    # Get items from Pocket API.
    items = getJsonPockets(keys, data)

    # If there's no itens to be saved exit
    if len(items) == 0:
        pocketLogger.info("No itens to be saved")
        exit()

    # Save each item to the file.
    if Configuration.SAVE_ITENS:
        info = "File to Save: {}"
        pocketLogger.info(info.format(Configuration.FILENAME_TO_SAVE))
        for item in items:
            item.saveToFile(Configuration.FILENAME_TO_SAVE)

    # Use the Pocket API to remove the retrieve tag.
    if Configuration.REMOVE_TAG:
        removeTagFromItem(keys, items)

    # log items
    for item in items:
        pocketLogger.debug("Info item: " + item.toString())

# main()


def parseArgs():
    """
    I parse Args from the console with getopt and update the state
    """

    shortopts = "vo:t:r"
    longopts = ["verbose", "version", "output=",
                "tagSearch=", "removeTag", "doNotSave", "debug"]

    options, remains = getopt(sys.argv[1:], shortopts, longopts)

    for opt, answer in options:
        if opt in ("-v", "--verbose"):
            pocketLogger.setLevel(logging.INFO)

        if opt in ("--debug"):
            pocketLogger.setLevel(logging.DEBUG)

        if opt in ("--version"):
            pocketLogger.setLevel(logging.INFO)
            pocketLogger.info(Configuration.VERSION)
            exit()

        if opt in ("--output"):
            Configuration.FILENAME_TO_SAVE = answer

        if opt in ("-t", "--tagSearch"):
            Configuration.RET_PARAM_TAG = answer

        if opt in ("-r", "--removeTag"):
            Configuration.REMOVE_TAG = True

        if opt in ("--doNotSave"):
            Configuration.SAVE_ITENS = False

# parseArgs()


if __name__ == "__main__":

    parseArgs()
    main()
else:
    raise "This script should be called as a single program"


# PyPocket end
