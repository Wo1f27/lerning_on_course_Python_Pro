# Условие задачи:
#
# Вы имеете отсортированный массив, в котором некоторые элементы могут отсутствовать,
# но остальные элементы по-прежнему отсортированы. Например, массив может выглядеть следующим образом:
#
# [1, 2, None, None, 5, 6, 7, None, 10, 11]
#
# Где None представляет собой пропущенные элементы. Ваша задача — найти индекс заданного элемента в таком массиве,
# используя бинарный поиск. Если элемент отсутствует, возвращайте -1.

import pytest


def search_in_array(arr: list, x: int):

    if len(arr) == 0:
        return f'Передан пустой массив'

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2 # Находим середину массива

        if arr[mid] is None: # Проверка если серединный элемент None
            left_mid = mid - 1
            right_mid = mid + 1

            while True:
                if left_mid < left and right_mid > right: # Если выходим за границы массива возвращает -1
                    return -1
                elif left_mid >= left and arr[left_mid] is not None:
                    new_mid = left_mid
                    break
                elif right_mid <= right and arr[right_mid] is not None:
                    new_mid = right_mid
                    break
                left_mid -= 1
                right_mid += 1
        else:
            new_mid = mid

        if arr[new_mid] == x:
            return new_mid
        elif arr[new_mid] < x:
            left = new_mid + 1
            continue
        elif arr[new_mid] > x:
            right = new_mid - 1
            continue
    return -1


def test_search_in_array():
    arr = [1, 2, None, None, 5, 6, 7, None, 10, 11]
    assert search_in_array(arr, 7) == 6
    assert search_in_array(arr, 12) == -1
    assert search_in_array(arr, 1) == 0
    assert search_in_array([], 10) == 'Передан пустой массив'
    arr_none = [None, None, None, None]
    assert search_in_array(arr_none, 10) == -1
    arr_single_num = [None, None, None, 2, None, None]
    assert search_in_array(arr_single_num, 2) == 3


if __name__ == '__main__':
    pytest.main()
