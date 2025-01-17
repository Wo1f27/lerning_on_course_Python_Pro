# [3, 1, 4, 1, 5, 9, 2, 6, 5]
# 4.0 (так как сумма всех элементов равна 36, а количество элементов равно 9, поэтому среднее значение равно 36 / 9)

def avg_number(lst: list):
    sum_num = 0
    for num in lst:
        sum_num += num
    avg_num = sum_num / len(lst)
    return avg_num


def avg_number_2(lst: list):
    avg_num = sum(lst) / len(lst)
    print(avg_num)
    return avg_num
