# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **Welcome {message.from_user.mention} Sweet Heart How Are You!** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Aɢᴀʀ ᴀᴘᴋᴏ ᴠᴄ ᴘᴇʏ sᴏɴɢ ᴘʟᴀʏ ᴋᴀʀɴᴇʏ ʜᴀɪɴ ᴛᴏ ᴍᴜᴊʜᴇʏ ᴀᴘɴᴇʏ ɢʀᴏᴜᴘ ᴍᴀɪɴ ʙᴀɴᴀ ᴅᴏ ᴠᴄ ʀɪɢʜᴛ ᴋᴇʏ sᴀᴛʜ ᴀᴜʀ /play ᴋɪ ᴄᴏᴍᴍᴀɴᴅ ᴅᴀʟᴀɪɴ ᴀɢᴀʀ ғɪʀ ʙʜɪ ɪssᴜ ʜᴀɪ ᴛᴏ ᴍᴇʀʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ sᴇʏ ᴄᴏɴᴛᴀᴄᴛ ᴋᴀʀᴀɪɴ 👉 @Dr_Asad_Ali!.**

 👨‍🔧 **Tʜɪs ᴡɪʟʟ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴍᴜsɪᴄ ᴏɴ ʏᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠᴄ ᴄʜᴀᴛ ᴀɴʏ ɪssᴜᴇ ᴄᴏɴᴛᴀᴄᴛ @@HarshitSharma361**

💡 **Find ᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜɪs ʙᴜᴛᴛᴏɴ..👉 » 📚 Cᴏᴍᴍᴀɴᴅs Bᴜᴛᴛᴏɴ 📚 **

❔ **How ᴛᴏ ᴜsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜɪs ʙᴜᴛᴛᴏɴ...👉  » ❓ Bᴀsɪᴄ Gᴜɪᴅᴇ Button!**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ Gʀᴏᴜᴘ ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("Bᴀsɪᴄ Gᴜɪᴅᴇ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Cᴏᴍᴍᴀɴᴅs︎ 📚", callback_data="cbcmds"),
                    InlineKeyboardButton("💝 Oᴡɴᴇʀ 💝", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Gʀᴏᴜᴘ 👥︎", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Cʜᴀɴɴᴇʟ 📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👑 Kɪɴɢ 👑", url="https://t.me/Dr_Asad_Ali"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**
6.) **Join @Shayri_Music_Lovers Give Me Heart @Give_Me_Heart**
📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @Give_Me_Heart**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.

@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Hello {message.from_user.mention} Sᴡᴇᴇᴛ Hᴇᴀʀᴛ ❤️ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ !</b>

**Yᴏᴜ ᴄᴀɴ ғɪɴᴅ ʜᴇʀᴇ sᴇᴠᴇʀᴀʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜ ʙʀɪᴇғ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ 👇**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Bᴀsɪᴄ Cᴍᴅ 📚", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 Aᴅᴠᴀɴᴄᴇᴅ Cᴍᴅ 📕", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 Aᴅᴍɪɴ Cᴍᴅ 📘", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 Sᴜᴅᴏ Cᴍᴅ 📗", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 Oᴡɴᴇʀ Cᴍᴅ 📙", callback_data="cbowner")],
                [InlineKeyboardButton("📔 Fᴜɴ Cᴍᴅ 📔", callback_data="cbfun")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Hᴇʀᴇ ɪs ᴛʜᴇ  [Asᴀᴅ ᴀʟɪ sᴇʀᴠᴇʀ](https://t.me/Give_Me_Heart) ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅ:

» /play (song name/link) - play music on video chat
» /stream (query/link) - stream the yt live/radio live music
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Hᴇʀᴇ ɪs ᴛʜᴇ  [Asᴀᴅ ᴀʟɪ sᴇʀᴠᴇʀ](https://t.me/Give_Me_Heart) ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅ:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Hᴇʀᴇ ɪs ᴛʜᴇ  [Asᴀᴅ ᴀʟɪ sᴇʀᴠᴇʀ](https://t.me/Give_Me_Heart) sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅ:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
