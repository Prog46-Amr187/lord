# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit



from config import BOT_USERNAME, MY_HEART, MY_SERVER
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from pyrogram import Client, filters
from rocksdriver.queues import QUEUE, get_queue
from rocksdriver.filters import command, other_filters


keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 Close", callback_data="cls")]]
)


@Client.on_message(command(["playlist", f"playlist@{BOT_USERNAME}", "queue", f"queue@{BOT_USERNAME}"]) & other_filters)
async def playlist(client, m: Message):
   chat_id = m.chat.id
   if chat_id in QUEUE:
      chat_queue = get_queue(chat_id)
      if len(chat_queue)==1:
         await m.reply(f"🎼 **[Now Play](https://t.me/AKJA0)**\n\n[{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}`", disable_web_page_preview=True)
      else:
         QUE = f"🍄 **[Waiting At Rocks](https://t.me/JAI6H)**\n\n[{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}` \n\n**📖 Playlist:**"
         l = len(chat_queue)
         for x in range (1, l):
            han = chat_queue[x][0]
            hok = chat_queue[x][2]
            hap = chat_queue[x][3]
            QUE = QUE + "\n" + f"**#{x}** - [{han}]({hok}) | `{hap}`"
         await m.reply(QUE, reply_markup=keyboard, disable_web_page_preview=True)
   else:
      await m.reply("❄ **Nothing is currently playing.**")