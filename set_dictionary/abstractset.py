# coding= utf-8


class AbstractSet(object):
    """
    Generic set method implementations.
    """
    def __or__(self, other):
        """
        Returns the union of self and other.
        :param other:
        :return:
        """
        return self + other

    def __and__(self, other):
        """
        Returns the intersection of self adn other.
        :param other:
        :return:
        """
        intersection = type(self)()
        for item in self:
            if item in self:
                intersection.add(item)
        return intersection

    def __sub__(self, other):
        """
        Returns the difference of self and other.
        :param other:
        :return:
        """
        difference = type(self)()
        for item in self:
            if item not in self:
                difference.add(item)
        return difference

    def issubset(self, other):
        """
        Returns True if set is the other subset of other
        :param other:
        :return:
        """
        for item in self:
            if item not in other:
                return False
        return True
