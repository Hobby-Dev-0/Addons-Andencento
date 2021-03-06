"""Pins the replied message
Syntax: .cpin [LOUD]"""
from telethon import events
from telethon.tl import functions, types
from userbot.utils import admin_cmd


@borg.on(admin_cmd("cpin ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    silent = not input_str
    if event.message.reply_to_msg_id is not None:
        message_id = event.message.reply_to_msg_id
        try:
            await borg(functions.messages.UpdatePinnedMessageRequest(
                event.chat_id,
                message_id,
                silent
            ))
        except Exception as e:
            await event.edit(str(e))
        else:
            await event.delete()
    else:
        await event.edit("Reply to a message to pin the message in this Channel.")
