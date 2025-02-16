import utils
import time
from datetime import datetime


class Delivery:
    def __init__(self, delivery_id, sender_point, destination, weight, time_of_delivery, is_urgent=False):
        self.delivery_id = delivery_id
        self.sender_point = sender_point
        self.destination = destination
        self.weight = weight
        self.time_of_delivery = datetime.strptime(time_of_delivery, '%Y-%m-%d %H:%M')
        self.is_urgent = is_urgent

    def __repr__(self):
        return (f'Доставка: {self.delivery_id}; {self.sender_point} -> {self.destination}; Вес: {self.weight};'
                f' Дата доставки: {self.time_of_delivery}\n')


class DeliveryManagementSystem:

    def __init__(self):
        self.deliveries = []
        self.urgent_delivery = utils.Stack()
        self.non_urgent_delivery = utils.Queue()

    def list_deliveries(self, arr: list):
        if len(arr) != 0:
            for deliv in arr:
                print(deliv)
        else:
            return 'Список доставок пуст'

    def add_delivery(self, delivery: Delivery):
        try:
            self.deliveries.append(delivery)
        except Exception as ex:
            raise ValueError(f'Ошибка оформления доставки {ex}')

    def remove_delivery(self, delivery_id: int):
        for delivery in self.deliveries:
            if delivery.delivery_id == delivery_id:
                self.deliveries.remove(delivery)
                return f'Доставка удалена'
        return f'Доставка с номером {delivery_id} не найдена'

    def update_delivery(self, delivery_id, **kwargs):
        for delivery in self.deliveries:
            if delivery.delivery_id == delivery_id:
                for key, value in kwargs.items():
                    setattr(delivery, key, value)
                    return f'Доставка {delivery_id} изменена'
        return f'Доставка с номером {delivery_id} не найдена'

    def sort_by_weight(self):
        return utils.merge_sort(self.deliveries, 'weight')

    def sort_by_time_of_delivery(self):
        return utils.quick_sort(self.deliveries, 'time_of_delivery')

    def sort_by_delivery_id(self):
        return utils.heap_sort(self.deliveries, 'delivery_id')

    def search_delivery_id(self, target: int):
        return utils.linear_search(self.deliveries, target, 'delivery_id')

    def search_time_of_delivery(self, target: str | datetime):
        return utils.binary_search(self.deliveries, target, 'time_of_delivery')

    def add_request_for_delivery(self, elem: Delivery):
        if elem.is_urgent:
            self.urgent_delivery.push(elem)
        else:
            self.non_urgent_delivery.enqueue(elem)

    def process_request(self):
        while not self.urgent_delivery.is_empty():
            time.sleep(1)
            delivery = self.urgent_delivery.pop()
            self.add_delivery(delivery)
            print(f'Запрос на срочную доставку {delivery.delivery_id} обработан')

        while not self.non_urgent_delivery.is_empty():
            time.sleep(1)
            delivery = self.non_urgent_delivery.dequeue()
            self.add_delivery(delivery)
            print(f'Запрос {delivery.delivery_id} обработан по очереди')


if __name__ == '__main__':

    test_requests_for_delivery = [
        Delivery(1, 'Москва','Санкт-Петербург', 3.5, '2025-02-20 11:00'),
        Delivery(2, 'Санкт-Петербург', 'Нижний-Новгород', 4.2, '2025-02-18 12:30', True),
        Delivery(3, 'Москва', 'Тверь', 1, '2025-02-21 17:30'),
        Delivery(4, 'Архангельск', 'Москва', 5.4, '2025-02-19 15:00', True),
        Delivery(5, 'Москва', 'Екатеринбург', 3.1, '2025-02-22 09:00', True),
        Delivery(6, 'Москва', 'Самара', 1.1, '2025-02-25 07:00'),
        Delivery(7, 'Санкт-Петербург', 'Екатеринбург', 7.3, '2025-02-28 13:00', True),
        Delivery(8, 'Самара', 'Москва', 5.0, '2025-02-22 16:00'),
        Delivery(9, 'Самара', 'Брянск', 3.9, '2025-02-25 11:00'),
        Delivery(10, 'Москва', 'Ростов', 6.4, '2025-02-24 12:00', True),
    ]

    dms = DeliveryManagementSystem()

    while True:
        print(
            """Добро пожаловать в систему управления доставками.\n
            Для выбора введите номер пункта\n
            1. Обработать запросы на доставку
            2. Показать запросы на доставку
            3. Добавить запрос на доставку
            4. Поиск доставки по номеру доставки
            5. Поиск доставки по времени доставки
            6. Отсортировать доставки по номеру доставки
            7. Отсортировать доставки по времени доставки
            8. Отсортировать доставки по весу груза
            9. Показать список доставок
            10. Выйти\n"""
        )

        action = input('Введите номер действия: ')
        match action:
            case '1':
                for i in test_requests_for_delivery:
                    dms.add_request_for_delivery(i)
                dms.process_request()
            case '2':
                print(test_requests_for_delivery)
            case '3':
                delivery_id = dms.deliveries[-1].delivery_id + 1
                sender_point = input('Введите пункт отправления: ')
                destination = input('Введите пункт назанчения: ')
                weight = input('Укажите вес груза: ')
                time_of_delivery = input('Укажите дату доставки: ')
                while True:
                    urgent = input('Доставка срочная? (Y/n): ')
                    if urgent == 'Y':
                        is_urgent = True
                        break
                    elif urgent == 'n':
                        is_urgent = False
                        break
                    else:
                        print('Введено некорректное значение, попробуйте еще раз! ')
                dms.add_request_for_delivery(
                    Delivery(delivery_id, sender_point, destination, weight, time_of_delivery, is_urgent)
                )
            case '4':
                params_to_search = input('Введите номер доставки: ')
                try:
                    params_to_search = int(params_to_search)
                except ValueError:
                    print('Введено некорректное значение!')
                print(dms.search_delivery_id(params_to_search))
            case '5':
                params_to_search = input('Введите дату доставки: ')
                isinstance(params_to_search, str)
                params_to_search = datetime.strptime(params_to_search, '%Y-%m-%d %H:%M')
                ind = dms.search_time_of_delivery(params_to_search)
                print(dms.deliveries[ind])
            case '6':
                deliveries = dms.sort_by_delivery_id()
                print(dms.list_deliveries(deliveries))
            case '7':
                deliveries = dms.sort_by_time_of_delivery()
                print(dms.list_deliveries(deliveries))
            case '8':
                deliveries = dms.sort_by_weight()
                print(dms.list_deliveries(deliveries))
            case '9':
                print(dms.list_deliveries(dms.deliveries))
            case '10':
                print('До свидания!')
                break
            case '11':
                print(test_requests_for_delivery)
        input('Нажмите Enter для продолжения...')




