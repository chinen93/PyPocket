#
# IMPORTS
#


#
# CONSTANTS
#


#
# CODE
#
class PocketItem:

    def __init__(self, details):
        """
        I initialize a pocket item
        """
        self.authors        = details["authors"]
        self.excerpt        = details["excerpt"]
        self.favorite       = details["favorite"]
        self.given_title    = details["given_title"]
        self.given_url      = details["given_url"]
        self.has_image      = details["has_image"]
        self.has_video      = details["has_video"]
        self.images         = details["images"]
        self.is_article     = details["is_article"]
        self.item_id        = details["item_id"]
        self.resolved_id    = details["resolved_id"]
        self.resolved_title = details["resolved_title"]
        self.resolved_url   = details["resolved_url"]
        self.status         = details["status"]
        self.videos         = details["videos"]
        self.word_count     = details["word_count"]

        pocket_tags = details["tags"]
        self.tags = []

        for tag in pocket_tags:
            self.tags.append(tag)
    # __init__()

    
    def toString(self):
        """
        I return a string to be inserted into a file
        """
    
        pattern = "* {}\n  [[{}]]"
        string = pattern.format(self.resolved_title, self.resolved_url)

        return string
    # toString()


    def saveToFile(self, filename):
        """
        I append myself to a file
        """
        with open("filename", "a") as f:
            f.write(self.toString())
    # saveToFile()

# PocketItem
