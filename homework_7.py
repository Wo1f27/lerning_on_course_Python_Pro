import asyncio


counter = 0
increments_for_tasks = 1000
num_tasks = 5

lock = asyncio.Lock()


async def increment_counter():
    global counter
    for i in range(increments_for_tasks):
        counter += 1


async def main():
    tasks = [increment_counter() for i in range(num_tasks)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    expected_value = num_tasks * increments_for_tasks
    print(f'Значение счетчика: {counter}, Ожидаемое значение: {expected_value}')
