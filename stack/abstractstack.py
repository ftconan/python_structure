# coding = utf-8

from inherit_abstract.abstractcollection import AbstractCollection


class AbstractStack(AbstractCollection):
    """
    An abstract stack implementation.
    """
    def __init__(self, source_collection):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        :param source_collection:
        """
        AbstractCollection.__init__(self, source_collection)

    def add(self, item):
        """
        Adds item to self.
        :param item:
        :return:
        """
        self.push(item)
