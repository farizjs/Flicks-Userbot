# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import requests

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.vidwibu$")
async def _(event):
    try:
        response = requests.get(
            "https://api-tede.herokuapp.com/api/asupan/wibu").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video wibu.**")


@register(outgoing=True, pattern=r"^\.chika$")
async def _(event):
    try:
        response = requests.get(
            "https://api-tede.herokuapp.com/api/chika").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video chikakiku.**")


@register(outgoing=True, pattern=r"^\.bocil$")
async def _(event):
    try:
        response = requests.get(
            "https://api-alphabot.herokuapp.com/api/asupan/bocil?apikey=Alphabot"
        ).json()
        await event.client.send_file(event.chat_id, response["result"])
        await event.delete()
    except Exception:
        await event.edit("**Tidak bisa menemukan video asupan bocil.**")


CMD_HELP.update(
    {
        "video": "**Plugin : **`video`\
        \n\n  •  **Syntax :** `.vidwibu`\
        \n  •  **Function : **Untuk Mengirim video wibu secara random.\
        \n\n  •  **Syntax :** `.chika`\
        \n  •  **Function : **Untuk Mengirim video chikakiku secara random.\
    "
    }
)
