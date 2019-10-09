#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import settings

DEVELOPER_KEY = settings.DEVELOPER_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(video_title):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    # video_titleでyoutube動画検索
    search_response = youtube.search().list(
        q=video_title,
        part="id,snippet",
        maxResults=10
    ).execute()

    # responseから動画のIdを取得
    videos = []
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result["id"]["videoId"])
    try:
        videoid = videos[0]
        return videoid
        print(videoid)
    except KeyError:
        return None
        print("None")


if __name__ == "__main__":
    try:
        videoid = youtube_search("Pretender")
    except HttpError:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
