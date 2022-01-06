# Thanks Full To Team Ultroid
# Ported By Vcky @VckyouuBitch
# Copyright (c) 2021 Geez - Projects
# Fix By Kyy @IDnyaKosong


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot import CMD_HANDLER as cmd
from userbot.utils import flicks_cmd


NO_ADMIN = "`Maaf Kamu Bukan Admin 👮`"


async def get_call(event):
    kyy = await event.client(getchat(event.chat_id))
    kyy = await event.client(getvc(kyy.full_chat.call, limit=1))
    return kyy.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@flicks_cmd(pattern="startvc$")
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(startvc(e.chat_id))
        await e.edit("`Memulai Obrolan Suara`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@flicks_cmd(pattern="stopvc$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("`Mengakhiri Obrolan Suara`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@flicks_cmd(pattern="vcinvite")
async def _(e):
    await e.edit("`Sedang Mengivinte Member...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await e.edit(f"`Invited {z} users`")


CMD_HELP.update({
    "vcg": f"perintah: `{cmd}startvc`\
    \n↳ : Untuk Memulai voice chat group.\
    \nPerintah: `{cmd}stopvc`\
    \n↳ : Untuk Memberhentikan voice chat group.\
    \nPerintah: `{cmd}vcinvite`\
    \n↳ : Mengundang Member group ke voice chat group. (You must be joined)."
})
