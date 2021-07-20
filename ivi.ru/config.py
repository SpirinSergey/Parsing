from fake_useragent import UserAgent

URL = "https://www.ivi.ru/collections/new-movies"
user_agent = UserAgent().random
HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': user_agent,
}
CSV = "cards.csv"
