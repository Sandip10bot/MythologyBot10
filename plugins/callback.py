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
	await query.message.edit_text(text=(script.DEV_ADI_PARASHAKTI), reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
    
    elif query.data == "khjr":
        buttons = [[
            InlineKeyboardButton('Back', callback_data='2020')
        ]]
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
