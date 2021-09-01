"""
✘ Commands Available -

• `{i}fullpromote <reply user/ username>`
 Promote User With All rights
"""



import asyncio

from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import ChatNotModifiedError, UserIdInvalidError
from telethon.tl.functions.channels import DeleteUserHistoryRequest, EditAdminRequest
from telethon.tl.functions.channels import ExportMessageLinkRequest as ExpLink
from telethon.tl.functions.messages import SetHistoryTTLRequest
from telethon.tl.types import Chat, ChatAdminRights, InputMessagesFilterPinned

from . import *


@ultroid_cmd(
    pattern="fullpromote ?(.*)",
    admins_only=True,
    type=["official", "manager"],
    ignore_dualmode=True,
)
async def prmte(ult):
    xx = await eor(ult, get_string("com_1"))
    await ult.get_chat()
    user, rank = await get_user_info(ult)
    if not rank:
        rank = "••Aᴅᴍɪɴ••"
    if not user:
        return await xx.edit("`Reply to a user to promote him with all rights!`")
    try:
        await ult.client(
            EditAdminRequest(
                ult.chat_id,
                user.id,
                ChatAdminRights(
                    add_admins=True,
                    invite_users=True,
                    change_info=True,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True,
                    manage_call=True,
                ),
                rank,
            ),
        )
        await xx.edit(
            f"**{inline_mention(user)}** `is now an admin with full rights in` **{ult.chat.title}** `with title` **{rank}**.",
        )
    except BadRequestError:
        return await xx.edit("`I don't have the right to promote you.`")
    await asyncio.sleep(5)
    await xx.delete()