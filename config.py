import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
START_IMG_URL = getenv("START_IMG_URL")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID"))
PROG_ID = list(map(int, getenv("PROG_ID","833360381").split()))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝙄𝙌 𝙈𝙐𝙎𝙄𝘾 ♥️•")
OWNER_ID = list(map(int, getenv("OWNER_ID", "833360381").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
USER_OWNER = getenv("USER_OWNER","IQ7amo")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/zzzdevo/zz-bot-zz")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MGIMT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/IQSUPP")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999999"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "AgCSxocAAbubmvSeqkLcBlekf-XFcp6vndlF62S-KfwWZ9lUzHeYVcMlPYwIJFFPx1D0dHvleJpNLKykIrKDsWm8V1NQiSFCsLp_cd9Q1h_YTve1ZmwJtxV182OoOyW2qh-bEBZBGhXvUJcLEIqOTqfDS7xA78T66EE5-yu8lOwDm8jZUaiAVe1gMYTio7-LCX1erVcH6zuX4W62QnylDHJ920-A3_tLjTXCJbVYS3lMrSHL_GoT3nIutnllVDa3CYJKvEdFuwG7xgDJAVj3xYJt9Aw29XhuTyIY8SA4fCbyRnOFzHrZM19c43UCMRjaYk-CBXV2iMcOknCbN221nDej9gkwAAAAFu7FdkAA")
STRING2 = getenv("STRING_SESSION2", "AgFPyocANJQ0H_2H-Gno9MTTQDewjgYDhF45CgJeO6L5gpIVU_xvni_Zh4RFP99Ava_ob8w0yhzaT74IMEHwTPeHbx0291KY5lkKE8cq1pcrV6LHxZROERKhWwI6weRAQbmwEnIVrbVsl9ZAYAkXzu8Bvf12phdy-3MSpBJn0XJgmP1zeHjH11_cLie1jEddWEO7Bm08XDPE77K0KETkYdLty6aCigDsrruUAGKcEmHw6jqF7tB_WTwduJ6ZjL6hK0MtW955RpxHSzkQGIJLj48zfR9EcFJ34GqPa081r-8bEMavhNCvGoQ_0zHSY8gsxRaY8xXMxXTm60ZvArlaafalxWfgAAAAFM8cI7AA")
STRING3 = getenv("STRING_SESSION3", "AgCSxocAAbubmvSeqkLcBlekf-XFcp6vndlF62S-KfwWZ9lUzHeYVcMlPYwIJFFPx1D0dHvleJpNLKykIrKDsWm8V1NQiSFCsLp_cd9Q1h_YTve1ZmwJtxV182OoOyW2qh-bEBZBGhXvUJcLEIqOTqfDS7xA78T66EE5-yu8lOwDm8jZUaiAVe1gMYTio7-LCX1erVcH6zuX4W62QnylDHJ920-A3_tLjTXCJbVYS3lMrSHL_GoT3nIutnllVDa3CYJKvEdFuwG7xgDJAVj3xYJt9Aw29XhuTyIY8SA4fCbyRnOFzHrZM19c43UCMRjaYk-CBXV2iMcOknCbN221nDej9gkwAAAAFu7FdkAA")
STRING4 = getenv("STRING_SESSION4", "AgFPyocANJQ0H_2H-Gno9MTTQDewjgYDhF45CgJeO6L5gpIVU_xvni_Zh4RFP99Ava_ob8w0yhzaT74IMEHwTPeHbx0291KY5lkKE8cq1pcrV6LHxZROERKhWwI6weRAQbmwEnIVrbVsl9ZAYAkXzu8Bvf12phdy-3MSpBJn0XJgmP1zeHjH11_cLie1jEddWEO7Bm08XDPE77K0KETkYdLty6aCigDsrruUAGKcEmHw6jqF7tB_WTwduJ6ZjL6hK0MtW955RpxHSzkQGIJLj48zfR9EcFJ34GqPa081r-8bEMavhNCvGoQ_0zHSY8gsxRaY8xXMxXTm60ZvArlaafalxWfgAAAAFM8cI7AA")
STRING5 = getenv("STRING_SESSION5", "AgCSxocAAbubmvSeqkLcBlekf-XFcp6vndlF62S-KfwWZ9lUzHeYVcMlPYwIJFFPx1D0dHvleJpNLKykIrKDsWm8V1NQiSFCsLp_cd9Q1h_YTve1ZmwJtxV182OoOyW2qh-bEBZBGhXvUJcLEIqOTqfDS7xA78T66EE5-yu8lOwDm8jZUaiAVe1gMYTio7-LCX1erVcH6zuX4W62QnylDHJ920-A3_tLjTXCJbVYS3lMrSHL_GoT3nIutnllVDa3CYJKvEdFuwG7xgDJAVj3xYJt9Aw29XhuTyIY8SA4fCbyRnOFzHrZM19c43UCMRjaYk-CBXV2iMcOknCbN221nDej9gkwAAAAFu7FdkAA")

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []



START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/a3352a2148f8ca63da280.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/a3352a2148f8ca63da280.jpg"

STATS_IMG_URL = getenv("https://telegra.ph/file/85f232e0613f9403c4560.jpg")

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)



if MONGO_DB_URI != None:
    MONGO_DB_URI = MONGO_DB_URI.strip()
if MONGO_DB_URI == "":
    MONGO_DB_URI = None
