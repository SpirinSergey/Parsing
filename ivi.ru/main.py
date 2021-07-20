import requests
from bs4 import BeautifulSoup
import csv
from config import URL, HEADERS, CSV


def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    if response:
        print(f'Успех! Код сервера - {response.status_code}')
        response.encoding = 'utf-8'
        print(response.headers['Content-Type'])
    return response


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='gallery__item')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('div', class_='nbl-slimPosterBlock__title').get_text(),
                'link_pic': item.find('div', class_='nbl-slimPosterBlock__extraItem').find('img').get('src')
            }
        )
    return cards


def save_svg(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Название", "Ссылка"])
        for item in items:
            writer.writerow([item["title"], item["link_pic"]])


html = get_html(URL)
save_svg(get_content(html.text), CSV)
