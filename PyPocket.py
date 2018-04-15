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


def getJsonPockets(consumerKey, authenticateKey, tags = None, state = None):
    """
    I retrieve the pockets saved
    """

    # Data to pass to server.
    data = {"consumer_key": consumerKey, 
            "access_token": authenticateKey,
            "detailType": "complete",
            "sort":"title"}

    # If exist a tag of itens to be retrieve
    if(tags):
        data["tag"] = tags

    # Check the state of each 
    if(state):
        data["state"] = state

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
            item["item_id"] = details["item_id"]
            item["given_title"] = details['given_title']
            item["resolved_title"] = details['resolved_title']
            item["resolved_url"] = details['resolved_url']
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
    consumerKey, authenticateKey = getKeys()

    items = getJsonPockets(consumerKey, 
                           authenticateKey, 
                           configuration.POCKET_TAG, 
                           configuration.POCKET_STATE)
    
    print(items)
# main()


if __name__ == "__main__":
    main()
else:
    raise "This script should be called as a single program"


# PyPocket end
