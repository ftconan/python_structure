# coding = utf-8

from array_linked_list.arrays import Array
from abstractstack import AbstractStack


class ArrayStack(AbstractStack):
    """
    An array-based stack implementation.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the contents of sourceCollection,
        if it's present.
        """
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, source_collection)

    def __iter(self):
        """
        Supports iteration over a view of self.
        Visits items from bottom to top of stack.
        :return:
        """
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def peek(self):
        """
        Returns the item at top of the stack,
        Precodition: the stack is not empty.
        Raises KeyError if the stack is empty.
        :return:
        """
        return self.items[len(self) -1]

    def clear(self):
        """
        Makes self become empty.
        :return:
        """
        self.size = 0
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """
        Inserts item at top of the stack.
        :return:
        """
        # Resize array here if necessary
        self.items[len(self)] = item
        self.item += 1

    def pop(self):
        """
        Removes and returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raises KeyError if the stack is empty.
        Postcondition: the top item is removed from the stack.
        :return:
        """
        old_item = self.items[len(self) - 1]
        self.size -= 1
        # Resize the array here if necessary
        return old_item
