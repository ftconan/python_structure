# coding = utf-8


class AbstractCollection(object):
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

    def _eq__(self, other):
        """
        Returns True if self equals other, or False otherwise.
        :param other:
        :return:
        """
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        other_iter = iter(other)
        for item in self:
            if item != next(other_iter):
                return False
        return True
