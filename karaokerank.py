# coding: UTF-8
from urllib import request
from bs4 import BeautifulSoup

def get_karaokerank(url,video_num=10):
    instance = request.urlopen(url)
    soup = BeautifulSoup(instance, "html.parser")

    # DAMのカラオケランキングページから曲名と歌手名を取得
    titles = [soup.select_one("body > div.l-page.ranking > div.l-container > div.l-main.no-js > div.l-section.main-contents > div.l-inner > div.l-ranking-container-wrap > div > div > ol > li:nth-child({0}) > div.ranking-item-inner.is-pc > a.title > p > span".format(i+1)).text for i in range(video_num)]
    artists = [soup.select_one("body > div.l-page.ranking > div.l-container > div.l-main.no-js > div.l-section.main-contents > div.l-inner > div.l-ranking-container-wrap > div > div > ol > li:nth-child({0}) > div.ranking-item-inner.is-pc > a.artist > p".format(i+1)).text for i in range(video_num)]

    return titles,artists
