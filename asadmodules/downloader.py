# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit


from __future__ import unicode_literals

import asyncio
import math
import os
import time
from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import requests
import wget
import yt_dlp
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from config import BOT_USERNAME, REPO_OWNER as bn
from rocksdriver.decorators import humanbytes
from rocksdriver.filters import command, other_filters


ydl_opts = {
    'format': 'best',
    'keepvideo': True,
    'prefer_ffmpeg': False,
    'geo_bypass': True,
    'outtmpl': '%(title)s.%(ext)s',
    'quite': True
}


@Client.on_message(command(["song", f"song@{bn}"]) & ~filters.edited)
def song(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("🔎 **𝕱𝖎𝖓𝖉𝖎𝖓𝖌 𝖘𝖔𝖓𝖌**...")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("❌ 𝕾𝖔𝖓𝖌 𝖓𝖔𝖙 𝖋𝖔𝖚𝖓𝖉.\n\n𝕻𝖑𝖊𝖆𝖘𝖊 𝖊𝖓𝖙𝖊𝖗 𝖈𝖔𝖗𝖗𝖊𝖈𝖙 𝖘𝖔𝖓𝖌 𝖓𝖆𝖒𝖊.")
        print(str(e))
        return
    m.edit("📥 𝕯𝖔𝖜𝖓𝖑𝖔𝖆𝖉𝖎𝖓𝖌 𝖋𝖎𝖑𝖊...")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**🎧 𝖀𝖕𝖑𝖔𝖆𝖉𝖊𝖗 [ᴋɪɴɢ](https://t.me/{REPO_OWNER})**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("📤 𝖀𝖕𝖑𝖔𝖆𝖉𝖎𝖓𝖌 𝖋𝖎𝖑𝖊...")
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("❌ 𝕰𝖗𝖗𝖔𝖗")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@Client.on_message(
    command(["vsong", f"vsong@{bn}", "video", f"video@{bn}"]) & ~filters.edited
)
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("📥 **𝕯𝖔𝖜𝖓𝖑𝖔𝖆𝖉𝖎𝖓𝖌 𝖛𝖎𝖉𝖊𝖔...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **𝕰𝖗𝖗𝖔𝖗:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("📤 **𝖀𝖕𝖑𝖔𝖆𝖉𝖎𝖓𝖌 𝖛𝖎𝖉𝖊𝖔...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)


@Client.on_message(command(["lyric", f"lyric@{bn}"]))
async def lyrics(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("» **𝕲𝖎𝖛𝖊 𝖑𝖞𝖗𝖎𝖈𝖘 𝖓𝖆𝖒𝖊 𝖙𝖔.**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("🔎 **𝕾𝖊𝖆𝖗𝖈𝖍𝖎𝖓𝖌 𝖑𝖞𝖗𝖎𝖈𝖘...**")
        resp = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit("❌ **𝕷𝖞𝖗𝖎𝖈𝖘 𝖓𝖔𝖙 𝖋𝖔𝖚𝖓𝖉.**\n\n» **𝕻𝖑𝖊𝖆𝖘𝖊 𝖊𝖓𝖙𝖊𝖗 𝖛𝖆𝖑𝖎𝖉 𝖓𝖆𝖒𝖊...**")