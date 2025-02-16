class Stack:
    """Реализует функционал стека"""
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    """Реализует функционал очереди"""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


def get_key(k, key):
    """Возвращает атрибут объекта для сортировки"""
    return getattr(k, key)


def quick_sort(arr: list, key: str) -> list:
    result = arr[:]
    """Быстрая сортировка"""
    if len(result) <= 1:
        return result
    pivot = get_key(result[len(result) // 2], key)
    left = [x for x in result if get_key(x, key) < pivot]
    middle = [x for x in result if get_key(x, key) == pivot]
    right = [x for x in result if get_key(x, key) > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)


def merge_sort(arr: list, key: str) -> list:
    """Сортировка слиянием"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)


def merge(left: list, right: list, key: str):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if get_key(left[i], key) < get_key(right[j], key):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def heapify(arr: list, n: int, i: int, key: str):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and get_key(arr[left], key) > get_key(arr[largest], key):
        largest = left
    if right < n and get_key(arr[right], key) > get_key(arr[largest], key):
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)


def heap_sort(arr: list, key: str):
    """Пирамидальная сортировка"""
    arr = arr[:]
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)
    return arr


def binary_search(arr: list, x: str | int, key: str):
    """Бинарный поиск"""

    if len(arr) == 0:
        return f'Передан пустой массив'

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] is None:
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

        if get_key(arr[new_mid], key) == x:
            return new_mid
        elif get_key(arr[new_mid], key) < x:
            left = new_mid + 1
            continue
        elif get_key(arr[new_mid], key) > x:
            right = new_mid - 1
            continue
    return -1


def linear_search(arr: list, x: str | int, key: str):
    for elem in arr:
        if get_key(elem, key) == x:
            return elem
    return -1
