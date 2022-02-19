# © t.me/farizsj
# From https://github.com/farizjs/Flicks-Userbot <Flicks-Userbot>
# Dont Remove Credits

from telethon.tl.types import ChannelParticipantsAdmins
import os, logging, asyncio
from telethon import Button
from userbot import bot, tgbot
from userbot.utils import asst_cmd
from telethon import events

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)


saya = bot.get_me()
OWNER_ID = saya.id

# if userbot doesn't have asst_cmd
# @tgbot.on(events.NewMessage(pattern="^/mentionall ?(.*)", from_users=OWNER_ID))
# -------------------------------------------------------------------------------

@asst_cmd(pattern=r"^/mentionall ?(.*)", from_users=OWNER_ID)
async def mentionall(event):
  if event.is_private:
    return await event.respond("__Perintah ini hanya dapat digunakan dalam grup dan channel!__")
  
  admins = []
  async for admin in tgbot.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__Hanya admin yang bisa mention all!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Saya tidak bisa menyebut anggota untuk pesan lama! (pesan yang dikirim sebelum saya ditambahkan ke grup)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Beri saya satu argumen!__")
  else:
    return await event.respond("__Balas pesan atau beri saya teks untuk menyebut orang lain!__")
  
  if mode == "text_on_cmd":
    usrnum = 0
    usrtxt = ""
    async for usr in tgbot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await tgbot.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    usrnum = 0
    usrtxt = ""
    async for usr in tgbot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await tgbot.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
