"""Разработать простую систему управления библиотекой, где будут храниться данные о книгах.
Основной задачей является предоставление пользователю возможности сортировки книг по различным критериям,
таким как название книги, автор или год издания."""

class Book:

    def __init__(self, id: int, title: str, author: str, published: str):
        if not isinstance(id, int):
            raise TypeError("id должен быть целым числом")
        if not isinstance(title, str):
            raise TypeError("title должен быть строкой")
        if not isinstance(author, str):
            raise TypeError("author должен быть строкой")
        if not isinstance(published, str):
            raise TypeError("published должен быть строкой")

        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.published: str = published

    def __repr__(self):
        return f'{self.id}. {self.title} by {self.author} ({self.published})'


def add_book(arr: list, book: Book) -> str:
    """Добавление книги в библиотеку"""
    if not isinstance(book, Book):
        raise ValueError(f'Параметры не соответствуют классу Book')
    try:
        arr.append(book)
    except Exception as ex:
        raise Exception(f'Возникла ошибка при добавлении книги: {ex}')

    return 'Книга добавлена'


def remove_book(arr: list, id: int) -> str:
    """Удаление книги из библиотеки по ее номеру"""
    for book in arr:
        if book.id == int(id):
            arr.remove(book)
            return f'Книга {book.title} удалена'
    return f'Книга с ID: {id} не найдена'


def list_books(arr: list) -> None:
    """Показ списка книг в библиотеке"""
    for book in arr:
        print(book)


def search_book(arr: list, key: str, target: str) -> Book:
    """Поиск книг по заданному атрибуту"""
    for book in arr:
        if sort_key(book, key) == target:
            return book
    return f'Книга не найдена'


def save_to_file_txt(books, filename) -> str:
    """Сохраняет список книг в файл с расширение .txt"""
    with open(filename, 'w', encoding='utf-8') as file:
        for book in books:
            file.write(f'{book.id}; {book.title}; {book.author}; {book.published}; \n')
    return f'Книги сохранены'


def load_from_file_txt(filename) -> list:
    """Загружает данные из файла"""
    book_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            record = line.split('; ')
            add_book(book_list, Book(int(record[0]), record[1], record[2], record[3]))
    return book_list


def sort_key(k, key):
    """Возвращает атрибут объекта для сортировки"""
    return getattr(k, key)


