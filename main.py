import discord
from discord.ext import commands
from youtube_api import get_video_data
from config import VIDEOS
import os
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GOALS_FILE = "goals.json"

def load_goals():
    if os.path.exists(GOALS_FILE):
        with open(GOALS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_goals(goals):
    with open(GOALS_FILE, "w") as f:
        json.dump(goals, f, indent=2)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready: {bot.user.name}")
    await send_video_updates()
    await bot.close()  # ✅ 処理が終わったら終了

async def send_video_updates():
    goals_reached = load_goals()

    for video in VIDEOS:
        video_id = video["video_id"]
        channel_id = video["channel_id"]
        base_goal = video.get("goal", 1000000)

        view_count, title, thumbnail_url = get_video_data(video_id)
        if view_count is None:
            print(f"再生回数の取得に失敗しました: {video_id}")
            continue

        current_goal = goals_reached.get(video_id, base_goal)
        new_goal = (view_count // 1000000) * 1000000

        embed = discord.Embed(
            title=f"📺 {title}",
            description=f"再生回数: **{view_count:,} 回**",
            color=0xff69b4
        )
        embed.set_thumbnail(url=thumbnail_url)
        embed.add_field(name="動画リンク", value=f"https://www.youtube.com/watch?v={video_id}", inline=False)

        if new_goal > current_goal:
            embed.add_field(name="🎉 達成！", value=f"目標 {new_goal:,} 回を超えました！おめでとう！", inline=False)
            goals_reached[video_id] = new_goal

        channel = bot.get_channel(channel_id)
        if channel:
            await channel.send(embed=embed)
        else:
            print(f"チャンネルが見つかりません: {channel_id}")

    save_goals(goals_reached)

bot.run(TOKEN)
