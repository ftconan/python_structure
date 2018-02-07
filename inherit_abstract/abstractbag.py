# coding = utf-8


class AbstractBag(object):
    """
    Sets the initial state of self, which includes the
    contents of source_collection, if it's present.
    """
    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the contents of source_collection,
        if it's present.
        """
        self.size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    def __add__(self, other):
        """
        Returns a new bag containing the contents of self and other.
        :param other:
        :return:
        """
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result
