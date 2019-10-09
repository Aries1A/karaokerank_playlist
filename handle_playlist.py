from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

import httplib2
import os
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

SCOPES = 'https://www.googleapis.com/auth/youtube'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
    creds = tools.run_flow(flow, store)
YOUTUBE = discovery.build('youtube', 'v3', http=creds.authorize(Http()))
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    http=creds.authorize(httplib2.Http()))

# プレイリスト上の動画Idを取得
def search_playlistitems(Id):
    search_response = youtube.playlistItems().list(
        part="snippet",
        playlistId=Id,
        maxResults=50
    ).execute()

    return [search_response["items"][i]["id"]for i in range(len(search_response["items"]))]

# 動画をプレイリストから削除
def reset_playlist(Id):
    youtube.playlistItems().delete(id=Id).execute()
    # print(reset_response.get("id"))
    print("deleted:{0}".format(Id))

# プレイリストに動画を追加
def insert_resource(playlistId, videoId):
    insert_response = youtube.playlistItems().insert(
        part="snippet",
        body=dict(
            snippet=dict(
                playlistId=playlistId,
                resourceId=dict(
                    kind="youtube#video",
                    videoId=videoId)
            )
        )
    ).execute()

# プレイリストを作成
def create_playlists(category):
    create_response = youtube.playlists().insert(
        part="snippet,status",
        body=dict(
            snippet=dict(
                title="【{0}】週間カラオケランキング".format(category),
                description="DAMのカラオケランキングを元に週に一回自動更新されます"
            ),
            status=dict(
                privacyStatus="Public"
            )
        )
    ).execute()

    return create_response["id"]


if __name__ == "__main__":
    categories = ["洋楽"]
    for i in categories:
        response = create_playlists(i)
        print("{0}: {1}".format(i,response))
