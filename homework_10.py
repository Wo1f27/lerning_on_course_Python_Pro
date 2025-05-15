"""
Реализовать парсер, который собирает все заголовки 3 уровня(h3),
со страницы https://ru.wikipedia.org/wiki/Python и сохраняет их в текстовый файл
"""

import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Python'

response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

h3_headers = soup.find_all('h3')

with open('headers.txt', 'w', encoding='utf-8') as file:
    for header in h3_headers:
        header_text = header.get_text(strip=True)
        file.write(header_text + '\n')

print("Success saved to 'headers.txt'.")