import asyncio
import time
from datetime import datetime


class Command:
    def execute(self):
        raise NotImplementedError("You should implement this method.")


class Task(Command):
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.created_at = datetime.now()

    def execute(self):
        print(f"Executing task {self.task_id}: {self.description}")
        time.sleep(2)
        print(f"Task {self.task_id} completed.")


class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def sort_tasks(self):
        n = len(self.tasks)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.tasks[j].created_at < self.tasks[min_index].created_at:
                    min_index = j
            self.tasks[i], self.tasks[min_index] = self.tasks[min_index], self.tasks[i]

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

async def run_task(task):
    await asyncio.sleep(1)
    task.execute()

async def run_all_tasks(task_manager):
    tasks = [run_task(task) for task in task_manager.tasks]
    await asyncio.gather(*tasks)

async def main():
    task_manager = TaskManager()
    task_id_counter = 1

    while True:
        print("\n1. Добавить задачу")
        print("2. Удалить задачу по ID")
        print("3. Запустить все задачи")
        print("4. Просмотреть список задач")
        print("5. Найти задачу по ID")
        print("6. Выход")
        choice = input("Выберите действие: ")

        match choice:
            case '1':
                description = input("Введите описание задачи: ")
                task = Task(task_id_counter, description)
                task_manager.add_task(task)
                print(f"Задача добавлена с ID {task_id_counter}.")
                task_id_counter += 1

            case '2':
                task_id = int(input("Введите ID задачи для удаления: "))
                task_manager.remove_task(task_id)
                print(f"Задача с ID {task_id} удалена.")

            case '3':
                await run_all_tasks(task_manager)

            case '4':
                task_manager.sort_tasks()
                for task in task_manager.tasks:
                    print(f"ID: {task.task_id}, Описание: {task.description}, Время создания: {task.created_at}")

            case '5':
                task_id = int(input("Введите ID задачи для поиска: "))
                task = task_manager.find_task(task_id)
                if task:
                    print(f"Найдена задача: ID: {task.task_id}, Описание: {task.description}")
                else:
                    print("Задача не найдена.")

            case '6':
                print("Выход из программы.")
                break

            case _:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    asyncio.run(main())
