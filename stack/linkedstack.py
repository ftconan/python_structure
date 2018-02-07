# coding = utf-8

from array_linked_list.node import Node
from abstractstack import AbstractStack


class LinkedStack(AbstractStack):
    """
    Link-based stack implementation.
    """
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the contents of sourceCollection,
        if it's present.
        """
        self.items = None
        AbstractStack.__init__(self, source_collection)

    def __iter(self):
        """
        Supports iteration over a view of self.
        Visits items from bottom to top of stack.
        :return:
        """
        def visit_nodes(node):
            if node is not None:
                visit_nodes(node.next)
                temp_list.append(node.data)
        temp_list = list()
        visit_nodes(self.items)
        return iter(temp_list)

    def peek(self):
        """
        Returns the item at top of the stack,
        Precodition: the stack is not empty.
        Raises KeyError if the stack is empty.
        :return:
        """
        if self.is_empty():
            raise KeyError("The stack is empty.")
        return self.items.data

    def clear(self):
        """
        Makes self become empty.
        :return:
        """
        self.size = 0
        self.items = None

    def push(self, item):
        """
        Inserts item at top of the stack.
        :return:
        """
        # Resize array here if necessary
        self.items = Node(item, self.items)
        self.size += 1

    def pop(self):
        """
        Removes and returns the item at top of the stack.
        Precondition: the stack is not empty.
        Raises KeyError if the stack is empty.
        Postcondition: the top item is removed from the stack.
        :return:
        """
        if self.is_empty():
            raise KeyError("The stack is empty.")
        old_item = self.items.data
        self.size -= 1
        # Resize the array here if necessary
        return old_item
