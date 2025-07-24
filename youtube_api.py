import os
import requests
from dotenv import load_dotenv

API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_video_data(video_id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "id": video_id,
        "key": API_KEY,
        "part": "snippet,statistics"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("APIエラー:", response.text)
        return None, None, None

    data = response.json()
    if not data["items"]:
        return None, None, None

    item = data["items"][0]
    title = item["snippet"]["title"]
    view_count = int(item["statistics"]["viewCount"])
    thumbnail_url = item["snippet"]["thumbnails"]["high"]["url"]

    return view_count, title, thumbnail_url
