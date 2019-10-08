from karaokerank import get_karaokerank
from search import youtube_search
from handle_playlist import insert_resource,reset_playlist,search_playlistitems
import datetime
import calendar
import settings

video_nums = {
0:50, #総合
1:50, #急上昇
2:30, #アニメ
3:30, #ボカロ
4:30, #洋楽
}

urls = {
0:"https://www.clubdam.com/app/dam/ranking/total-weekly.html",
1:"https://www.clubdam.com/app/dam/ranking/burst-daily.html",
2:"https://www.clubdam.com/app/dam/ranking/animation-weekly.html",
3:"https://www.clubdam.com/app/dam/ranking/vocaloid-weekly.html",
4:"https://www.clubdam.com/app/dam/ranking/yougaku-weekly.html"
}

ids = {
0:settings.ID_ALL,
1:settings.ID_HOT,
2:settings.ID_ANIME,
3:settings.ID_VOCALO,
4:settings.ID_WESTERN
}

weekday_categories = {
# 0:月曜日,プレイリストのリセットは1,-1を入れて実行
0:[0],
1:[1],
2:[2],
3:[1],
4:[3],
5:[1],
6:[4],
-1:[1]
}


#今日の曜日を取得
weekday = datetime.date.today().weekday()
weekday_name = calendar.day_name[weekday]
print(weekday_name)

for category in weekday_categories[weekday]: #今日更新するプレイリストの番号
    #更新前のプレイリストを全削除
    Items = search_playlistitems(ids[category])
    for resourceId in Items:
        reset_playlist(resourceId)
    #カラオケランキングを取得
    titles,artists = get_karaokerank(url=urls[category],video_num=video_nums[category])
    #youtbeで動画を検索
    for rank in range(len(titles)):
        videoid = youtube_search(video_title=titles[rank] + artists[rank])
        #プレイリストに追加
        if videoid is not None:
            insert_resource(ids[category],videoid)
