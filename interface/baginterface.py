# coding = utf-8


class BagInterface(object):
    """
    Interface for all bag types.
    """
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the contents of source_collection,
        if it's present.
        """
        pass

    def is_empty(self):
        """
        Returns True if len(self) == 0,or False otherwise.
        :return:
        """
        return True

    def __len__(self):
        """
        Returns the number of items in self.
        :return:
        """
        return 0

    def __str__(self):
        """
        Returns the number of items in self.
        :return:
        """
        return ''

    def __iter__(self):
        """
        Supports iterations over a view of self.
        :return:
        """
        return None

    def __add__(self, other):
        """
        Returns a new bag containing the contents or self and other
        :param other:
        :return:
        """
        return None

    def __eq__(self, other):
        """
        Returns True if self equals other, or False otherwise.
        :param other:
        :return:
        """
        return False

    def clear(self):
        """
        Makes self become empty.
        :return:
        """
        pass

    def add(self, item):
        """
        Adds item to self
        :param item:
        :return:
        """
        pass

    def remove(self):
        """
        Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self.
        :return:
        """
        pass
