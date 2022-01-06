# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests

from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import flicks_cmd


@flicks_cmd(pattern="vidwibu$")
async def _(event):
    try:
        response = requests.get(
            "https://api-tede.herokuapp.com/api/asupan/wibu").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video wibu.**")


@flicks_cmd(pattern="chika$")
async def _(event):
    try:
        response = requests.get(
            "https://api-tede.herokuapp.com/api/chika").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video chikakiku.**")


CMD_HELP.update(
    {
        "video": f"**Plugin : **`video`\
        \n\n  •  **Syntax :** `{cmd}vidwibu`\
        \n  •  **Function : **Untuk Mengirim video wibu secara random.\
        \n\n  •  **Syntax :** `{cmd}chika`\
        \n  •  **Function : **Untuk Mengirim video chikakiku secara random.\
    "
    }
)
