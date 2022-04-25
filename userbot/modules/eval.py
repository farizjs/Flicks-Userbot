# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
"""
Plugin : devtools


Perintah : `{i}eval print('world')`
Penggunaan: Jalankan skrip python kecil.

Perintah : `{i}exec print('hello')`
Penggunaan : Sama seperti `{i}eval`

Perintah : `{i}term <cmd>`
Penggunaan : Jalankan perintah dan skrip bash di server Anda.
"""

import asyncio
import io
import re
import sys
import traceback
from getpass import getuser
from os import remove
from sys import executable

from userbot import CMD_HELP, TERM_ALIAS, CMD_HANDLER
from userbot.utils import flicks_cmd


@flicks_cmd(pattern="eval(?: |$|\n)([\\s\\S]*)")
async def _(event):
    if event.fwd_from:
        return
    s_m_ = await event.edit("Processing ...")
    cmd = event.pattern_match.group(1)
    if not cmd:
        return await s_m_.edit("`Apa yang harus saya eval?...`")

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        returned = await aexec(cmd, s_m_)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = "No Output"
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    elif returned:
        evaluation = returned

    final_output = "**EVAL**: \n`{}` \n\n**OUTPUT**: \n`{}` \n".format(
        cmd, evaluation)

    if len(final_output) >= 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.txt"
            await s_m_.reply(cmd, file=out_file)
            await event.delete()
    else:
        await s_m_.edit(final_output)


async def aexec(code, smessatatus):
    message = event = smessatatus

    reply = await event.get_reply_message()
    exec(
        f"async def __aexec(message, reply, client): "
        + "\n event = smessatatus = message"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](message, reply, message.client)


@flicks_cmd(pattern="exec(?: |$|\n)([\\s\\S]*)")
async def run(run_q):
    """ For .exec command, which executes the dynamically created program """
    code = run_q.pattern_match.group(1)

    if run_q.is_channel and not run_q.is_group:
        return await run_q.edit("`Exec tidak diizinkan di channel!`")

    if not code:
        return await run_q.edit(
            "``` Setidaknya variabel diperlukan untuk"
            "menjalankan. Gunakan {CMD_HANDLER}help devtools sebagai contoh.```"
        )

    if code in ("userbot.session", "config.env"):
        return await run_q.edit("`Itu operasi yang berbahaya! Tidak diperbolehkan!`")

    if len(code.splitlines()) <= 5:
        codepre = code
    else:
        clines = code.splitlines()
        codepre = (
            clines[0] +
            "\n" +
            clines[1] +
            "\n" +
            clines[2] +
            "\n" +
            clines[3] +
            "...")

    command = "".join(f"\n {l}" for l in code.split("\n.strip()"))
    process = await asyncio.create_subprocess_exec(
        executable,
        "-c",
        command.strip(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    if result:
        if len(result) > 4096:
            file = open("output.txt", "w+")
            file.write(result)
            file.close()
            await run_q.client.send_file(
                run_q.chat_id,
                "output.txt",
                reply_to=run_q.id,
                caption="`Output terlalu besar, mengirim sebagai file`",
            )
            remove("output.txt")
            return
        await run_q.edit(
            "**Query: **\n`" f"{codepre}" "`\n**Result: **\n`" f"{result}" "`"
        )
    else:
        await run_q.edit(
            "**Query: **\n`" f"{codepre}" "`\n**Result: **\n`No result returned/False`"
        )


@flicks_cmd(pattern="term(?: |$|\n)(.*)")
async def terminal_runner(term):
    """ For .term command, runs bash commands and scripts on your server. """
    curruser = TERM_ALIAS if TERM_ALIAS else getuser()
    command = term.pattern_match.group(1)
    try:
        from os import geteuid

        uid = geteuid()
    except ImportError:
        uid = "Ini bukan ketua!"

    if term.is_channel and not term.is_group:
        return await term.edit("`Perintah istilah tidak diizinkan di saluran!`")

    if not command:
        return await term.edit(
            "``` Beri perintah atau Gunakan {CMD_HANDLER}help devtools sebagai contoh.```"
        )

    for i in ("userbot.session", "env"):
        if command.find(i) != -1:
            return await term.edit("`Itu operasi yang berbahaya! Tidak diperbolehkan!`")

    if not re.search(r"echo[ \-\w]*\$\w+", command) is None:
        return await term.edit("`Itu operasi yang berbahaya! Tidak diperbolehkan!`")

    process = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    if len(result) > 4096:
        output = open("output.txt", "w+")
        output.write(result)
        output.close()
        await term.client.send_file(
            term.chat_id,
            "output.txt",
            reply_to=term.id,
            caption="`Output terlalu besar, mengirim sebagai file`",
        )
        remove("output.txt")
        return

    if uid == 0:
        await term.edit(f"`{curruser}:~# {command}\n{result}`")
    else:
        await term.edit(f"`{curruser}:~$ {command}\n{result}`")


CMD_HELP.update({"devtools": f"{__doc__.format(i=CMD_HANDLER)}"})
