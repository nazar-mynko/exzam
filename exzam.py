from bs4 import BeautifulSoup   # модуль для парсінга
import requests                 # модуль для парсінга
import re           #модуль для роботи з текстом

def scrape_videos(url):

    req = requests.get(url)     #тіло сторінки
    send = BeautifulSoup(req.text, "html.parser")                  #отримуєм теги скріпт
    search = send.find_all("script")                               #формуємо всі символи
    key = '"videold":"'
    date = re.findall(key + r"([^*]{11})", str(search))           #шукає все по ключу відео айді (11 томущо айді відео на ютуб з 11знаків)

    return data

def scrape_lists(url):

    req = requests.get(url)                                      #таке саме  але шукає плей ліст айді
    send = BeautifulSoup(req.text, "html.parser")
    search = send.find_all("script")
    key = '"playlistId":"'
    data = re.findall(key + r"([^*]{34})", str(search))          #(34 томущо айді плейлистів з 34знаків)

    return data

if __name__ == "__exzam.py__":
    url ="https://www.youtube.com/c/smeshariki/playlists"        #який канал ми будемо парсить
    data = scrape_lists(url)
    data = data[::3]                                             #викидує все що не потрібно в наших слоях які ми отримаємо
    data = data[:-2]

    for i in data:
        output = 'https://www.youtube.com/playlist?list=' + i     #формує силки на плей листи
        vid = scrape_videos(output)
        vid = vid[::3]
        vid = vid[:-1]

        for i in vid:
            with open("D:\Python", "a", encoding="utf-8") as files:  #записує всі силки на відео які ми запарсили
                files.write(str('https://www.youtube.com/watch?v=' + i + '\n'))
                print('https://www.youtube.com/watch?v=' + i)
