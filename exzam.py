from bs4 import BeautifulSoup
import requests
import re

def scrape_videos(url):

    req = requests.get(url)
    send = BeautifulSoup(req.text, "html.parser")
    search = send.find_all("script")
    key = '"videold":"'
    date = re.findall(key + r"([^*]{11})", str(search))

    return data

def scrape_lists(url):

    req = requests.get(url)
    send = BeautifulSoup(req.text, "html.parser")
    search = send.find_all("script")
    key = '"playlistId":"'
    data = re.findall(key + r"([^*]{34})", str(search))

    return data

if __name__ == "__exzam.py__":
    url ="https://www.youtube.com/watch?v="
    data = scrape_lists(url)
    data = data[::3]
    data = data[:-2]

    for i in data:
        output = 'https://www.youtube.com/c/smeshariki/playlists' + i
        vid = scrape_videos(output)
        vid = vid[::3]
        vid = vid[:-1]

        for i in vid:
            with open("D:\Python", "a", encoding="utf-8") as files:
                files.write(str('https://www.youtube.com/watch?v='))
                print('https://www.youtube.com/watch?v=' + i)
