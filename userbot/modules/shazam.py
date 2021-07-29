# Ported By KENNEDY <@xgothboi>
#
# KennedyProject Userbot
# Copyright (C) 2021 KennedyProject
#
# This file is a part of <https://github.com/KennedyProject/KEN-UBOT/>
# PLease read the GNU Affero General Public License in
# <https://github.com/KennedyProject/KEN-UBOT/blob/KEN-UBOT/LICENSE>.


from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.shazam(?: |$)(.*)")
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("```Replying To Audio.```")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("```Identification Song```")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "Something Wrong. Use Audio Duration Minimal 5-10 Second."
                    )
                await event.edit("```Please Wait...```")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Please Unblock (@auddbot) And Try Again...```")
                return
            namem = f"**Title : **{result.text.splitlines()[0]}\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id, [start_msg.id, send_audio.id, check.id, result.id, response.id]
            )
    except TimeoutError:
        return await event.edit("`Error: `@auddbot` not responding, try again later...")

CMD_HELP.update(
    {
        "shazam": ">`.shazam <reply to voice/audio>"
        "\nUsage: Reverse search audio file using (@auddbot)"
    }
)
