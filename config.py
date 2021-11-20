import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Dr_Asad_Ali")
ALIVE_NAME = getenv("ALIVE_NAME", "Dr_Asad_Ali")
BOT_USERNAME = getenv("BOT_USERNAME", "AsadSupport")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Music_Asistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Shayri_Music_Lovers")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Give_Me_Heart")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/163e51ab720f0085c53a5.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "400"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://www.youtube.com/c/JankariKiDuniya")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/7169e0ea05e66f0ffd1a2.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/0aec1809fac360415d4cb.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/3234fc59a3c050513de49.jpg")
