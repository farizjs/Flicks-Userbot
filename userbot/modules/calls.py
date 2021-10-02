# Thanks Full To Team Ultroid
# Ported By Vcky @VckyouuBitch + @MaafGausahSokap
# Copyright (c) 2021 Geez - Projects
# Geez - Projects https://github.com/Vckyou/Geez-UserBot
# RAM - UBOT https://github.com/ramadhani892/RAM-UBOT
# Ini Belum Ke Fix Ya Bg :')
# Ambil aja gapapa tp Gaguna kaya hidup lu Woakkakaka

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`You`re not admin in here.`"


async def get_call(event):
    rambot = await event.client(getchat(event.chat_id))
    rama = await event.client(getvc(rambot.full_chat.call))
    return rama.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, groups_only=True, pattern=r"^\.startvc$")
async def start_voice(td):
    chat = await td.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await td.edit(NO_ADMIN)
    try:
        await td.client(startvc(td.chat_id))
        await td.edit("`Voice chat turned on, dont open your cam kontol...`")
    except Exception as ex:
        await td.edit(f"`{str(ex)}`")


@register(outgoing=True, groups_only=True, pattern=r"^\.stopvc$")
async def stop_voice(td):
    chat = await td.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await td.edit(NO_ADMIN)
    try:
        await td.client(stopvc(await get_call(td)))
        await td.edit("`Stoped the voice call...`")
    except Exception as ex:
        await td.edit(f"`{str(ex)}`")


@register(outgoing=True, groups_only=True, pattern=r"^\.vcinvite")
async def vc_invite(td):
    await td.edit("`Memulai Invite member group...`")
    users = []
    z = 0
    async for x in td.client.iter_participants(td.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await td.client(invitetovc(call=await get_call(td), users=p))
            z += 6
        except BaseException:
            pass
    await td.edit(f"`Menginvite {z} Member`")


CMD_HELP.update(
    {
        "ramcalls": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
         \n↳ : Invite semua member yang berada di group. (Kadang bisa kadang kaga)."
    }
)
