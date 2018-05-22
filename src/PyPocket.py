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


def getJsonPockets(consumerKey, authenticateKey, param):
    """
    I retrieve the pockets saved
    """

    # Data to pass to server.
    data = {"consumer_key": consumerKey,
            "access_token": authenticateKey}

    # Add parameters 
    if(param["contentType"]):
        data["contentType"] = param["contentType"]
    if(param["count"]):
        data["count"] = param["count"]
    if(param["detailType"]):
        data["detailType"] = param["detailType"]
    if(param["favorite"]):
        data["favorite"] = param["favorite"]
    if(param["state"]):
        data["state"] = param["state"]
    if(param["sort"]):
        data["sort"] = param["sort"]
    if(param["search"]):
        data["search"] = param["search"]
    if(param["tag"]):
        data["tag"] = param["tag"]

    if(param["since"]):
        data["since"] = param["since"]

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
        item = {}

        # Try to get descriptions of each item
        try:
            # Put only the descriptions that are relevant
            # item["authors"] = details["authors"]
            # item["excerpt"] = details["excerpt"]
            # item["favorite"] = details["favorite"]
            item["given_title"] = details['given_title']
            # item["given_url"] = details["given_url"]
            # item["has_image"] = details["has_image"]
            # item["has_video"] = details["has_video"]
            # item["images"] = details["images"]
            # item["is_article"] = details["is_article"]
            item["item_id"] = details["item_id"]
            # item["resolved_id"] = details["resolved_id"]
            item["resolved_title"] = details['resolved_title']
            item["resolved_url"] = details['resolved_url']
            # item["status"] = details["status"]
            # item["videos"] = details["videos"]
            # item["word_count"] = details["word_count"]
            pocket_tags = details['tags']

        except KeyError:
            pass

        # Separate the tags into a list
        item["tags"] = []
        for tag in pocket_tags:
            item["tags"].append(tag)


        # Put the item with only the needed descriptions on the return list
        items.append(item)

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
        exit


    # Parameters for retrieving itens from pocket
    # retrieveParam = {}
    # retrieveParam["contentType"] = None
    # retrieveParam["count"] = None
    # retrieveParam["detailType"] = "complete"
    # retrieveParam["favorite"] = None
    # retrieveParam["search"] = None
    # retrieveParam["sort"] = "title"
    # retrieveParam["state"] = Configuration.POCKET_STATE
    # retrieveParam["tag"] = Configuration.POCKET_TAG

    # retrieveParam["since"] = None

    retrieveParam = RetrieveParam()
    data = retrieveParam.data()

    print(data)

    items = getJsonPockets(keys.consumerKey,
                           keys.accessToken,
                           data)

    print(items)
# main()


if __name__ == "__main__":
    main()
else:
    raise "This script should be called as a single program"


# PyPocket end
