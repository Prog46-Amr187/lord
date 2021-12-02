import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "JAI6H")
ALIVE_NAME = getenv("ALIVE_NAME", "Amrjava")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GI18H")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsadSupport")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8f59f7e12b0e1142f8458.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "400"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/jankarikiduniya/Dr-Music-Video-Streaming")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/b056d094c11d7a05a4b28.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/1bce08290be5167ee5ffc.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/b056d094c11d7a05a4b28.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/b056d094c11d7a05a4b28.jpg")

# Don't Change It Bro ❣️ 😂


MY_SERVER = getenv("MY_SERVER", "GI18H")
REPO_OWNER = getenv("REPO_OWNER", "Prog46-Amr187/Music")
MY_HEART = getenv("MY_HEART", "uu_ak0")
BOT_UPDATE = getenv("BOT_UPDATE", "ct_gold")
MY_BRO = getenv("MY_BRO", "JAI6H")