def quick_sort(arr: list, key: str) -> list:
    """Быстрая сортировка"""
    if len(arr) <= 1:
        return arr
    pivot = sort_key(arr[len(arr) // 2], key)
    left = [x for x in arr if sort_key(x, key) < pivot]
    middle = [x for x in arr if sort_key(x, key) == pivot]
    right = [x for x in arr if sort_key(x, key) > pivot]
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
        if sort_key(left[i], key) < sort_key(right[j], key):
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

    if left < n and sort_key(arr[left], key) > sort_key(arr[largest], key):
        largest = left
    if right < n and sort_key(arr[right], key) > sort_key(arr[largest], key):
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


def sort_books_by_title(arr: list, key: str) -> None:
    """Сортировка книг по названию"""
    if key == 'quick_sort':
        sorted_books = quick_sort(arr, 'title')
    elif key == 'merge_sort':
        sorted_books = merge_sort(arr, 'title')
    elif key == 'heap_sort':
        sorted_books = heap_sort(arr, 'title')
    else:
        raise Exception(f'Передан неизвестный ключ')
    list_books(sorted_books)


def sort_books_by_author(arr: list, key: str) -> None:
    """Сортировка книг по автору"""
    if key == 'quick_sort':
        sorted_books = quick_sort(arr, 'author')
    elif key == 'merge_sort':
        sorted_books = merge_sort(arr, 'author')
    elif key == 'heap_sort':
        sorted_books = heap_sort(arr, 'author')
    else:
        raise Exception(f'Передан неизвестный ключ')
    list_books(sorted_books)


def sort_books_by_published(arr: list, key: str) -> None:
    """Сортировка книг по дате публикации"""
    if key == 'quick_sort':
        sorted_books = quick_sort(arr, 'published')
    elif key == 'merge_sort':
        sorted_books = merge_sort(arr, 'published')
    elif key == 'heap_sort':
        sorted_books = heap_sort(arr, 'published')
    else:
        raise Exception(f'Передан неизвестный ключ')
    list_books(sorted_books)


def main():
    books_list = []
    add_book(books_list, Book(1, '1984', 'Джордж Оруэлл', '1949'))
    add_book(books_list, Book(2, 'Убить пересмешника', 'Харпер Ли', '1960'))
    add_book(books_list, Book(3, 'Гордость и предубеждение', 'Джейн Остин', '1813'))
    add_book(books_list, Book(4, 'Мастер и Маргарита', 'Михаил Булгаков', '1967'))
    add_book(books_list, Book(5, 'Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд','1925'))
    add_book(books_list, Book(6, 'Преступление и наказание', 'Фёдор Достоевский', '1866'))
    add_book(books_list, Book(7, 'Сияние', 'Стивен Кинг', '1977'))
    add_book(books_list, Book(8, '451 градус по Фаренгейту', 'Рэй Брэдбери', '1953'))
    add_book(books_list, Book(9, 'Анна Каренина', 'Лев Толстой', '1877'))
    add_book(books_list, Book(10, 'Маленький принц', 'Антуан де Сент-Экзюпери', '1943'))
    while True:
        print(
            """Добро пожаловать в систему управления библиотекой!\n
            Выберите действие:
            1. Показать все книги
            2. Сортировать книги по названию
            3. Сортировать книги по автору
            4. Сортировать книги по году издания
            5. Найти книгу по названию
            6. Найти книгу по автору
            7. Добавить книгу
            8. Удалить книгу
            9. Сохранить книги в файл
            10. Загрзить книги из файла
            11. Выйти\n"""
        )

        action = input('Введите номер действия: ')
        match action:
            case '1':
                list_books(books_list)
            case '2':
                print('''\t1. Быстрая сортировка\n\t2. Сортировка слиянием\n\t3. Пирамидальная сортировка''')
                key = input('Выберите тип сортировки: ')
                match key:
                    case '1':
                        sort_books_by_title(books_list, 'quick_sort')
                    case '2':
                        sort_books_by_title(books_list, 'merge_sort')
                    case '3':
                        sort_books_by_title(books_list, 'heap_sort')
            case '3':
                print('''\t1. Быстрая сортировка\n\t2. Сортировка слиянием\n\t3. Пирамидальная сортировка''')
                key = input('Выберите тип сортировки: ')
                match key:
                    case '1':
                        sort_books_by_author(books_list, 'quick_sort')
                    case '2':
                        sort_books_by_author(books_list, 'merge_sort')
                    case '3':
                        sort_books_by_author(books_list, 'heap_sort')
            case '4':
                print('''\t1. Быстрая сортировка\n\t2. Сортировка слиянием\n\t3. Пирамидальная сортировка''')
                key = input('Выберите тип сортировки: ')
                match key:
                    case '1':
                        sort_books_by_published(books_list, 'quick_sort')
                    case '2':
                        sort_books_by_published(books_list, 'merge_sort')
                    case '3':
                        sort_books_by_published(books_list, 'heap_sort')
            case '5':
                target = input('Введите название книги: ')
                print(search_book(books_list, 'title', target))
            case '6':
                target = input('Введите автора книги: ')
                print(search_book(books_list, 'author', target))
            case '7':
                title = input('Введите название книги: ')
                author = input('Введите автора: ')
                published = input('Введите дату публикации: ')
                id = books_list[-1].id + 1
                add_book(books_list, Book(id, title, author, published))
                print('Книга добавлена!')
            case '8':
                id = input('Введите порядковый номер книги для удаления: ')
                try:
                    remove_book(books_list, id)
                    print('Книга удалена!')
                except Exception:
                    raise ValueError(f'Книга с номером {id} не найдена')
            case '9':
                print(save_to_file_txt(books_list, 'books.txt'))
            case '10':
                loaded_list = load_from_file_txt('books.txt')
                books_list.clear()
                books_list.extend(loaded_list)
                print('Книги загружены!')
            case '11':
                print('До свидания!')
                return False

        input('\nНажмите Enter для продолжения')


if __name__ == '__main__':
    main()
