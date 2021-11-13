# By Fariz (@FJ_GAMING) Flicks-Userbot
# Do not remove credits ⚠️
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from userbot import CMD_HELP
from userbot.events import register

chat = "@Ribot"


@register(outgoing=True, pattern="^.search ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text, username = event.pattern_match.group(1).split()

    else:
        await event.edit("`Masukan Yang Benar Biar Bisa Search Google`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(text)
            await conv.get_response()
            await event.client.forward_messages(event.chat_id)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("683757318"))
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(text)
            await conv.get_response()
            await event.client.forward_messages(event.chat_id)
            await event.delete()


CMD_HELP.update(
    {
        "googlesearch": ".search\
    \nUntuk Mencari sesuatu di google  ."
    }
)
