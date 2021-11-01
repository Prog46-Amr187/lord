# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit

import asyncio
import re

from config import BOT_USERNAME, GROUP_SUPPORT, IMG_1, IMG_2, UPDATES_CHANNEL
from rocksdriver.filters import command, other_filters
from rocksdriver.queues import QUEUE, add_to_queue
from rocksdriver.asad import call_py
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:70]
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(command(["play", f"play@{BOT_USERNAME}"]) & other_filters)
async def play(_, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url=f"https://t.me/Dr_Asad_Ali"),
                ],
                [
                    InlineKeyboardButton(
                        "👨‍👨‍👧‍👦 Gʀᴏᴜᴘ 👨‍👨‍👧‍👦", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],
            ]
        )

    replied = m.reply_to_message
    chat_id = m.chat.id
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **Dᴏᴡɴʟᴏᴀᴅɪɴɢ ᴀᴜᴅɪᴏ...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **Sᴏɴɢ ɪs ᴀᴛ ᴡᴀɪᴛɪɴɢ ᴘᴏsɪᴛɪᴏɴ**\n\n🏷 **Name:** [{songname[:15]}]({link})\n🎧 **Request by:** {m.from_user.mention()}\n🔢 **At position »** `{pos}`",
                    reply_markup=keyboard,
                )
            else:
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_2}",
                    caption=f"💡 **Sᴏɴɢ ɪs ᴘʟᴀʏɪɴɢ..**\n\n🏷 **Nᴀᴍᴇ:** [{songname[:15]}]({url})\n💡 **Sᴛᴀᴛᴜs:** `Playing`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}",
                    reply_markup=keyboard,
                )
        else:
            if len(m.command) < 2:
                await m.reply(
                    "» Rᴇᴘʟᴀʏ ᴛᴏ ᴀ **Aᴜᴅɪᴏ Fɪʟᴇ** or **Gɪᴠᴇ ᴍᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.**"
                )
            else:
                suhu = await m.reply("🔎 **Sᴇᴀʀᴄʜɪɴɢ...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **Nᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ.**")
                else:
                    songname = search[0]
                    url = search[1]
                    asad, ytlink = await ytdl(url)
                    if asad == 0:
                        await suhu.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Audio", 0
                            )
                            await suhu.delete()
                            await m.reply_photo(
                                photo=f"{IMG_1}",
                                caption=f"💡 **Sᴏɴɢ ɪs ᴀᴛ ᴡᴀɪᴛɪɴɢ ᴘᴏsɪᴛɪᴏɴ**\n\n🏷 **Name:** [{songname[:15]}]({url})\n💭 **Cʜᴀᴛ:** `{chat_id}`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}\n🔢 **Pᴏsɪᴛɪᴏɴ »** `{pos}`",
                                reply_markup=keyboard,
                            )
                        else:
                            try:
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                    ),
                                    stream_type=StreamType().pulse_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                                await suhu.delete()
                                await m.reply_photo(
                                    photo=f"{IMG_2}",
                                    caption=f"💡 **Sᴏɴɢ ɪs ᴘʟᴀʏɪɴɢ..**\n\n🏷 **Nᴀᴍᴇ:** [{songname[:15]}]({url})\n💡 **Sᴛᴀᴛᴜs:** `Playing`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await m.reply_text(f"🚫 Eʀʀᴏʀ: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "» Rᴇᴘʟᴀʏ ᴛᴏ ᴀ **Aᴜᴅɪᴏ Fɪʟᴇ** or **Gɪᴠᴇ ᴍᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.**"
            )
        else:
            suhu = await m.reply("🔎 **Sᴇᴀʀᴄʜɪɴɢ...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("❌ **Nᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ.**")
            else:
                songname = search[0]
                url = search[1]
                asad, ytlink = await ytdl(url)
                if asad == 0:
                    await suhu.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        await m.reply_photo(
                            photo=f"{IMG_1}",
                            caption=f"💡 **Sᴏɴɢ ɪs ᴀᴛ ᴡᴀɪᴛɪɴɢ ᴘᴏsɪᴛɪᴏɴ**\n\n🏷 **Name:** [{songname[:15]}]({url})\n💭 **Cʜᴀᴛ:** `{chat_id}`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}\n🔢 **Pᴏsɪᴛɪᴏɴ »** `{pos}`",
                                reply_markup=keyboard,
                        )
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await suhu.delete()
                            await m.reply_photo(
                                photo=f"{IMG_2}",
                                caption=f"💡 **Sᴏɴɢ ɪs ᴇɴᴅᴇᴅ.**\n\n🏷 **Nᴀᴍᴇ:** [{songname[:15]}]({url})\n💡 **Sᴛᴀᴛᴜs:** `Playing`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await m.reply_text(f"🚫 Eʀʀᴏʀ: `{ep}`")


# stream is used for live streaming only 

@Client.on_message(command(["stream", f"stream@{BOT_USERNAME}"]) & other_filters)
async def stream(_, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url=f"https://t.me/Dr_Asad_Ali"),
                ],
                [
                    InlineKeyboardButton(
                        "👨‍👨‍👧‍👦 Gʀᴏᴜᴘ 👨‍👨‍👧‍👦", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],
            ]
        )

    chat_id = m.chat.id
    if len(m.command) < 2:
        await m.reply("» give me a live-link/m3u8 url/youtube link to stream.")
    else:
        link = m.text.split(None, 1)[1]
        suhu = await m.reply("🔄 **Pʀᴏᴄᴇss sᴛʀᴇᴀᴍɪɴɢ...**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            asad, livelink = await ytdl(link)
        else:
            livelink = link
            asad = 1

        if asad == 0:
            await suhu.edit(f"❌ **yt-dl ɪssᴜᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ**\n\n» `{ytlink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **Sᴏɴɢ ɪs ᴀᴛ ᴡᴀɪᴛɪɴɢ ᴘᴏsɪᴛɪᴏɴ**\n\n🏷 **Name:** [{songname[:15]}]({url})\n💭 **Cʜᴀᴛ:** `{chat_id}`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}\n🔢 **Pᴏsɪᴛɪᴏɴ »** `{pos}`",
                    eply_markup=keyboard,
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            livelink,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(chat_id, "Radio", livelink, link, "Audio", 0)
                    await suhu.delete()
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        caption=f"💡 **[Radio live]({link}) sᴛʀᴇᴀᴍ sᴛᴀʀᴛɪɴɢ.**\n\n🏷 **Nᴀᴍᴇ:** [{songname[:15]}]({url})\n💡 **Sᴛᴀᴛᴜs:** `Playing`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}",
                                    reply_markup=keyboard,
                    )
                except Exception as ep:
                    await m.reply_text(f"🚫 error: `{ep}`")
