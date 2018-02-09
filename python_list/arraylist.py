# coding = utf-8

from array_linked_list.arrays import Array
from abstractlist import AbstractList
from arraylistiterator import ArrayListIterator


class ArrayList(AbstractList):
    """
    An array-based list implementation.
    """
    DEFALUT_CAPACITY = 10

    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the contents of source_collection, if it's present.
        """
        self.items = Array(ArrayList.DEFALUT_CAPACITY)
        AbstractList.__init__(self, source_collection)

    def __iter__(self):
        """
        Supports iteration over a view of self.
        :return:
        """
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __getitem__(self, i):
        """
        Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexeError.
        :param i:
        :return:
        """
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self.items[i]

    def __setitem__(self, i, item):
        """
        Precondition: 0 <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError.
        :param i:
        :param item:
        :return:
        """
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self.items[i] = item

    def insert(self, i, item):
        """
        Inserts the item at position i.
        :param i:
        :param item:
        :return:
        """
        # Resize array here if necessary
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)
        if i < len(self):
            for j in range(len(self), i, -1):
                self.items[j] = self.items[j - 1]
        self.items[i] = item
        self.size += 1
        self.inc_mod_count()

    def pop(self, i=None):
        """
        Precondition: 0 <= i < len(self).Removes and returns th item at position i.
        If i is None, i is given a default of len(self) - 1.
        Raise: IndexError
        :param i:
        :return:
        """
        if i == None:
            i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        item = self.items[i]
        for j in range(i, len(self) - 1):
            self.items[j] = self.items[j + 1]
        self.size -= 1
        self.inc_mod_count()
        # Resize array here if necessary
        return item

    def list_iterator(self):
        """
        Returns a list iterator.
        :return:
        """
        return ArrayListIterator(self)
