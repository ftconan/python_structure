# coding = utf-8

from array_linked_list.node import TwoWayNode
from abstractlist import AbstractList


class LinkedList(AbstractList):
    """
    A link-based list implementation.
    """

    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the contents of source_collection, if it's present.
        :param source_collection:
        """
        # Uses a circular structure with a sentinel node
        self.head = TwoWayNode()
        self.head.previous = self.head.next = self.head
        AbstractList.__init__(self, source_collection)

    def __iter__(self):
        """
        Supports iteration over a view of self.
        :return:
        """
        cursor = self.head.next
        while cursor != self.head:
            yield cursor.data
            cursor = cursor.next

    def get_node(self, i):
        """
        Helper method: returns a pointer to the node at position i.
        :param i:
        :return:
        """
        if i == len(self):
            return self.head
        if i == len(self) - 1:
            return self.head.previous
        probe = self.head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    def __setitem__(self, i, item):
        """
        Precondition: o <= i < len(self)
        Replaces the item at position i.
        Raises: IndexError.
        :param i:
        :param item:
        :return:
        """
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self.get_node(i).data = item

    def insert(self, i, item):
        """
        Inserts the item at position i.
        :param i:
        :param item:
        :return:
        """
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)
        the_node = self.get_node(i)
        new_node = TwoWayNode(item, the_node.previous, the_node)
        the_node.previous.next = new_node
        the_node.previous = new_node
        self.size += 1
        self.inc_mod_count()
