import logging

from userbot import BOT_USERNAME
from userbot import CMD_HANDLER as cmd
from userbot.utils import flicks_cmd

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@flicks_cmd(pattern="helpme")
async def _(event):
    if event.fwd_from:
        return
    botusername = BOT_USERNAME
    noob = "@FlicksSupport"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()
