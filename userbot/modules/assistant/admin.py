# Credits (c) DARK-COBRA

from telethon import events
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
)

from userbot import tgbot

# =================== CONSTANT ===================
PP_TOO_SMOL = "`Gambarnya terlalu kecil`"
PP_ERROR = "`Kegagalan saat memproses gambar`"
NO_ADMIN = "`Saya bukan admin!`"
NO_PERM = (
    "`Saya tidak memiliki izin yang memadai! Ini sangat sedep.`"
)
NO_SQL = "`Running on Non-SQL mode!`"

CHAT_PP_CHANGED = "`Gambar Obrolan Berubah`"
CHAT_PP_ERROR = (
    "`Beberapa masalah dengan memperbarui foto,`"
    "`mungkin karena saya bukan admin,`"
    "`atau tidak memiliki cukup hak.`"
)
INVALID_MEDIA = "`Ekstensi Tidak Valid`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)


@tgbot.on(events.NewMessage(pattern="^/ban(?: |$)(.*)"))
async def ban(event):
    noob = event.sender_id
    userids = []
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("You're not an admin!")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply("saya bukan Admin 🥺.")
        return

    user, reason = await get_user_from_event(event)
    if user:
        pass
    else:
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await event.reply("Tidak Ada Izin :D.")
        return
    # Helps ban group join spammers more easily
    try:
        reply = await event.get_reply_message()
        if reply:
            pass
    except BadRequestError:
        await event.reply(
            "`Saya tidak memiliki hak nuking pesan! Tapi tetap saja dia dilarang!`"
        )
        return
    if reason:
        await event.reply(f"Banned `{str(user.id)}` \nReason: {reason}")
    else:
        await event.reply(f"Banned  `{str(user.id)}` !")


@tgbot.on(events.NewMessage(pattern="^/unban(?: |$)(.*)"))
async def nothanos(event):
    userids = []
    noob = event.sender_id
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("Anda bukan Admin!")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply("Saya Bukan Admin 🥺")
        return
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await event.reply("`Pemblokiran Berhasil. Memberikan kesempatan lagi.🚶`")
    except BadRequestError:
        await event.reply("`Tidak ada izin 🤭`")
        return


@tgbot.on(events.NewMessage(pattern="^/promote(?: |$)(.*)"))
async def promote(event):
    userids = []
    noob = event.sender_id
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("Anda bukan admin!")
        return
    """ For .promote command, promotes the replied/tagged person """
    # Get targeted chat
    chat = await event.get_chat()
    # Grab admin status or creator in a chat
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, also return
    if not admin and not creator:
        await event.reply("Saya Bukan Admin 🥺")
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=False,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    user, rank = await get_user_from_event(event)
    if not rank:
        rank = "Admin"  # Just in case.
    if user:
        pass
    else:
        return
    # Try to promote if current user is admin or creator
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, new_rights, rank))
        await event.reply("`Berhasil Dipromosikan!`")

    # If Telethon spit BadRequestError, assume
    # we don't have Promote permission
    except BadRequestError:
        await event.reply("Tidak Ada Izin Untuk Mempromosikan 🤭")
        return


@tgbot.on(events.NewMessage(pattern="^/demote(?: |$)(.*)"))
async def demote(event):
    userids = []
    noob = event.sender_id
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("Anda bukan admin!")
        return
    """ For .demote command, demotes the replied/tagged person """
    # Admin right check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await event.reply("Saya Bukan Admin 🤭")
        return

    rank = "mememaster"  # dummy rank, lol.
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return

    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    # Edit Admin Permission
    try:
        await event.client(EditAdminRequest(event.chat_id, user.id, newrights, rank))

    # If we catch BadRequestError from Telethon
    # Assume we don't have permission to demote
    except BadRequestError:
        await event.reply("Saya Tidak ada Izin 🤔")
        return
    await event.reply("`Menurunkan Orang ini Berhasil!`")


@tgbot.on(events.NewMessage(pattern="^/pin(?: |$)(.*)"))
async def pin(event):
    userids = []
    noob = event.sender_id
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("Anda bukan admin!")
        return
    """ For .pin command, pins the replied/tagged message on the top the chat. """
    # Admin or creator check
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await event.reply("Saya Membutuhkan Izin Administrator 🤔")
        return

    to_pin = event.reply_to_msg_id

    if not to_pin:
        await event.reply("`Balas pesan untuk menyematkannya.`")
        return

    options = event.pattern_match.group(1)
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await event.client(UpdatePinnedMessageRequest(event.to_id, to_pin, is_silent))
    except BadRequestError:
        await event.reply("Tidak ada izin 🥺")
        return
    await event.reply("`Pinned Successfully!`")
    user = await get_user_from_id(msg.sender_id, msg)


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.reply("`Lewati nama pengguna, id, atau balasan pengguna!`")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj
