# Credits Cat-Userbot <github.com/TgCatUb/Cat-Userbot>
# Recode by fariz <farizjs>
# t.me/FlicksSupport
"""
Plugin : sangmata

Perintah : `{i}sg`
Penggunaan : Cek riwayat nama pengguna

Perintah : `{i}sgu`
Penggunaan : Cek riwayat username pengguna
"""

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, CMD_HELP, CMD_HANDLER
from userbot.utils import flicks_cmd, edit_delete, edit_or_reply, get_user_from_event, _format


async def sanga_seperator(sanga_list):
    for i in sanga_list:
        if i.startswith("🔗"):
            sanga_list.remove(i)
    s = 0
    for i in sanga_list:
        if i.startswith("Username History"):
            break
        s += 1
    usernames = sanga_list[s:]
    names = sanga_list[:s]
    return names, usernames

@flicks_cmd(pattern="sg(u)?(?:\s|$)([\s\S]*)")
async def _(event):  # sourcery no-metrics
    "To get name/username history."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "`balas pesan teks pengguna untuk mendapatkan riwayat nama/username pengguna atau berikan id/username`",
        )
    user, rank = await get_user_from_event(event, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMataInfo_bot"
    flicksevent = await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await edit_delete(flicksevent, "`unblock @Sangmatainfo_bot dan kemudian coba lagi`")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(flicksevent, "`bot tidak dapat mengambil hasil`")
    if "No records found" in responses:
        await edit_delete(flicksevent, "`Pengguna tidak memiliki catatan apa pun`")
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    saya = None
    check = usernames if cmd == "u" else names
    for i in check:
        if saya:
            await event.reply(i, parse_mode=_format.parse_pre)
        else:
            saya = True
            await flicksevent.edit(i, parse_mode=_format.parse_pre)

CMD_HELP.update({"sangmata": f"{__doc__.format(i=CMD_HANDLER)}"})
