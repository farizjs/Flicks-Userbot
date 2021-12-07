import logging

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import BOT_USERNAME
from userbot.events import register

chat = "@BotFather"

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@register(outgoing=True, pattern=r"^\.helpme")
async def yardim(event):
    try:
        kenbotusername = BOT_USERNAME
        if kenbotusername is not None:
            results = await event.client.inline_query(kenbotusername, "@FlicksSupport")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Silahkan Tambahkan Var `BOT_TOKEN` dan `BOT_USERNAME` terlebih dahulu."
            )
    except Exception:
        return await event.edit(
            "`Anda tidak dapat mengirim hasil sebaris dalam obrolan ini (disebabkan oleh SendInlineBotResultRequest)\nSedang menyalakan, mohon tunggu`"
        )
              async with event.client.conversation(chat) as conv:
               try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(BOT_USERNAME)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message("Search")
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await event.edit("Harap Unblock @Botfather.")
                await event.edit(
                    f"**Berhasil Menyalakan Mode Inline**\n\n**Ketik** `.helpme` **lagi untuk membuka menu bantuan.**"
                )
