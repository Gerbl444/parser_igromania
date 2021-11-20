import requests
from bs4 import BeautifulSoup

HOST = "https://www.igromania.ru"
URL = "https://www.igromania.ru/games/"
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

def get_html(url):
    req = requests.get(url, headers=HEADERS)
    return req

def get_content(html):
    soup = BeautifulSoup(html, "html.parser")
    contents = soup.find_all("div", class_ = "left-block")
    games = []
    for content in contents:
        games.append (
            {
                'name_game': content.find("a", class_ = "name").get_text(strip=True),
                'link_game': HOST + content.find("a", class_ = "name").get('href')
            }
        )
    return games

def parser():
    html = get_html(URL) #print(get_content(html.text))
    if html.status_code == 200:
        games = []
        count_page = int(input("Сколько страниц парсим? ").strip()) + 1
        count = 1
        for page in range(1, count_page):
            print(f"Парсим страницу: {count}")
            html = get_html(URL + "all/all/all/all/all/0/" + str(page) + "/")
            games.extend(get_content(html.text))
            count = count + 1
        return games
    else:
        print("Произошла ошибка!")

def output():
    pars = parser()
    length = len(pars)
    count_game = 0
    while count_game < length:
        print(pars[count_game]['name_game'] + " " + pars[count_game]['link_game'])
        count_game = count_game + 1

output()