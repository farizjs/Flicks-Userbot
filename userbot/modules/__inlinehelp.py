import logging

from userbot import BOT_USERNAME, BOT_TOKEN
from telethon.errors.rpcerrorlist import BotInlineDisabledError
from userbot.utils import flicks_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@flicks_cmd(pattern="helpme")
async def yardim(event):
    flicksbotusername = BOT_USERNAME
    if flicksbotusername and BOT_TOKEN:
        try:
            results = await event.client.inline_query(
                flicksbotusername, "@FlicksSupport"
            )
        except BotInlineDisabledError:
            return await event.edit(
                "`Bot tidak dapat digunakan dalam mode sebaris\nPastikan untuk mengaktifkan mode sebaris!`"
            )
        await results[0].click(
            event.chat_id, reply_to=event.reply_to_msg_id, hide_via=False
        )
        await event.delete()
    else:
        return await event.edit(
            "`Botnya tidak berfungsi! Silakan atur Bot Token dan Nama Pengguna dengan benar`"
            "\n`Plugin telah dihentikan`"
        )
