import requests
from bs4 import BeautifulSoup
import csv

# HOST = "https://www.ivi.ru/"
CSV = "cards.csv"
URL = "https://www.ivi.ru/collections/new-movies"
HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


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
