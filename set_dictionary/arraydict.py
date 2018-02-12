# coding = utf-8

from abstractdict import AbstractDict, Item


class ArrayDict(AbstractDict):
    """
    Represents an array-based dictionary.
    """
    def __init__(self, source_collection):
        """
        Will copy items to the collection from source_collection if it's present.
        :param source_collection:
        """
        self.items = list()
        AbstractDict.__init__(self, source_collection)

    def __iter__(self):
        """
        Serves up the keys in the dictionary.
        :return:
        """
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor].key
            cursor += 1

    def __getitem__(self, key):
        """
        Precondition: the is in the dictionary.
        Raises: a KeyError if th key is not in the dictionary.
        Returns the value associated with the key.
        :param key:
        :return:
        """
        index = self.index(key)
        if index == -1:
            raise KeyError("Missing:" + str(key))
        return self.items[index].value

    def __setitem__(self, key, value):
        """
        If the key is not in the dictionary, adds the key and value to it.
        Otherwise, replaces the old value with the new value.
        :param key:
        :param value:
        :return:
        """
        index = self.index(key)
        if index == -1:
            self.items.append(self(key, value))
            self.size += 1
        else:
            self.items[index].value = value

    def pop(self, key):
        """
        Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Removes the key and returns the associated or returns the default value otherwise.
        :param key:
        :return:
        """
        index = self.index(key)
        if index == -1:
            raise KeyError("Missing: " + str(key))
        self.size -= 1
        return self.items.pop(index).value

    def index(self, key):
        """
        Helper method for key search
        :param key:
        :return:
        """
        index = 0
        for entry in self.items:
            if entry.key == key:
                return index
            index += 1
        return -1
