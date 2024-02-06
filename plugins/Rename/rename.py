"""
Apache License 2.0
Copyright (c) 2023 Dj
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Dev Channel Link : https://t.me/LazyDeveloper 
Repo Link : https://github.com/LazyDeveloperr/LazyPrincess
License Link : https://github.com/LazyDeveloperr/LazyPrincess/blob/main/LICENSE
# Removing this is strictly prohibited ! Don't remove this all without the 
permission of LazyDeveloperr
"""
    # Credit @LazyDeveloper.
    # Please Don't remove credit.
    # Born to make history @LazyDeveloper !

    # Thank you LazyDeveloper for helping us in this Journey
    # 🥰  Thank you for giving me credit @LazyDeveloperr  🥰

    # for any error please contact me -> telegram@LazyDeveloperr or insta @LazyDeveloperr 

import asyncio
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait,UserNotParticipant
import humanize
from info import *


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video) & filters.user(ADMINS))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**What do you to do with this file?**\n\n**File Name** : `{filename}`\n\n**File Size** : `{filesize}`"""
        buttons = [[ InlineKeyboardButton("Start Rename", callback_data="rename") ],
                   [ InlineKeyboardButton("Cancel", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**What do you to do with this file?**\n\n**File Name** : `{filename}`\n\n**File Size** : `{filesize}`"""
        buttons = [[ InlineKeyboardButton("Start Rename", callback_data="rename") ],
                   [ InlineKeyboardButton("Cancel", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass
