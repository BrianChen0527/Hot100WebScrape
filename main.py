import requests
from bs4 import BeautifulSoup
import re
from datetime import date, timedelta

def find_weekly_hot_songs(n,url):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    song_elements = soup.select(".chart-element__information__song.text--truncate.color--primary")
    song_elements = str(song_elements)
    songs_set = set()
    for i in range(n):
        start = song_elements.find("\">") + len("\">")
        end = song_elements.find("</span>")
        song = song_elements[start:end]
        songs_set.add(song)
        song_elements = song_elements[end:]
    return songs_set

def allsundays(weeks, day):
    d = date.fromisoformat(day)
    d += timedelta(days = (5 - d.weekday() + 7) % 7)  # First Sunday
    sundays = []
    for i in range(weeks):
        sundays.append(str(d))
        d += timedelta(days = 7)
    return sundays


if __name__ == '__main__':
    start_day = "2020-01-01"
    weeks = 10
    URL = "https://www.billboard.com/charts/hot-100/"
    n = 5
    all_songs_list = set()
    week_dates = allsundays(weeks, start_day)

    for sundays in week_dates:
        weekly_URL = URL + sundays
        print(weekly_URL)
        songs_list = find_weekly_hot_songs(n, weekly_URL)
        print(songs_list)
        all_songs_list = set.union(all_songs_list, songs_list)

    print(all_songs_list)













