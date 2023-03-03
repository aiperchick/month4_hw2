import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://doramy.club/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='post-home')
    doramy_club = []

    for item in items:
        doramy_club.append(
            {
                'name': URL + item.find('a').get('href'),
                'series': item.find('td', class_='naz').get_text(),
                'country': item.find('td', class_='naz').get_text(),
                'genre': item.find('td', class_='naz').get_text(),
                'status': item.find('div', class_='status')
            })

    return doramy_club


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        doramy_club1 = []
        for page in range(0, 1):
            html = get_html(f'https://doramy.club/', params=page)
            doramy_club1.extend(get_data(html.text))
        return doramy_club1
        # print(f'\n{doramy_club1}\n')
    else:
        raise Exception('Parser Error......')


parser()
