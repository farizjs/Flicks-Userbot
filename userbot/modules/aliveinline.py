import logging

from userbot import BOT_USERNAME
from userbot import CMD_HANDLER as cmd
from userbot.utils import flicks_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@flicks_cmd(pattern="xalive")
async def yardim(event):
    try:
        kenbotusername = BOT_USERNAME
        if kenbotusername is not None:
            results = await event.client.inline_query(kenbotusername, "flicksalive")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                f"`Botnya tidak berfungsi! Silahkan atur vars `BOT_TOKEN` dan `BOT_USERNAME` dengan benar.\ntau gunakan perintah `{cmd}set var BOT_TOKEN` <token> dan `{cmd}set var BOT_USERNAME` <Username Bot mu>."
            )
    except Exception:
        return await event.edit(
            f"**Anda tidak dapat mengirim inline menu dalam obrolan ini, silakan gunakan perintah** `{cmd}inlineon`"
        )
