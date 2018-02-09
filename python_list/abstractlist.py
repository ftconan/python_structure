# coding = utf-8

from inherit_abstract.abstractcollection import AbstractCollection


class AbstractList(AbstractCollection):
    """
    An abstract list implementation.
    """
    def __init__(self, source_collection=None):
        """
        Maintains a count of modifications t th list.
        """
        self.mod_count = 0
        AbstractCollection.__init__(self, source_collection)

    def get_mod_count(self):
        """
        Returns teh count of modifications to the list.
        :return:
        """
        return self.mod_count

    def inc_mod_count(self):
        """
        Increments the count of modifications to the list.
        :return:
        """
        self.mod_count += 1

    def index(self, item):
        """
        Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list.
        :param item:
        :return:
        """
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError(str(item) + " not in list.")

    def add(self, item):
        """
        Adds the item to the end fo the list.
        :return:
        """
        self.insert(len(self), item)

    def remove(self, item):
        """
        Precondition: item is in self.
        Raises: ValueError if item not in self.
        Postcondition: item is removed from self.
        :param item:
        :return:
        """
        position = self.index(item)
        self.pop(position)
