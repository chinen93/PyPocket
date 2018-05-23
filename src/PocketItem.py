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

        pocket_tags = details["word_count"]
        self.tags = []

        for tag in pocket_tags:
            self.tags.append(tag)
    # __init__()

# PocketItem
