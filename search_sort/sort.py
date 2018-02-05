# coding=utf-8


def swap(lyst, i, j):
    """
    Exchanges the items at positions i and j.
    :param lyst:
    :param i:
    :param j:
    :return:
    """
    # temp = lyst[j]
    # lyst[i] = lyst[j]
    # lyst[j] = temp
    lyst[i], lyst[j] = lyst[j], lyst[i]


def selection_sort(lyst):
    """
    选择排序
    :param lyst:
    :return:
    """
    i = 0
    # n-1次 选择最小的放在第i位置上
    while i < len(lyst) - 1:
        min_index = i
        j = i + 1
        # 找到第j位置上最小的数
        while j < len(lyst):
            if lyst[j] < lyst[min_index]:
                min_index = j
            j += 1
        # 交换
        if min_index != i:
            swap(lyst, min_index, i)
        i += 1
    return lyst


def bubble_sort(lyst):
    """
    冒泡排序
    :param lyst:
    :return:
    """
    n = len(lyst)
    # n-1 bubble
    while n > 1:
        i = 1
        # 把大的数字通过两两交换最后
        while i < n:
            if lyst[i] < lyst[i -1]:
                swap(lyst, i, i-1)
            i += 1
        n -= 1
    return lyst


def bubble_sort_with_tweak(lyst):
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i-1]:
                swap(lyst, i, i-1)
                swapped = True
            i += 1
        # 不需要交换
        if not swapped:
            return lyst
        n -= 1


def insertion_sort(lyst):
    """
    插入排序
    :param lyst:
    :return:
    """
    i = 1
    while i < len(lyst):
        item_to_insert = lyst[i]
        j = i - 1
        # 找到最小的插到第j位置上
        while j >= 0:
            if item_to_insert < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = item_to_insert
        i += 1
    return lyst


if __name__ == '__main__':
    selection_sort([5, 3, 1, 2, 4])
    bubble_sort([5, 3, 1, 2, 4])
    bubble_sort_with_tweak([5, 3, 1, 2, 4])
    insertion_sort([5, 3, 1, 2, 4])
