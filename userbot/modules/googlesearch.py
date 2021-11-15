#  © @FJ_GAMING
# ⚠️ Do not remove credits
import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.search(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Give a teks too!`")
    else:
        await event.edit("`Processing...`")
    chat = "@ribot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"{text}")
            response = await conv.get_response()
            await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @ribot **Dan Coba Lagi!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_message(
            event.chat_id,
            message,
            caption=f"**Hasil Pencarian**",
        )
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id])
        await event.delete()


CMD_HELP.update({"googlesearch": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.search` <teks>"
                 "\n↳ : Untuk mencari sesuatu di google."})
