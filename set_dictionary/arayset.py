# coding = utf-8

from inherit_abstract.arrraybag import ArrayBag
from abstractset import AbstractSet


class ArraySet(ArrayBag, AbstractSet):
    """
    An array-based implementation of a set.
    """
    def __init__(self, source_collection=None):
        ArrayBag.__init__(self, source_collection)

    def add(self, item):
        """
        Ads item to the set if it is not in the set.
        :param item:
        :return:
        """
        if item not in self:
            ArrayBag.add(self, item)
