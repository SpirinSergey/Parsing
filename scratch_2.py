
# scraper.py
import requests
from bs4 import BeautifulSoup

url = 'https://ivi.ru/movies/2020'
headers = {}

response = requests.get(url)
if response:
    print(f'Успех! Код сервера - {response.status_code}')
    response.encoding = 'utf-8'
    print(response.headers['Content-Type'])

    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='gallery__item gallery__item_virtual')
else:
    print(f'Ошибка... Код сервера - {response.status_code}')





