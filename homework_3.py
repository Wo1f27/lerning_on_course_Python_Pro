import pytest


employees = []


class Employee:

    def __init__(self, first_name, last_name, age, salary, position, tab_id):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.salary: float = salary
        self.position: str = position
        self.tab_id: int = tab_id

    def __repr__(self):
        return (f'{self.tab_id}: {self.last_name} {self.first_name}, Возраст: {self.age}, '
                    f'Должность: {self.position}, Зарплата: {self.salary}')


def add_employer(employer: Employee) -> str:

    """Функция для добавления сотрудников в спсок"""

    if not isinstance(employer, Employee):
        raise ValueError('Должен быть экземпляр класса Employee')
    try:
        employees.append(employer)
    except Exception as ex:
        raise Exception(f'При добавлении сотрудника возникла ошибка с данными: {ex}')
    return f'Сотрудник {employer} успешно добавлен'


def shell_sort(arr: list[Employee], key: str):

    """
    Алгоритм сортировки Шелла\n
    arr: список сотрудников\n
    key: поле по которому нужно отсортировать список
    """

    sort_key = lambda emp: getattr(emp, key)
    length_arr = len(arr)
    gap = length_arr // 2

    while gap > 0:
        for i in range(gap, length_arr):
            temp = arr[i]
            j = i
            while j >= gap and sort_key(arr[j - gap]) > sort_key(temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def display_employees(arr: list[Employee]) -> None:

    """Возвращает список сотрудников в удобочитаемом виде"""

    for emp in arr:
        print(emp)


# Ниже тесты
@pytest.fixture
def employees_fixture() -> list[Employee]:
    employees.clear()
    add_employer(Employee('Иван', 'Иванов', 21, 50000, 'Кладовщик', 1))
    add_employer(Employee('Михаил', 'Сидоров', 23, 60000, 'Сборщик', 2))
    add_employer(Employee('Андрей', 'Боровков', 29, 40000, 'Охранник', 3))
    add_employer(Employee('Борис', 'Стругацкий', 44, 55000, 'Архитектор', 4))
    add_employer(Employee('Вероника', 'Алимова', 33, 52000, 'Секретарь', 5))
    return employees


def test_sort_for_first_name(employees_fixture: list[Employee]) -> None:
    shell_sort(employees_fixture, 'first_name')
    assert employees_fixture[0].first_name == 'Андрей'
    assert employees_fixture[1].first_name == 'Борис'
    assert employees_fixture[2].first_name == 'Вероника'
    assert employees_fixture[3].first_name == 'Иван'
    assert employees_fixture[4].first_name == 'Михаил'


def test_sort_for_last_name(employees_fixture: list[Employee]) -> None:
    shell_sort(employees_fixture, 'last_name')
    assert employees_fixture[0].last_name == 'Алимова'
    assert employees_fixture[1].last_name == 'Боровков'
    assert employees_fixture[2].last_name == 'Иванов'
    assert employees_fixture[3].last_name == 'Сидоров'
    assert employees_fixture[4].last_name == 'Стругацкий'


def test_sort_for_age(employees_fixture: list[Employee]) -> None:
    shell_sort(employees_fixture, 'age')
    assert employees_fixture[0].age == 21
    assert employees_fixture[1].age == 23
    assert employees_fixture[2].age == 29
    assert employees_fixture[3].age == 33
    assert employees_fixture[4].age == 44


def test_sort_for_salary(employees_fixture: list[Employee]) -> None:
    shell_sort(employees_fixture, 'salary')
    assert employees_fixture[0].salary == 40000
    assert employees_fixture[1].salary == 50000
    assert employees_fixture[2].salary == 52000
    assert employees_fixture[3].salary == 55000
    assert employees_fixture[4].salary == 60000


def test_sort_for_position(employees_fixture: list[Employee]) -> None:
    shell_sort(employees_fixture, 'position')
    assert employees_fixture[0].position == 'Архитектор'
    assert employees_fixture[1].position == 'Кладовщик'
    assert employees_fixture[2].position == 'Охранник'
    assert employees_fixture[3].position == 'Сборщик'
    assert employees_fixture[4].position == 'Секретарь'


if __name__ == '__main__':
    employees.clear()
    add_employer(Employee('Иван', 'Иванов', 21, 50000, 'Кладовщик', 1))
    add_employer(Employee('Михаил', 'Сидоров', 23, 60000, 'Сборщик', 2))
    add_employer(Employee('Андрей', 'Боровков', 29, 40000, 'Охранник', 3))
    add_employer(Employee('Борис', 'Стругацкий', 44, 55000, 'Архитектор', 4))
    add_employer(Employee('Вероника', 'Алимова', 33, 52000, 'Секретарь', 5))

    display_employees(employees)
    print('\n================Сортировка по имени====================')
    shell_sort(employees, 'first_name')
    display_employees(employees)
    print('\n================Сортировка по фамилии==================')
    shell_sort(employees, 'last_name')
    display_employees(employees)
    print('\n================Сортировка по возрасту=================')
    shell_sort(employees, 'age')
    display_employees(employees)
    print('\n================Сортировка по зарплате=================')
    shell_sort(employees, 'salary')
    display_employees(employees)
    print('\n================Сортировка по должности================')
    shell_sort(employees, 'position')
    display_employees(employees)



