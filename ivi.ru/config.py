from fake_useragent import UserAgent


user_agent = UserAgent().random
CSV = "cards.csv"
URL = "https://www.ivi.ru/collections/new-movies"
HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': user_agent,
}
