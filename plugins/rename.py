import asyncio
import math
import time 
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.enums import MessageMediaType
import humanize
from database.users_chats_db import db
from info import *
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
import traceback
from datetime import datetime
import logging, asyncio, shutil, psutil, os, sys

PROGRESS_BAR = """\n
╭━━━━❰• **Process** •❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """

@Client.on_message( filters.private & (filters.document | filters.audio | filters.video) & filters.user(ADMINS))
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

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    try:
        if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
            new_name = message.text
            await message.delete()
            media = await client.get_messages(message.chat.id, message.reply_to_message.id)
            file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
            filename = file.file_name
            types = file.mime_type.split("/")
            mime = types[0]
            mg_id = media.reply_to_message.id
            try:
                out = new_name.split(".")
                out[1]
                out_name = out[-1]
                out_filename = new_name
                await message.reply_to_message.delete()
                if mime == "video":
                    markup = InlineKeyboardMarkup([[
                        InlineKeyboardButton("📁 Document", callback_data="upload_document"),
                        InlineKeyboardButton("🎥 Video", callback_data="upload_video")]])
                elif mime == "audio":
                    markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                        "📁 Document", callback_data="doc"), InlineKeyboardButton("🎵 audio", callback_data="upload_audio")]])
                else:
                    markup = InlineKeyboardMarkup(
                        [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]])
                # Lazy-WarninG -> Please Dont chnage anything after this Line 
                await message.reply_text(f"**Select the output file type**\n**🎞New Name** :- ```{out_filename}```", reply_to_message_id=mg_id, reply_markup=markup)

            except:
                try:
                    out = filename.split(".")
                    out_name = out[-1]
                    out_filename = new_name + "." + out_name
                    print(f"out name: {out_filename}")
                except:
                    await message.reply_to_message.delete()
                    await message.reply_text("**Error** :  No  Extension in File, Not Supporting", reply_to_message_id=mg_id)
                    return
                await message.reply_to_message.delete()
                if mime == "video":
                    markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                        "📁 Document", callback_data="upload_document"), InlineKeyboardButton("🎥 Video", callback_data="upload_video")]])
                elif mime == "audio":
                    markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                        "📁 Document", callback_data="upload_document"), InlineKeyboardButton("🎵 audio", callback_data="upload_audio")]])
                else:
                    markup = InlineKeyboardMarkup(
                        [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]])
                # Lazy-WarninG -> Please Dont chnage anything after this Line 
                await message.reply_text(f"**Select the output file type**\n**🎞New Name ->** :- {out_filename}",
                                        reply_to_message_id=mg_id, reply_markup=markup)
    except Exception as e:
        print(f"error: {e}")

async def progress_for_pyrogram(current, total, ud_type, message, start):

    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "{0}{1}".format(
            ''.join(["█" for i in range(math.floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - math.floor(percentage / 5))]))

        tmp = progress + script.PROGRESS_BAR.format( 
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n\n{}".format(ud_type, tmp),               
                reply_markup=InlineKeyboardMarkup( [[
                    InlineKeyboardButton("⨳  C L Ф S Ξ  ⨳", callback_data="cancel")
                    ]]
                )
            )
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60      
    return "%d:%02d:%02d" % (hour, minutes, seconds)


@Client.on_message(filters.private & filters.command(['viewthumb']) & filters.user(ADMINS))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("No Thumbnail Yet.") 
		
@Client.on_message(filters.private & filters.command(['delthumb']) & filters.user(ADMINS))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("❌️ Your Thumbnail Deleted!")
	
