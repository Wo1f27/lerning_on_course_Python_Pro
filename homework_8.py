"""
1. Создание каррированных функций:

Функция для расчета отработанных часов
Напишите каррированную функцию hours_per_day(hours) которая возвращает функцию, которая умножает количество 
отработанных дней на заданное количество часов в день. Например, hours_per_day(8)(20) должно возвращать 160, 
так как 8 часов в день умножить на 20 дней равно 160.
"""


def hours_per_day(hours):
    def calculate_days(days):
        return hours * days
    return calculate_days


"""
Функция для расчета бонусов
Напишите каррированную функцию bonus_percentage(percentage) которая возвращает функцию, которая вычисляет 
бонус от зарплаты. Например, bonus_percentage(10)(3000) должно возвращать 300, так как бонус 10% от 3000 — это 300.
"""


def bonus_percentage(percent):
    def calculate_salary(salary):
        return percent * (salary // 100)
    return calculate_salary


"""
2. Частичное применение:

Функция для расчета чистой зарплаты
Напишите функцию net_salary(gross_salary, tax_rate) для расчета чистой зарплаты после вычета налогов. 
Используйте functools.partial для создания функции с фиксированной налоговой ставкой, например, 20%.
"""

def net_salary(gross_salary, tax_rate):
    return gross_salary - (gross_salary * tax_rate)


"""
Функция для расчета итоговой зарплаты с учетом бонусов
Напишите функцию final_salary(base_salary, bonus) для расчета итоговой зарплаты с учетом бонусов. 
Используйте functools.partial для создания функции с фиксированным бонусом, например, 500.
"""

def final_salary(base_salary, bonus):
    return base_salary + bonus


"""
3. Композиция функций

Функции для расчета заработной платы
Напишите функции calculate_hours(hours_per_day, days) и calculate_gross_salary(hours, hourly_rate), 
где calculate_hours вычисляет общее количество отработанных часов, а calculate_gross_salary вычисляет 
заработную плату до вычета налогов. Затем создайте композицию этих функций, чтобы получить 
конечную зарплату до вычета налогов.
"""

def calculate_hours(hours_per_day, days):
    return hours_per_day * days


def calculate_gross_salary(hours, hourly_rate):
    return hours * hourly_rate

def composed_salary_function(hours_per_day, days, hourly_rate):
    return calculate_gross_salary(calculate_hours(hours_per_day, days), hourly_rate)


"""
Функции для итогового расчета
Напишите функции calculate_net_salary(gross_salary) и apply_bonus(salary, bonus). Создайте композицию этих функций, 
чтобы получить чистую зарплату после применения бонусов и вычета налогов.
"""

def calculate_net_salary(gross_salary):
    tax_rate = 0.20
    return gross_salary - (gross_salary * tax_rate)


def apply_bonus(salary, bonus):
    return salary + bonus

def final_salary_composition(gross_salary, bonus):
    return apply_bonus(calculate_net_salary(gross_salary), bonus)


if __name__ == "__main__":
    from functools import partial

    print('\tСоздание каррированных функций')
    print('Функция для расчета отработанных часов:')
    print(hours_per_day(8)(20))
    print('Функция для расчета бонусов:')
    print(bonus_percentage(10)(3000))
    print('\tЧастичное применение')
    print('Функция для расчета чистой зарплаты:')
    tax_20 = partial(net_salary, tax_rate=0.20)
    print(tax_20(5000))
    print('Функция для расчета итоговой зарплаты с учетом бонусов:')
    bonus_500 = partial(final_salary, bonus=500)
    print(bonus_500(3000))
    print('\tКомпозиция функций')
    print('Функции для расчета заработной платы:')
    print(composed_salary_function(8, 20, 25))
    print('Функции для итогового расчета:')
    print(final_salary_composition(4000, 300))
    