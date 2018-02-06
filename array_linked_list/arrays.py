# coding = utf-8


class Array(object):
    """
    Represents an array.
    """
    def __init__(self, capacity, fill_value=None):
        """
        :param capacity: capacity is the static size of the array.
        :param fill_value: fill_value is placed at each position.
        """
        self.items = list()
        for count in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        """
        The capacity of the array.
        :return:
        """
        return len(self.items)

    def __str__(self):
        """
        The string representation of the array.
        :return:
        """
        return str(self.items)

    def __iter__(self):
        """
        Supports traversal with a for loop
        :return:
        """
        return iter(self.items)

    def __getitem__(self, index):
        """
        Subscript operator for access at index.
        :param index:
        :return:
        """
        return self.items[index]

    def __setitem__(self, index, new_item):
        """
        Subscript operator for replacement at index.
        :param key:
        :param value:
        :return:
        """
        self.items[index] = new_item


if __name__ == '__main__':
    a = Array(5)
    print len(a)
    print(a)
    for i in range(len(a)):
        a[i] = i + 1
    print a[0]
    for item in a:
        print item
