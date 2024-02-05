from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto
from pyrogram import Client, filters, enums 
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from Script import script
import random
from info import *

@Client.on_callback_query()
async def callbackss(client: Client, query: CallbackQuery):
    if query.data == "s_y":
      buttons = [
        [
          InlineKeyboardButton('1988', callback_data='1988'),
          InlineKeyboardButton('1993', callback_data='1993'),
          InlineKeyboardButton('1997', callback_data='1997'),
          InlineKeyboardButton('1998', callback_data='1998')
        ],
        [
          InlineKeyboardButton('2000', callback_data='2000'),
          InlineKeyboardButton('2002', callback_data='2002'),
          InlineKeyboardButton('2008', callback_data='2008'),
          InlineKeyboardButton('2009', callback_data='2009')
        ],
        [
          InlineKeyboardButton('2011', callback_data='2011'),
          InlineKeyboardButton('2013', callback_data='2013'),
          InlineKeyboardButton('2015', callback_data='2015'),
          InlineKeyboardButton('2017', callback_data='2017')
        ],
        [
          InlineKeyboardButton('2018', callback_data='2018'),
          InlineKeyboardButton('2019', callback_data='2019'),
          InlineKeyboardButton('2020', callback_data='2020'),
          InlineKeyboardButton('2021', callback_data='2021')
        ],
        [
          InlineKeyboardButton('2022', callback_data='2022'),
          InlineKeyboardButton('2023', callback_data='2023'),
          InlineKeyboardButton('2024', callback_data='2024')
        ]
      ]
      reply_markup = InlineKeyboardMarkup(buttons)
      await query.message.edit_text(
                text=(script.SERIALS_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      )
    elif query.data == "1988":
        buttons = [[
            InlineKeyboardButton('Luv Kush - Uttar Ramayan', callback_data='lk'),
            InlineKeyboardButton('Back', callback_data='s_y')
	]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )  
    elif query.data == "lk":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='1988')
	]]
        await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto("https://graph.org/file/d3553fb949c9cfab3fb50.jpg")
	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.LUV_KUSH),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        ) 
    elif query.data == "1993":
        buttons = [[
            InlineKeyboardButton('Shri Krishna', callback_data='sk'),
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
	)
    elif query.data == "sk":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='1993')
        ]]
        await client.edit_message_media(
                query.message.chat.id, 
                query.message.id, 
                InputMediaPhoto("https://graph.org/file/0ffb1cc06d35e917a72ec.jpg")
	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.SHRI_KRISHNA),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "1997":
        buttons = [[
            InlineKeyboardButton('Jai Hanuman', callback_data='jh'),
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "jh":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='1997')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/f3fb3fba71030631a4e81.jpg")
	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.JAI_HANUMAN),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "1998":
        buttons = [[
            InlineKeyboardButton('Mahabharat', callback_data='mbold'),
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "mbold":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='1998')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/88762f9036355fa959ebe.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.MAHABHARAT_OLD),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2000":
        buttons = [[
            InlineKeyboardButton('Jai Mahalakshmi', callback_data='jml'),
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
	)
    elif query.data == "jml":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2000')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/3aed764415d92f44b4bea.jpg")
	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.JAI_MAHALAKSHMI),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2002":
        buttons = [[
            InlineKeyboardButton('Shiv Mahapuran', callback_data='smp'),
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
	)
    elif query.data == "smp":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2002')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/abbab43f9d7473e05758f.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.SHIV_MAHAPURAN),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2008":
        buttons = [[
            InlineKeyboardButton('Meera', callback_data='meera'),
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "meera":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2008')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/c13f98a2af41bdaf30b7b.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.MEERA),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2009":
        buttons = [[
            InlineKeyboardButton('Little Krishna', callback_data='lk'),
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "lk":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2009')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/0b5ff7755e95673536e78.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.LITTLE_KRISHNA),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2011":
        buttons = [[
            InlineKeyboardButton('Dwarkadheesh', callback_data='dk')
	],[
	    InlineKeyboardButton('Devon Ke Dev Mahadev', callback_data='dkdm')
      	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "dk":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2011')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/65e79f235e9f6e3994803.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.DWARKADHEESH),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "dkdm":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2011')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/c8792929b6c9c51f8d53d.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.DKDM),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2013":
        buttons = [[
            InlineKeyboardButton('Buddha', callback_data='buddha')
      	],[
	    InlineKeyboardButton('MahaBharat', callback_data='mbnew')
      	],[
	    InlineKeyboardButton('The Adventures Of Hatim', callback_data='hatim')
      	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "buddha":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2013')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/fc9f80637d3f8aaf79e67.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.BUDDHA),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "mbnew":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2013')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/e5ca05fe7811cce8bc06d.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.MAHABHARAT_NEW),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "hatim":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2013')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/2683af8ab72dc938998c5.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.HATIM),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2015":
        buttons = [[
            InlineKeyboardButton('Suryaputra Karn', callback_data='spk')
      	],[
	    InlineKeyboardButton('Siya Ke Ram', callback_data='skr')
	],[
	    InlineKeyboardButton('Krishna Balram', callback_data='kb')
	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "spk":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2015')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/a303009efbe2d55349a65.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.SURYAPUTRA_KARN),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "skr":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2015')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/3cce014e6279ea52c3708.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.SIYA_KE_RAM),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "kb":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2015')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/c21949b0ae9807708335f.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.KRISHNA_BALRAM),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2017":
        buttons = [[
            InlineKeyboardButton('Maa Shakti', callback_data='ms')
      	],[
	    InlineKeyboardButton('Kaise Bane Mushak Ganeshji Ki Savari?', callback_data='gks')
      	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "ms":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2017')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/7b7e60b561a16f6857275.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.MAA_SHAKTI),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "gks":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2017')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/470dac3c0e65c5eed7a21.jpg")
	      )
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.KBM_GANESH_KI_SAVARI),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2018":
        buttons = [[
            InlineKeyboardButton('Radhakrishn', callback_data='rk')
	],[
	    InlineKeyboardButton('Karn Sangini', callback_data='ks')
      	],[
	    InlineKeyboardButton('Mahishasura Vadh', callback_data='msv')
      	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "rk":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2018')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/c09a16c11c1884c796dbe.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.RADHAKRISHN),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "ks":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2018')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/50ea0516d60999f35242b.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.KARN_SANGINI),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "msv":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2018')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/7af01579618500b57dc65.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.M_VADH),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2019":
        buttons = [[
            InlineKeyboardButton('Jag Jaanani Maa Vaishnodevi', callback_data='jjmv')
	],[
	    InlineKeyboardButton('Shrimad Bhagwat Mahapuran', callback_data='sbm')
	],[
	    InlineKeyboardButton('Namah Lakshmi Narayan', callback_data='nln')
	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "jjmv":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2019')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/4d6913668505348784ead.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.JJMV),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "sbm":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2019')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/82ec44ab0f292cf29591d.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.SB_MAHAPURAN),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "nln":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2019')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/427fd328a6b94461bbb3f.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.NAMAH),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2020":
        buttons = [[
            InlineKeyboardButton('Deva Shree Ganesha', callback_data='dsg')
	],[
	InlineKeyboardButton('Devi Adi Parashakti', callback_data='dap')
      	],[
      	    InlineKeyboardButton('Kahat Hanuman Jaishree Ram', callback_data='khjr')
      	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "dsg":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2020')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/24994b6166b85a7e1c96d.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.DEVA_SHREE_GANESHA),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "dap":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2020')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.DEV_ADI_PARASHAKTI),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "khjr":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2020')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/a46696b76e2ee9440dc89.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.KAHAT_HANUMAN_JSRAM),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2021":
        buttons = [[
            InlineKeyboardButton('Baal Shiv', callback_data='bs')
      	],[
      	    InlineKeyboardButton('Kashibai', callback_data='kashibai')
      	],[
      	    InlineKeyboardButton('Jai Kanhaiya Lal Ki', callback_data='jklk')
      	],[
      	    InlineKeyboardButton('The Legend of Hanuman', callback_data='tloh')
      	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "bs":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2021')
        ]]
	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/3a3956ba102dd741dc5fb.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.BAAL_SHIV),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "jklk":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2021')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.JKLK),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "kashibai":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2021')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/1ecc1d194e9b91fe752b7.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.KASHIBAI),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "tloh":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2021')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.THE_LEGEND_OF_HANUMAN),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2022":
        buttons = [[
            InlineKeyboardButton('Brij Ke Gopal', callback_data='bkg')
	],[
	    InlineKeyboardButton('Dharm Yoddha Garud', callback_data='dyg')
      	],[
      	    InlineKeyboardButton('Parshuram', callback_data='parshuram')
      	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "bkg":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2022')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.BRIJ_KE_GOPAL),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "dyg":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2022')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/2e35179341f18dd6423b7.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.GARUD),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "parshuram":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2022')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.PARSHURAM),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2023":
        buttons = [[
            InlineKeyboardButton('Karmadhikari Shanidev', callback_data='kshanidev')
	],[
	    InlineKeyboardButton('Shiv Shakti', callback_data='ss')
      	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "kshanidev":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2023')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/472d0c8c6d048830a8473.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.K_SHANIDEV),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "ss":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2023')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/548ea31088580deb76bb4.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.SHIV_SHAKTI),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "2024":
        buttons = [[
            InlineKeyboardButton('Shrimad Ramayan', callback_data='s_r')
      	],[
	    InlineKeyboardButton('Prachand Ashok', callback_data='pa')
	],[
      	    InlineKeyboardButton('Chiranjeevi Hanuman', callback_data='ch')
      	],[
            InlineKeyboardButton('Back', callback_data='s_y')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.Y_TXT),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "s_r":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2024')
        ]]
      	await client.edit_message_media(query.message.chat.id, query.message.id, InputMediaPhoto("https://graph.org/file/fd5de18e1e0978b9850d3.jpg")
      	)
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.SHRIMAD_RAMAYAN),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "ch":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2024')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.C_HANUMAN),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
      	)
    elif query.data == "pa":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2024')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
                text=(script.P_ASHOK),
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
        )
