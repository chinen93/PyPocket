#
# IMPORTS
#


#
# CONSTANTS
#


#
# CODE
#
class ModifyParam:
    """
    A class to manage parameters to modify pockets
    """

    def __init__(self):
        """
        Create a new parameters manager
        """
        self.actions = []
    #__init__()


    def _createAction(self, item, actionString):
        """
        I create a generic action
        """
        action = {
            "action": actionString,
            "item_id": item.item_id
        }
        self.actions.append(action)
    # _createAction()


    def _createTagAction(self, item, actionString, tags):
        """
        I create a generic tag action
        """
        action = {
            "action": actionString,
            "tags": tags,
            "item_id": item.item_id
        }
        self.actions.append(action)
    # _createTagAction()


    def archive(self, item):
        """
        I create an archive action
        """
        self._createAction(item, "archive")
    # archive()


    def delete(self, item):
        """
        I create a delete action
        """
        self._createAction(item, "delete")
    # delete()


    def favorite(self, item):
        """
        I create a favorite action
        """
        self._createAction(item, "archive")
    # favorite()


    def readd(self, item):
        """
        I create a readd action
        """
        self._createAction(item, "readd")
    # readd()


    def unfavorite(self, item):
        """
        I create an unfavorite action
        """
        self._createAction(item, "unfavorite")
    # unfavorite()


    def tags_add(self, item, tags):
        """
        I create a tags_add action
        """
        self._createTagAction(item, "tags_add", tags)
    # tags_add()


    def tags_clear(self, item, tags):
        """
        I create a tags_clear action
        """
        self._createTagAction(item, "tags_clear", tags)
    # tags_clear()


    def tags_remove(self, item, tags):
        """
        I create a tags_remove action
        """
        self._createTagAction(item, "tags_remove", tags)
    # tags_remove()


    def tags_rename(self, item, tags):
        """
        I create a tags_rename action
        """
        self._createTagAction(item, "tags_rename", tags)
    # tags_rename()


    def tags_replace(self, item, tags):
        """
        I create a tags_replace action
        """
        self._createTagAction(item, "tags_replace", tags)
    # tags_replace()

# ModifyParam
