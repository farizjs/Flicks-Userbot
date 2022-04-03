# Copyright (C) 2021 Catuserbot <https://github.com/sandy1709/catuserbot>
# Recode by @farizjs
# FROM Flicks-Userbot <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot

import io
import sys
import traceback

from userbot import CMD_HELP, CMD_HANDLER as hai
from userbot.utils import flicks_cmd, edit_or_reply


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


CMD_HELP.update({"calkulator": f"{hai}calc\n"
                 f"usage : Menyelesaikan permasalahan matematika dasar.\n"
                 "Memecahkan persamaan matematika yang diberikan dengan aturan BODMAS.\n"
                 f"contoh : `{hai}calc 2+9`, `{hai}calc 2*2`, `{hai}calc 7-2`, `{hai}calc 9/3`"})
