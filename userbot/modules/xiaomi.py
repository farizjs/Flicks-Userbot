# created by @eve_enryu
"""
Plugin : xiaomi
Hanya untuk perangkat Xiaomi!


`{i}firmware` (codename)\
Penggunaan : Dapatkan Firmware terbaru\

`{i}pb` (codename)\
Penggunaan : Dapatkan Pemulihan PitchBlack terbaru\

`{i}specs` (codename)\
Penggunaan : Dapatkan informasi spesifikasi cepat tentang perangkat\

`{i}fastboot` (codename)\
Penggunaan : Dapatkan MIUI fastboot terbaru\

`{i}recovery` (codename)\
Penggunaan : Dapatkan MIUI pemulihan terbaru\

`{i}eu` (codename)\
Penggunaan : Dapatkan rom xiaomi.eu terbaru\

`{i}vendor` (codename)\
Penggunaan : mengambil vendor terbaru\

`{i}of` (codename)\
Penggunaan : Dapatkan Pemulihan ORangeFox terbaru
"""

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import flicks_cmd


@flicks_cmd(pattern="firmware(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    firmware = "firmware"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{firmware} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Harap Unblock @XiaomiGeeksBot```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@flicks_cmd(pattern="fastboot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = "fastboot"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{fboot} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Harap Unblock @XiaomiGeeksBoot```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@flicks_cmd(pattern="recovery(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    recovery = "recovery"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{recovery} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Harap Unblock @XiaomiGeeksBot```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@flicks_cmd(pattern="pb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pitch = "pb"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{pitch} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Harap Unblock @XiaomiGeeksBot```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@flicks_cmd(pattern="of(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ofox = "of"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{ofox} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Harap Unblock @XiaomiGeeksBot```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@flicks_cmd(pattern="eu(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    eu = "eu"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{eu} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Harap Unblock @XiaomiGeeksBot```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@flicks_cmd(pattern="vendor(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    vendor = "vendor"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{vendor} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Harap Unblock @XiaomiGeeksBot```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@flicks_cmd(pattern="specs(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = "specs"
    await event.edit("```Processing```")
    async with bot.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/{specs} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("```Harap Unblock @XiaomiGeeksBot```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


CMD_HELP.update({"xiaomi": f"{__doc__.format(i=cmd)}"})
