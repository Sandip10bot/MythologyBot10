import os
import time
import ytthumb
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("ytthumb"))
async def yt_thumbnail(bot, update):
    message = await update.reply_text(
        text="`Analysing...`",
        disable_web_page_preview=True,
        quote=True
    )
    try:
        if " | " in update.text:
            video = update.text.split(" | ", -1)[0]
            quality = update.text.split(" | ", -1)[1]
        else:
            video = update.text
            quality = "hd"
        thumbnail = ytthumb.thumbnail(
            video=video,
            quality=quality
        )
        await update.reply_photo(
            photo=thumbnail,
            quote=True
        )
        await message.delete()
    except Exception as error:
        y = await message.edit_text(
            text="**Use :** /ytthumb utube link here.",
            disable_web_page_preview=True)
        await asyncio.sleep(30)
        await y.delete()
        await message.delete()
