# Copyright (C) 2021 King - Userbot
# Created by Apis
# Jangan hapus credit asu!!!
# Recode back team Flicks - Userbot

from random import choice

from userbot import CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
XBOT_STRINGS = [
    "** Aku Userbot Bang 😎**",
    "** Berani lawan ku gban kau 😁**",
    "** Lawak cuman user telegram belum jadi userbot 😂**",
    "** Userbot ni bos 😎**",

]


@register(outgoing=True, pattern="^.xbot$")
async def xbot(xbotflicks):
    await xbotflicks.edit(choice(XBOT_STRINGS))

CMD_HELP.update(
    {
        "xbot": "**• Plugin Xbot •** \
        \n\n  •  **Perintah :** `.xbot`\
        \n  •  **Function : **Xbot random untuk bersenang senang saja\
    "
    }
)
