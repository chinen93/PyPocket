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
        if "authors" in details:
            self.authors        = details["authors"]

        if "excerpt" in details:
            self.excerpt        = details["excerpt"]

        if "favorite" in details:
            self.favorite       = details["favorite"]

        if "given_title" in details:
            self.given_title    = details["given_title"]

        if "given_url" in details:
            self.given_url      = details["given_url"]

        if "has_image" in details:
            self.has_image      = details["has_image"]

        if "has_video" in details:
            self.has_video      = details["has_video"]

        if "images" in details:
            self.images         = details["images"]

        if "is_article" in details:
            self.is_article     = details["is_article"]

        if "item_id" in details:
            self.item_id        = details["item_id"]

        if "resolved_id" in details:
            self.resolved_id    = details["resolved_id"]

        if "resolved_title" in details:
            self.resolved_title = details["resolved_title"]

        if "resolved_url" in details:
            self.resolved_url   = details["resolved_url"]

        if "status" in details:
            self.status         = details["status"]

        if "videos" in details:
            self.videos         = details["videos"]

        if "word_count" in details:
            self.word_count     = details["word_count"]

        if "tags" in details:
            pocket_tags = details["tags"]
            self.tags = []

            for tag in pocket_tags:
                self.tags.append(tag)
    # __init__()


    def toString(self):
        """
        I return a string to be inserted into a file
        """

        pattern = "* {}\n  [[{}]]\n"
        string = pattern.format(self.resolved_title, self.resolved_url)

        return string
    # toString()


    def saveToFile(self, filename):
        """
        I append myself to a file
        """
        with open(filename, "a+") as f:
            f.write(self.toString())
    # saveToFile()

# PocketItem
