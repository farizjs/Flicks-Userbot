from time import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from userbot.utils import flicks_cmd
from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd

# Sudah di ubah menjadi cmd handler
# Fixes by team Flick-Userbot


@flicks_cmd(pattern="allban(?: |$)(.*)")
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("`Anda Tidak Mempunyai Hak Disini`")
        return
    await event.edit("**Berjalan.**")
    sleep(3)
    await event.edit("**Berjalan..**")
    sleep(3)
    await event.edit("**Berjalan...**")
    sleep(3)
    await event.edit("**Berjalan....**")

    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("**Perintah berhasil di jalankan**\n\n__Semua member telah terblokir__ 🙂")

CMD_HELP.update(
    {
        "allban": f"**• Plugin Allban •**\
        \n\n  •  **Perintah :** `{cmd}allban`\
        \n  •  **Function :** Blokir semua member dengan 1 perintah\n\n**!!! WARNING !!!**\
    "
    }
)
