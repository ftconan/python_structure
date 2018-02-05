# coding=utf-8


def index_of_min(lyst):
    """
    min()
    搜索最小值
    Returns teh index of minimum items.
    :param lyst:
    :return:
    """
    min_index = 0
    current_index = 1
    while current_index < len(lyst):
        if lyst[current_index] < lyst[min_index]:
            min_index = current_index
        current_index += 1
    return min_index


def sequential_search(target, lyst):
    """
    in()
    顺序搜索
    Returns the position of the target item if found, or -1 otherwise.
    :param target:
    :param lyst:
    :return:
    """
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1


def binary_search(target, sorted_list):
    """
    二叉搜索 log2n
    分页法
    :param target:
    :param sorted_list:
    :return:
    """
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid_point = (left + right) // 2
        if target == sorted_list[mid_point]:
            return mid_point
        elif target < sorted_list[mid_point]:
            right = mid_point - 1
        else:
            left = mid_point + 1
    return -1


if __name__ == '__main__':
    index_of_min([6, 3, 4, 8, 1, 9])
    sequential_search(1, [6, 3, 4, 8, 1, 9])
    binary_search(1, [1, 2, 3, 4, 5, 6])
