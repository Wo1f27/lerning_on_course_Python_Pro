import time
class Task:

    def __init__(self, name: str, duration: str):
        self.name = name
        self.duration = duration

    def __repr__(self):
        return f'Task: {self.name}, Duration: {self.duration}'


class TaskScheduler:

    def __init__(self):
        self.queue = Queue()

    def add_task(self, task: Task) -> str:
        try:
            self.queue.enqueue(task)
            return f'Задача {task.name} добавлена'
        except Exception as e:
            raise ValueError(f'Задача {task.name} не добавлена: {e}')

    def execute_tasks(self) -> None:
        while not self.queue.is_empty():
            start_time = time.time()
            task = self.queue.dequeue()
            time.sleep(float(task.duration))
            end_time = time.time()
            print(f'Задача {task.name} выполнена, время выполнения: {end_time - start_time}')

    def is_empty(self) -> bool:
        return self.queue.is_empty()

    def count_tasks(self) -> int:
        return len(self.queue)


class Queue:
    """Реализует функционал очереди"""
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


def main():
    tasks_scheduler = TaskScheduler()

    tasks = [
        Task('Task#1', '2'),
        Task('Task#2', '2.5'),
        Task('Task#3', '1.5'),
        Task('Task#4', '2'),
        Task('Task#5', '2.5')
    ]

    for i in tasks:
        print(tasks_scheduler.add_task(i))

    print(f'Количество задач в очереди: {tasks_scheduler.count_tasks()}')
    tasks_scheduler.execute_tasks()


if __name__ == '__main__':
    main()



