# Credits: @xditya
# Recode by @farizjs
# FROM Flicks-Userbot <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot

import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import userbot.modules.sql_helper.pm_permit_sql as pmpermit_sql
from userbot import *
from userbot.utils import flicks_cmd

i = CMD_HANDLER
TELEPIC = PMPERMIT_PIC
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
saya = bot.get_me()
myid = saya.id
CUSTOM_PMPERMIT = None
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "`Userbot PM security! Tolong tunggu saya untuk menyetujui Anda. 😊"
)
DEFAULTUSER = ALIVE_NAME
USER_BOT_WARN_ZERO = "`Saya telah memperingatkan Anda untuk tidak melakukan spam. Sekarang Anda telah diblokir dan dilaporkan hingga pemberitahuan lebih lanjut.`\n\n**Selamat Tinggal!** "
USER_BOT_NO_WARN = (
    "**PM Security ~ Userbot**\n\nSenang melihatmu di sini, tapi  "
    "[{}](tg://user?id={}) saat ini tidak tersedia.\nIni adalah pesan otomatis.\n\n"
    "{}\n\n**Kamu punya** `{}/{}` **peringatan...**"
    "\n\n   ~ Terima kasih."
)


@flicks_cmd(pattern="ok ?(.*)")
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            if chat.id in PM_WARNS:
                del PM_WARNS[chat.id]
            if chat.id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat.id].delete()
                del PREV_REPLY_MESSAGE[chat.id]
            pmpermit_sql.approve(chat.id, reason)
            await event.edit(
                "Disetujui [{}](tg://user?id={}) untuk PM kamu.".format(firstname, chat.id)
            )
            await asyncio.sleep(3)
            await event.delete()


# Approve outgoing


@bot.on(events.NewMessage(outgoing=True))
async def you_dm_niqq(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            if chat.id not in PM_WARNS:
                pmpermit_sql.approve(chat.id, "outgoing")
                logit = "#Auto_Approved\nUser - [{}](tg://user?id={})".format(
                    chat.first_name, chat.id
                )
                try:
                    await bot.send_message(BOTLOG_CHATID, logit)
                except BaseException:
                    pass


@flicks_cmd(pattern="block ?(.*)")
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if chat.id == DEVS:
            await event.edit("Anda mencoba untuk memblokir tuanku. Selamat tinggal selama 100 detik! 💤")
            await asyncio.sleep(100)
        else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "Terlambat.\nBlocked [{}](tg://user?id={})".format(
                        firstname, chat.id
                    )
                )
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))


@flicks_cmd(pattern="tolak ?(.*)")
async def approve_p_m(event):
    if event.fwd_from:
        return
    replied_user = await event.client(GetFullUserRequest(event.chat_id))
    firstname = replied_user.user.first_name
    event.pattern_match.group(1)
    chat = await event.get_chat()
    if event.is_private:
        if chat.id == DEVS:
            await event.edit("Maaf, Saya Tidak Dapat Menolak Tuan Saya")
        else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    "[{}](tg://user?id={}) tidak disetujui untuk PM.".format(
                        firstname, chat.id
                    )
                )


@flicks_cmd(pattern="listapproved")
async def approve_p_m(event):
    if event.fwd_from:
        return
    approved_users = pmpermit_sql.get_all_approved()
    APPROVED_PMs = "[TeleBot] Currently Approved PMs\n"
    if len(approved_users) > 0:
        for a_user in approved_users:
            if a_user.reason:
                APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) untuk {a_user.reason}\n"
            else:
                APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
    else:
        APPROVED_PMs = "Tidak Ada PM yang Disetujui (yet)"
    if len(APPROVED_PMs) > 4095:
        with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
            out_file.name = "approved.pms.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="[Userbot]PM yang Disetujui Saat Ini",
                reply_to=event,
            )
            await event.delete()
    else:
        await event.edit(APPROVED_PMs)


@bot.on(events.NewMessage(incoming=True))
async def on_new_private_message(event):
    if event.sender_id == myid:
        return

    if BOTLOG_CHATID is None:
        return

    if not event.is_private:
        return

    message_text = event.message.message
    chat_id = event.sender_id

    message_text.lower()
    if USER_BOT_NO_WARN == message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return
    sender = await bot.get_entity(chat_id)

    if chat_id == saya.id:

        # don't log Saved Messages

        return

    if sender.bot:

        # don't log bots

        return

    if sender.verified:

        # don't log verified accounts

        return

    if not pmpermit_sql.is_approved(chat_id):
        # pm permit
        await do_pm_permit_action(chat_id, event)


async def do_pm_permit_action(chat_id, event):
    if PM_AUTO_BAN.lower() == "False":
        return
    if chat_id not in PM_WARNS:
        PM_WARNS.update({chat_id: 0})
    if PM_WARNS[chat_id] == PM_LIMIT:
        r = await event.reply(USER_BOT_WARN_ZERO)
        await asyncio.sleep(3)
        await event.client(functions.contacts.BlockRequest(chat_id))
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r
        the_message = ""
        the_message += "#BLOCKED_PMs\n\n"
        the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
        the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
        # the_message += f"Media: {message_media}"
        try:
            await event.client.send_message(
                entity=BOTLOG_CHATID,
                message=the_message,
                # reply_to=,
                # parse_mode="html",
                link_preview=False,
                # file=message_media,
                silent=True,
            )
            return
        except BaseException:
            return
    # inline pmpermit menu
    mybot = BOT_USERNAME
    MSG = USER_BOT_NO_WARN.format(
        DEFAULTUSER, myid, MESAG, PM_WARNS[chat_id] + 1, PM_LIMIT
    )
    tele = await bot.inline_query(mybot, "pmpermit")
    r = await tele[0].click(event.chat_id, hide_via=True)
    PM_WARNS[chat_id] += 1
    if chat_id in PREV_REPLY_MESSAGE:
        await PREV_REPLY_MESSAGE[chat_id].delete()
    PREV_REPLY_MESSAGE[chat_id] = r



@bot.on(
    events.NewMessage(
        incoming=True, from_users=(DEVS)
    )
)
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**Dev di sini**")
            await bot.send_message(chat, "**Ini dia Tuanku! Beruntungnya kamu!!**")


# instant block
NEEDIT = None
if NEEDIT == "on":

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        event.message.message
        event.message.media
        event.message.id
        event.message.to_id
        chat_id = event.chat_id
        sender = await bot.get_entity(chat_id)
        if chat_id == saya.id:
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if not pmpermit_sql.is_approved(chat_id):
            await bot(functions.contacts.BlockRequest(chat_id))

CMD_HELP.update(
    {
        "pmpermit": f"Cmd: > `{i}ok`"
        "\n↳ : Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm."
        f"\n\nCmd: >`{i}tolak`"
        "\n↳ : Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm."
        f"\n\nCmd: >`{i}block`"
        "\n↳ : Memblokir Orang Di PM."
        f"\n\nCmd: >`{i}unblock`"
        "\n↳ : Membuka Blokir."
        f"\n\n**Note :\nUntuk mengaktifkan pmpermit gunakan perintah**\n`{i}set var PM_AUTO_BAN true`"})
