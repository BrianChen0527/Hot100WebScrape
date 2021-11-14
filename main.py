import requests
from bs4 import BeautifulSoup
import re
from datetime import date, timedelta
import multiprocessing as mp

def find_weekly_hot_songs(n,url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    song_elements = soup.select(".chart-element__information__song.text--truncate.color--primary")
    song_elements = str(song_elements)
    songs_set = set()
    for i in range(n):
        start = song_elements.find("\">") + len("\">")
        end = song_elements.find("</span>")
        song = song_elements[start:end]
        songs_set.add(song)
        song_elements = song_elements[end+1:]
    return songs_set

def allsundays(weeks, day):
    d = date.fromisoformat(day)
    d += timedelta(days = (5 - d.weekday() + 7) % 7)  # First Sunday
    sundays = []
    for i in range(weeks):
        sundays.append(str(d))
        d += timedelta(days = 7)
    return sundays

def collect_result(result):
    global all_songs
    print(type(result))
    for song in result:
        all_songs_set.add(song)


if __name__ == '__main__':
    # parallel processing
    pool = mp.Pool(mp.cpu_count())
    all_songs_set = set()
    all_songs = []
    URL = "https://www.billboard.com/charts/hot-100/"
    start_day = input("Enter start date in format yyyy-mm-dd: ")
    weeks = input("How many consecutive weeks to record: ")
    weeks = int(weeks)
    n = input("Record the top # songs each week: ")
    n = int(n)
    week_dates = allsundays(weeks, start_day)

    for sundays in week_dates:
        print("[+] Adding songs from the week of " + sundays + "...")
        weekly_URL = URL + sundays
        pool.apply_async(find_weekly_hot_songs, args=(n, weekly_URL), callback=collect_result)

    pool.close()
    pool.join()

    for song in all_songs_set:
        print(song)
