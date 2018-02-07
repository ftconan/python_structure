# coding = utf-8

from array_linked_list.arrays import Array
from inherit_abstract.abstractbag import AbstractBag


class ArrayBag(AbstractBag):
    """
    An array-based bag implementation.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the contents of source_collection,
        if it's present.
        """
        # self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        # self.size = 0
        # if source_collection:
        #     for item in source_collection:
        #         self.add(item)
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        AbstractBag.__init__(self, source_collection)

    def __str__(self):
        """
        Returns the number of items in self.
        :return:
        """
        return '{' + ', '.join(map(str, self)) + '}'

    def __iter__(self):
        """
        Supports iterations over a view of self.
        :return:
        """
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    # def __add__(self, other):
    #     """
    #     Returns a new bag containing the contents or self and other
    #     :param other:
    #     :return:
    #     """
    #     result = ArrayBag(self)
    #     for item in other:
    #         result.add(item)
    #     return result

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
        for item in self:
            if item not in other:
                return False
        return True

    def clear(self):
        """
        Makes self become empty.
        :return:
        """
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """
        Adds item to self
        :param item:
        :return:
        """
        self.items[len(self)] = item
        self.size += 1

    def remove(self, item):
        """
        Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self.
        :return:
        """
        # Check precondition adn raise if necessary
        if item not in self:
            raise KeyError(str(item) + 'not in bag')
        # Search for index of target item
        target_index = 0
        for target_item in self:
            if target_item == item:
                break
            target_index += 1

        # Shift items to the left of target up by one position
        for i in range(target_index, len(self) - 1):
            self.items[i] = self.items[i + 1]
        # Decrement logical size
        self.size -= 1