@Client.on_message(filters.private & filters.photo & filters.user(ADMINS))
async def addthumbs(client, message):
    mkn = await message.reply_text("...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("✅️ Your Thumbnail Saved!")

@Client.on_message(filters.private & filters.command('set_caption') & filters.user(ADMINS))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Note: Lazy_Mode active ✅\n\n__𝙶𝚒𝚟𝚎 𝚖𝚎 𝚊 𝚌𝚊𝚙𝚝𝚒𝚘𝚗 𝚝𝚘 𝚜𝚎𝚝.__\n\n𝙴𝚡𝚊𝚖𝚙𝚕𝚎:- `/set_caption {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__** 𝚈𝙾𝚄𝚁 𝙲𝙰𝙿𝚃𝙸𝙾𝙽 𝚂𝙰𝚅𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 ✅**__")

    
@Client.on_message(filters.private & filters.command('del_caption') & filters.user(ADMINS))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("Note: Lazy_Mode active ✅\n\n😔**Sorry sweetheart ! No Caption found...**😔")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**** Your Caption deleted successfully**✅️")
                                       
@Client.on_message(filters.private & filters.command('see_caption') & filters.user(ADMINS))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Note: Lazy_Mode active ✅\n\nYour Caption:-**\n\n`{caption}`")
    else:
       await message.reply_text("😔**Sorry ! No Caption found...**😔")


# Rename

@Client.on_callback_query(filters.regex('rename'))
async def rename(bot,update):
	user_id = update.message.chat.id
	date = update.message.date
	await update.message.delete()
	await update.message.reply_text("»»——— 𝙋𝙡𝙚𝙖𝙨𝙚 𝙚𝙣𝙩𝙚𝙧 𝙣𝙚𝙬 𝙛𝙞𝙡𝙚 𝙣𝙖𝙢𝙚...",	
	reply_to_message_id=update.message.reply_to_message.id,  
	reply_markup=ForceReply(True))  

@Client.on_callback_query(filters.regex("upload"))
async def doc(bot, update):    
    new_name = update.message.text
    new_filename = new_name.split(":-")[1]
    file_path = f"downloads/{new_filename}"
    file = update.message.reply_to_message

    ms = await update.message.edit("Tʀyɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅɪɴɢ....")    
    try:
     	path = await bot.download_media(message=file, file_name=file_path, progress=progress_for_pyrogram,progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))                    
    except Exception as e:
     	return await ms.edit(e)
     	     
    duration = 0
    try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
           duration = metadata.get('duration').seconds
    except:
        pass
    ph_path = None
    user_id = int(update.message.chat.id) 
    media = getattr(file, file.media.value)
    c_caption = await db.get_caption(update.message.chat.id)
    c_thumb = await db.get_thumbnail(update.message.chat.id)

    if c_caption:
         try:
             caption = c_caption.format(filename=new_filename, filesize=humanbytes(media.file_size), duration=convert(duration))
         except Exception as e:
             return await ms.edit(text=f"Yᴏᴜʀ Cᴀᴩᴛɪᴏɴ Eʀʀᴏʀ Exᴄᴇᴩᴛ Kᴇyᴡᴏʀᴅ Aʀɢᴜᴍᴇɴᴛ ●> ({e})")             
    else:
         caption = f"**{new_filename}**"
 
    if (media.thumbs or c_thumb):
         if c_thumb:
             ph_path = await bot.download_media(c_thumb) 
         else:
             ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")

    await ms.edit("Tʀyɪɴɢ Tᴏ Uᴩʟᴏᴀᴅɪɴɢ....")
    type = update.data.split("_")[1]
    try:
        if type == "document":
            await bot.send_document(
                update.message.chat.id,
                document=file_path,
                thumb=ph_path, 
                caption=caption, 
                progress=progress_for_pyrogram,
                progress_args=("Uᴩʟᴏᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
        elif type == "video": 
            await bot.send_video(
		update.message.chat.id,
	        video=file_path,
	        caption=caption,
		thumb=ph_path,
		duration=duration,
	        progress=progress_for_pyrogram,
		progress_args=("Uᴩʟᴏᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
        elif type == "audio": 
            await bot.send_audio(
		update.message.chat.id,
		audio=file_path,
		caption=caption,
		thumb=ph_path,
		duration=duration,
	        progress=progress_for_pyrogram,
	        progress_args=("Uᴩʟᴏᴅ Sᴛᴀʀᴛᴇᴅ....", ms, time.time()))
    except Exception as e:          
        os.remove(file_path)
        if ph_path:
            os.remove(ph_path)
        return await ms.edit(f" Eʀʀᴏʀ {e}")
 
    await ms.delete() 
    os.remove(file_path) 
    if ph_path: os.remove(ph_path)
