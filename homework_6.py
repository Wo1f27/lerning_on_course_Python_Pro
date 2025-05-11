import aiohttp
import aiofiles
import re
import asyncio
import time


MAX_CURRENT_REQUESTS = 5
RETRY_COUNT = 3


async def fetch(url, session):
    for attempt in range(RETRY_COUNT):
        try:
            async with session.get(url, timeout=10) as response:
                response.raise_for_status()
                return await response.text()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            print(f"Ошибка при загрузке {url}: {e}. Попытка {attempt + 1} из {RETRY_COUNT}.")
            await asyncio.sleep(2)
    return None


def parse_html(html):
    quotes = []
    quote_pattern = re.compile(
        r'<span class="text" itemprop="text">(.*?)</span>.*?<small class="author" itemprop="author">(.*?)</small>',
        re.DOTALL)

    for match in quote_pattern.finditer(html):
        quote_text = match.group(1).strip()
        author_name = match.group(2).strip()
        quotes.append({'quote': quote_text, 'author': author_name})

    return quotes


async def save_to_file(data, filename):
    async with aiofiles.open(filename, 'a', encoding='utf-8') as f:
        for item in data:
            quote = item['quote']
            author = item['author']
            await f.write(f'"{quote}" - {author}\n')


async def process_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch(url, session))
            tasks.append(task)

        for i in range(0, len(tasks), MAX_CURRENT_REQUESTS):
            chunk = tasks[i:i + MAX_CURRENT_REQUESTS]
            response = await asyncio.gather(*chunk)
            for html in response:
                if html:
                    quotes = parse_html(html)
                    await save_to_file(quotes, 'quotes.txt')


if __name__ == "__main__":
    start_time = time.time()
    urls = [
        'http://quotes.toscrape.com/'
    ]
    asyncio.run(process_urls(urls))
    print(f"Завершено за {time.time() - start_time:.2f} секунд.")
