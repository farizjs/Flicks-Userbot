# https://github.com/fjgaming212/Flicks-Userbot
# Jan dihapus ya :)
# Kalo mau ambil aja :D

import logging

from userbot import BOT_USERNAME, CMD_HELP
from userbot.events import register

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@register(outgoing=True, pattern=r"^\.xrepo")
async def yardim(event):
    try:
        kenbotusername = BOT_USERNAME
        if kenbotusername is not None:
            results = await event.client.inline_query(kenbotusername, "@InfoFlicksUserbot")
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
            "**Anda tidak dapat mengirim inline menu dalam obrolan ini, silakan gunakan perintah** `.inlineon`"
        )


CMD_HELP.update(
    {
        "inlinebot": "** Plugin :** inlinebot\
        \n\n  •  Perintah : `.helpme`\
        \n  •  Function : Untuk menu bantuan modul Flicks-Userbot\
        \n\n  •  Perintah : `.xrepo`\
        \n  •  Function : Repo Flicks-Userbot\
        \n\n  •  Perintah : `.aboutflicks`\
        \n  •  Function : Tentang Flicks-Userbot\
        \n\n  •  Perintah : `.tutorial`\
        \n  •  Function : Tutorial memasang Flicks-Userbot\

    "
    }
)
