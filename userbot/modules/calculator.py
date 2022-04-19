# Copyright (C) 2021 Catuserbot <https://github.com/sandy1709/catuserbot>
# Copyright (C) 2021 Ultroid <https://github.com/Teamultroid/Ultroid>
# Recode by @farizjs
# FROM Flicks-Userbot <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot
"""
Plugin : Calculator

Perintah : `{i}icalc`
Penggunaan : Inline Kalkulator

Perintah : `{i}calc`
Penggunaan : Alternatif jika `{i}icalc` tidak dapat digunakan
"""

import io
import sys
import traceback

from userbot import BOT_USERNAME, CMD_HELP, CMD_HANDLER as hai
from userbot.utils import flicks_cmd, edit_or_reply


@flicks_cmd(pattern="icalc")
async def yardim(event):
    try:
        botusername = BOT_USERNAME
        if botusername is not None:
            results = await event.client.inline_query(botusername, "calc")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                f"`Botnya tidak berfungsi! Silahkan atur vars `BOT_TOKEN` dan `BOT_USERNAME` dengan benar.\ntau gunakan perintah `{hai}set var BOT_TOKEN` <token> dan `{hai}set var BOT_USERNAME` <Username Bot mu>."
            )
    except Exception:
        return await event.edit(
            f"**Anda tidak dapat mengirim inline menu dalam obrolan ini, sebagai alternatif, silakan gunakan perintah** `{hai}calc`"
        )


@flicks_cmd(pattern="calc(?: |$)(.*)*")
async def calculator(event):
    "Untuk menyelesaikan persamaan matematika dasar."
    cmd = event.text.split(" ", maxsplit=1)[1]
    event = await edit_or_reply(event, "Calculating ...")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    san = f"print({cmd})"
    try:
        await aexec(san, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Maaf saya tidak dapat menemukan hasil untuk persamaan yang diberikan"
    final_output = "**PERSAMAAN**: `{}` \n\n **SOLUSI**: \n`{}` \n".format(
        cmd, evaluation
    )
    await event.edit(final_output)


async def aexec(code, event):
    exec("async def __aexec(event): " +
         "".join(f"\n {l}" for l in code.split("\n")))

    return await locals()["__aexec"](event)


CMD_HELP.update({"calculator": f"{__doc__.format(i=hai)}"})
