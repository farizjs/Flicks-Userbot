from time import sleep
from userbot.events import register
from userbot import ALIVE_NAME, CMD_HELP, WEATHER_DEFCITY


@register(outgoing=True, pattern='^.intro(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"`Hai Perkenalkan Namaku {ALIVE_NAME}`")
    sleep(3)
    await typew.edit(f"`Umurku Rahasia :D`")
    sleep(1)
    await typew.edit(f"`Tinggal Di {WEATHER_DEFCITY}, Salam Kenal :)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.lopyu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH 🥰`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Selalu Bersyukur`")
    sleep(1)
    await typew.edit("`Dan Jangan Lupa Tertawa:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.aku(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Aku Userbot`")
    sleep(3)
    await typew.edit("`Jangan Main Main`")
    sleep(2)
    await typew.edit("`Aku Gban Nanti Nangesss Lho 🥺`")
# Create by myself @localheart


CMD_HELP.update({
    "flicks": "\
**Perintah:** `.intro`\
\n**Penjelasan:** Memperkenalkan diri anda\
\n\n**Perintah:** `.semangat`\
\n**Penjelasan:** Sedikit Motifasi\
\n\n**Perintah:** `.aku`\
\n**Penjelasan:** Lihat sendiri 🏃\
\n\n**Perintah:** `.lopyu`\
\n**Penjelasan:** Lihat Sendiri 🏃"})
