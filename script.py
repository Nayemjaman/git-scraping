from bs4 import BeautifulSoup
import requests
import json
import datetime
import os
# import twint
import pathlib


DATE_START = str(datetime.datetime.today().date() - datetime.timedelta(days=1))
DATA_PATH = pathlib.Path("data/")
DATA_PATH.mkdir(parents=True, exist_ok=True)

HASHTAG = 'play'
JSON_FILENAME = DATA_PATH / str(datetime.datetime.today().date())

headers = {
        'authority': 'www.skysports.com/',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

url = 'https://www.skysports.com/football/news'
r = requests.get(url, headers=headers).text
soup = BeautifulSoup(r,'html.parser')

latest_title = soup.find('a', class_="news-list__headline-link").text
os.system(f'snscrape --jsonl --progress --since {DATE_START} twitter-hashtag "{HASHTAG}" > {JSON_FILENAME}.json')
print(latest_title)







