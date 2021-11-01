# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit

from config import BOT_USERNAME
from pyrogram.types import Message
from rocksdriver.filters import command, other_filters
from pyrogram import Client, filters
from rocksdriver.queues import QUEUE, get_queue


@Client.on_message(command(["playlist", f"playlist@{BOT_USERNAME}", "queue", f"queue@{BOT_USERNAME}"]) & other_filters)
async def playlist(client, m: Message):
   chat_id = m.chat.id
   if chat_id in QUEUE:
      chat_queue = get_queue(chat_id)
      if len(chat_queue)==1:
         await m.reply(f"💡 **[Nᴏᴡ ᴘʟᴀʏɪɴɢ](https://t.me/Give_Me_Heart)**\n\n[{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}`", disable_web_page_preview=True)
      else:
         QUE = f"💡 **[Nᴏᴡ ᴘʟᴀʏɪɴɢ](https://t.me/Dr_Asad_Ali)**\n\n[{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}` \n\n**📖 Pʟᴀʏʟɪsᴛ:**"
         l = len(chat_queue)
         for x in range (1, l):
            han = chat_queue[x][0]
            hok = chat_queue[x][2]
            hap = chat_queue[x][3]
            QUE = QUE + "\n" + f"**#{x}** - [{han}]({hok}) | `{hap}`"
         await m.reply(QUE, disable_web_page_preview=True)
   else:
      await m.reply("❄1�71ￄ1�77 **Nᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ.**")
