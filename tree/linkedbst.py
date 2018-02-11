# coding = utf-8

from inherit_abstract.abstractcollection import AbstractCollection
from bstnode import BSTNode


class LinkedBST(AbstractCollection):
    """
    A link-based binary search tree implementation.
    """
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the contents of source_collection,
        if it's present.
        :param source_collection:
        """
        self.root = None
        AbstractCollection.__init__(source_collection)

    def finde(self, item):
        """
        Returns data if item is found or None otherwise.
        :return:
        """
        # Helpler function t search the binary tree
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        # Top-level call on the root node
        return recurse(self.root)

    def inorder(self):
        """
        Supports an inorder travesal on a vbiew of self.
        :return:
        """
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)
        recurse(self.root)
        return iter(lyst)

    def __str__(self):
        """
        Returns a string representation with the tree rotated
        90 degrees counterclockwise.
        :return:
        """
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " + level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self.root, 0)

    def add(self, item):
        """
        Adds item to the tree.
        :param item:
        :return:
        """
        # Helper function to search for item's position
        def recurse(node):
            # New item is less; go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal;
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)

            # Tree is empty, so new item goes at the root
            if self.is_empty():
                self.root = BSTNode(item)
            else:
                recurse(self.root)
            self.size += 1
