# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit
# 💔༆ _🅡🅾 C⃤🅚🅢_ԹՏԹԺ ༄🇵🇰 【Usᴇʀ_ᴅɪᴇᴅ】






from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
    REPO_OWNER,
    MY_BRO,
    MY_SERVER,
    BOT_UPDATE,
)
from asadmodules import __version__
from rocksdriver.asad import user
from rocksdriver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.

@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **Welcome {message.from_user.mention} Sweet Heart How Are You!** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Aɢᴀʀ ᴀᴘᴋᴏ ᴠᴄ ᴘᴇʏ sᴏɴɢ ᴘʟᴀʏ ᴋᴀʀɴᴇʏ ʜᴀɪɴ ᴛᴏ ᴍᴜᴊʜᴇʏ ᴀᴘɴᴇʏ ɢʀᴏᴜᴘ ᴍᴀɪɴ ᴀᴅᴍɪɴ ʙᴀɴᴀ ᴅᴏ ᴠᴄ ʀɪɢʜᴛ ᴋᴇʏ sᴀᴛʜ ᴀᴜʀ /join ᴋɪ ᴄᴏᴍᴍᴀɴᴅ ᴅᴀʟᴀɪɴ ᴀɢᴀʀ ғɪʀ ʙʜɪ ɪssᴜ ʜᴀɪ ᴛᴏ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ 👉 [ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/{REPO_OWNER}) ᴏʀ [ᴅᴇᴠᴇʟᴏᴘᴇʀ ʙʀᴏ](https://t.me/{MY_BRO})**

 👨‍🔧 **Tʜɪs ᴡɪʟʟ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴏɴʟʏ ᴠɪᴅᴇᴏ ᴍᴜsɪᴄ ᴏɴ ʏᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠᴄ ᴄʜᴀᴛ ɢʀᴏᴜᴘ**

💡 **Find ᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜɪs ʙᴜᴛᴛᴏɴ. ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ᴀɴᴅ @HarshitSharma361 .👉 » 📚 Cᴏᴍᴍᴀɴᴅs Bᴜᴛᴛᴏɴ 📚 **

❔ **How ᴛᴏ ᴜsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜɪs ʙᴜᴛᴛᴏɴ...👉  » ❓ Bᴀsɪᴄ Gᴜɪᴅᴇ Button!** 
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⚙️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("👩‍💻 ʙᴀsɪᴄ Gᴜɪᴅᴇ👩‍💻 ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 ᴜᴘᴅᴀᴛᴇs 📚", url=f"https://t.me/{BOT_UPDATE}"),
                    InlineKeyboardButton("💝 ᴏᴡɴᴇʀ 💝", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 ɢʀᴏᴜᴘ 👥︎", url=f"https://t.me/{GROUP_SUPPORT}"),
                    InlineKeyboardButton(
                        "📣 cʜᴀɴɴᴇʟ 📣", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(
                        "👑 kɪɴɢ 👑", url="https://t.me/Dr_Asad_Ali"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Group", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "📣 Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hᴇʟʟᴏ {message.from_user.mention()}, ɪ'ᴍ {BOT_NAME}**\n\n✨ Bᴏᴛ ɪs ᴡᴏʀᴋɪɴɢ ɴᴏʀᴍᴀʟʟʏ\n🍀 Mʏ Mᴀsᴛᴇʀ: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n✨ Bᴏᴛ Vᴇʀsɪᴏɴ: `v{__version__}`\n🍀 Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ: `{pyrover}`\n✨ Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ: `{__python_version__}`\n🍀 PʏTɢCᴀʟʟs ᴠᴇʀsɪᴏɴ: `{pytover.__version__}`\n✨ Uᴘᴛɪᴍᴇ Sᴛᴀᴛᴜs: `{uptime}`\n\n**Tʜᴀɴᴋs ғᴏʀ Aᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ, ғᴏʀ ᴘʟᴀʏɪɴɢ ᴠɪᴅᴇᴏ & ᴍᴜsɪᴄ ᴏɴ ʏᴏᴜʀ Gʀᴏᴜᴘ's ᴠɪᴅᴇᴏ ᴄʜᴀᴛ** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")
    
    
@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("**ɢᴇᴛᴛɪɴɢ ʜᴇʟᴘ ᴍᴇɴᴜ**...")
    delta_ping = time() - start
    await m_reply.edit_text("⚡ **ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ**\n⚡️ **ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ**\n⚡ **ᴀғᴛᴇʀ ᴀᴅᴍɪɴ ʀᴜɴ /join ᴄᴏᴍᴍᴀɴᴅ**\n⚡ **ᴛᴜʀɴᴇᴅ ᴏɴ ᴠᴄ ᴛʜᴇɴ ʀᴜɴ /play ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ sᴏɴɢ ɴᴀᴍᴇ**\n⚡ **ᴊᴏɪɴ** @Shayri_Music_Lovers\n**ʟᴏᴠᴇ ʏᴏᴜ ᴀʟʟ ❤️❤️**")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )