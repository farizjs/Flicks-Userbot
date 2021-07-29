from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern'^.fak(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(".                       /¯ )")
    sleep(1)
    await typew.edit(".                       /¯ )\n                      /¯  /")
    sleep(1)
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    sleep(1)
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    sleep(1)
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    sleep(1)
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    sleep(1)
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    sleep(1)
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    sleep(1)
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    sleep(1)
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")


@register(outgoing=True, pattern='^.diam(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Kamu Berisik Banget Dari Tadi.**")
    sleep(2)
    await typew.edit("**Bisa Diam Tidak?!**")


CMD_HELP.update({
    "nyindir2":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fak`\
\n↳ : Coba Aja Sendiri.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.diam`\
\n↳ : Coba Aja Sendiri."
})
