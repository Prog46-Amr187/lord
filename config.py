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
ALIVE_NAME = getenv("ALIVE_NAME", "Give_Me_Heart")
BOT_USERNAME = getenv("BOT_USERNAME", "Give_Me_Heart")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Give_Me_Heart")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Shayri_Music_Lovers")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Give_Me_Heart")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c97bf9418d089092d8429.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/65934171576a9df24346e.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/65934171576a9df24346e.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/65934171576a9df24346e.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/65934171576a9df24346e.jpg")
