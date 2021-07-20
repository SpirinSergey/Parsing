from fake_useragent import UserAgent

URL = 'https://russia24.pro/'
user_agent = UserAgent().random
HEADERS = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': user_agent,
    'Content-Type': 'text/json'
}
search_url = []
cnt = 0
