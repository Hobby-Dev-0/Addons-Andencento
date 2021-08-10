import asyncio
from asyncio import wait
from telethon import events, utils

from userbot.events import register

@register(outgoing=True, pattern="^.sspam")
async def spammer(e):
    if e.text[0].isalpha() or e.text[0] in ("/", "#", "@", "!"):
        return
    message = e.text
    text = message.split()
    counter = int(text[1])
    spam_message = str(text[2])
      #  sm = ' '.join([str(elem) for elem in spam_message]) 
       # sm = ' '.join(map(str, spam_message)) 
    sleep2 = int(text[3])
    await e.delete()
    for _ in range(counter):
        await asyncio.wait([ 
        e.respond(spam_message)])
        await asyncio.sleep(sleep2)
        
