import random
from userbot.utils import asst_cmd

APAKAH_STRING = ["Iya",
                 "Tidak",
                 "Mungkin",
                 "Mungkin Tidak",
                 "Bisa jadi",
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YNTKTS",
                 "Coba aja",
                 "Apa iya?",
                 "Bisa iya bisa tidak"
                 ]


@asst_cmd(pattern=r"^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan!')
        return
    await event.reply(random.choice(APAKAH_STRING))
