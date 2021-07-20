import requests
from bs4 import BeautifulSoup
import config



# Получение страницы
def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    if response:
        return response.text
    else:
        print(f'Ошибка... Код сервера - {response.status_code}')


def get_content(html):
    return BeautifulSoup(html, 'lxml')


# Выводит последнюю новость
def new(url):
    return [get_content(get_html(url)).find('time').text,
            get_content(get_html(url)).find('h1').text,
            get_content(get_html(url)).find('div', class_='r24_text').text]


quotes = get_content(get_html(URL)).find_all('a', class_='r24_url')

for s in quotes:
    g = str(s)
    u = g[g.find('href="https://russia24.pro'):g.find('href="https://russia24.pro') + 37]
    if not u[-1].isdigit() and not u[-1].isalpha() and u[-2].isdigit():
        search_url.append(u[6:])

print('Всего', len(search_url), 'новостей:\n')

for el in search_url:
    cnt += 1
    print(cnt, 'новость.')
    print(*new(el))
    print('\n')
