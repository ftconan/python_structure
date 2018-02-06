# coding = utf-8

from array_linked_list.arrays import Array


class Grid(object):
    """
    Represents a two-dimensional array.
    """
    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        """
        Returns the number of the rows.
        :return:
        """
        return len(self.data)

    def get_width(self):
        """
        Returns the number of the columns.
        :return:
        """
        return len(self.data[0])

    def __getitem__(self, index):
        """
        Supports two-dimensional indexing with [row][column]
        :param index:
        :return:
        """
        return self.data[index]

    def __str__(self):
        """
        Return a string representation of the grid.
        :return:
        """
        result = ''
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + ' '
            result += '\n'
        return result


if __name__ == '__main__':
    table = Grid(4, 5, 0)
    print table
