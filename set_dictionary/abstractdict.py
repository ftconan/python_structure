# coding = utf-8

from inherit_abstract.abstractcollection import AbstractCollection


class AbstractDict(AbstractCollection):
    """
    Common data and method implementations for dictionaries.
    """
    def __init__(self, source_collection):
        """
        Will copy items to the collection from source_collection if it's present.
        """
        AbstractCollection.__init__(self)
        if source_collection:
            for key, value in source_collection:
                self[key] = value

    def __str__(self):
        return "{" + ", ".join(map(str, self.items())) + "}"

    def __and__(self, other):
        """
        Returns a new dictionary containing the contents of self adn other.
        :param other:
        :return:
        """
        result = type(self)(map(lambda item: (item.key, item.value), self.items()))
        for key in other:
            result[key] = other[key]
        return result

    def __eq__(self, other):
        """
        Returns True if self equals other, or False otherwise.
        :param other:
        :return:
        """
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for key in self:
            if not key in other:
                return False
        return True

    def keys(self):
        """
        Returns a iterator on the keys in the dictionary.
        :return:
        """
        return iter(self)

    def values(self):
        """
        Reutrns an iterator on the values in the dictionary.
        :return:
        """
        return iter(map(lambda key: self[key], self))

    def items(self):
        """
        Returns an iterator on the items in the dictionary.
        :return:
        """
        return iter(map(lambda key: Item(key, self[key]), self))


class Item(object):
    """
    Represents a dictionary item. Supports comparisons by key.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other):
            return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other):
            return False
        return self.key <= other.key
