# coding = utf-8

from array_linked_list.node import Node
from inherit_abstract.abstractbag import AbstractBag


class LinkedBag(AbstractBag):
    """
    An link-based bag implementation.
    """
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the contents of source_collection,
        if it's present.
        """
        # self.items = None
        # self.size = 0
        # if source_collection:
        #     for item in source_collection:
        #         self.add(item)
        self.items = None
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
        cursor = self.items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    # def __add__(self, other):
    #     """
    #     Returns a new bag containing the contents or self and other
    #     :param other:
    #     :return:
    #     """
    #     self.items = Node(other, self.items)
    #     self.size += 1

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
        self.items = None

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
        # Search for the node containing the target item
        # probe will point to the target node
        # trailer will point to the one before it, if it exists
        probe = self.items
        trailer = None
        for target_item in self:
            if target_item == item:
                break
            trailer = probe
            probe = probe.next
        # Unhook te node to be deleted, either the first one or the one thereafter
        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next
        # Decrement logical size
        self.size -= 1
