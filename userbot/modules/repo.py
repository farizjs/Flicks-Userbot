# FROM Flicks-Userbot
# <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot

import logging

from userbot import BOT_USERNAME, CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import flicks_cmd


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@flicks_cmd(pattern="repo")
async def yardim(event):
    try:
        botusername = BOT_USERNAME
        if botusername is not None:
            results = await event.client.inline_query(botusername, "repo")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Botnya tidak berfungsi! Silahkan atur vars `BOT_TOKEN` dan `BOT_USERNAME` dengan benar.\ntau gunakan perintah `.set var BOT_TOKEN` <token> dan `.set var BOT_USERNAME` <Username Bot mu>."
            )
    except Exception:
        return await event.edit(
            "**__USERBOT INDONESIA__**\n"
            "𝗥𝗲𝗽𝗼 🇮🇩\n"
            "╰⎆ [Flick-Userbot](https://github.com/farizjs/Flicks-Userbot)\n"
            "❏ 𝗢𝘄𝗻𝗲𝗿 ⎆ [Fariz • 🇮🇩](t.me/farizjs)\n"
            "❏ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ⎆ [groups](t.me/FlicksSupport)\n" 
            "❏ 𝗧𝗲𝗮𝗺 ⎆  [click here](t.me/devoloperflicks)\n"
        )

