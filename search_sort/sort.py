# coding=utf-8
import random
from _ctypes import Array


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


def quick_sort(lyst):
    """
    快排
    :param lyst:
    :return:
    """
    quick_sort_helper(lyst, 0, len(lyst) - 1)


def quick_sort_helper(lyst, left, right):
    """
    快排递归
    :param lyst:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        pivot_location = partition(lyst, left, right)
        quick_sort_helper(lyst, left, pivot_location - 1)
        quick_sort_helper(lyst, pivot_location + 1, right)


def partition(lyst, left, right):
    """
    切割
    :param lyst:
    :param left:
    :param right:
    :return:
    """
    # Find the pivot and exchange it with the lalst item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap(lyst, right, boundary)
    return boundary


def main(size=20, sort=quick_sort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print(lyst)
    sort(lyst)
    print(lyst)


def merge_sort(lyst):
    """
    lyst       list being sorted
    copy_buffer temporary space needed during merge
    :param lyst:
    :return:
    """
    # copy_buffer = Array(len(lyst))
    copy_buffer = lyst
    merge_sort_helper(lyst, copy_buffer, 0, len(lyst) - 1)


def merge_sort_helper(lyst, copy_buffer, low, high):
    """
    :param lyst: list being sorted
    :param copy_buffer: temp space needed during merge
    :param low: bounds of sublist
    :param high: bounds of sublist
    :return:
    """
    if low < high:
        middle = (low + high) // 2
        merge_sort_helper(lyst, copy_buffer, low, middle)
        merge_sort_helper(lyst, copy_buffer, middle + 1, high)
        merge(lyst, copy_buffer, low, middle, high)


def merge(lyst, copy_buffer, low, middle, high):
    """
    :param lyst: list that is being sorted
    :param copy_buffer: temp space needed during the merge process
    :param low: beginning of first sorted sublist
    :param middle: end of first sorted sublist
    :param high: end of second sorted sublist
    :return:
    """
    # Initialize i1 and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1
    # Interleave items from the sublists into the copy_buffer in such a way that order is maintained
    for i in range(low, high + 1):
        if i1 > middle:
            # First sublist exhausted
            copy_buffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            # Second sublist exhausted
            copy_buffer[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            # Item in first sublist <
            copy_buffer[i] = lyst[i2]
        else:
            # Item in second sublist <
            copy_buffer[i] = lyst[i2]
            i2 += 1

    # Copy sorted items back to proper position in lyst
    for i in range(low, high + 1):
        lyst[i] = copy_buffer[i]


def fib(n):
    """
    Fibonacci
    :param n:
    :return:
    """
    sum = 0
    if n > 2:
        first = 1
        second = 1
        sum = first + second
        count = 3
        while count <= n:
            temp = first + second
            first = second
            second = temp
            sum += temp
            count += 1
    return sum


if __name__ == '__main__':
    selection_sort([5, 3, 1, 2, 4])
    bubble_sort([5, 3, 1, 2, 4])
    bubble_sort_with_tweak([5, 3, 1, 2, 4])
    insertion_sort([5, 3, 1, 2, 4])
    main()
    merge_sort([5, 3, 1, 2, 4])
    fib(1)
