# https://github.com/fjgaming212/Flicks-Userbot

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from userbot import CMD_HELP
from userbot.events import register

chat = "@Ribot"


@register(outgoing=True, pattern=r"^\.search(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1):
        text = event.pattern_match.group(1).split()

    else:
        await event.edit("`Tolong masukan kata kata yang Ingin dicari`")
        return

    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()
        except YouBlockedUserError:
            await event.client(UnblockRequest("683757318"))
            await conv.send_message("/start")
            audio = await conv.get_response()
            await conv.send_message(text)
            audio = await conv.get_response()
            await event.client.forward_messages(event.chat_id, audio)
            await event.delete()


CMD_HELP.update(
    {
        "googlesearch": ". search\
    \nUntuk Mencari sesuatu di google  ."
    }
)
