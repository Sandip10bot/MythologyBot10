class script(object):
    START_TXT = """<b>Hey {}</b> 👋🏻\n\nWelcome To <b>𝕽α∂нαкяιѕнη</b>.\nHere You Can Find Many <b>Mythology</b> Serials ➺ <b>Use</b> /serials.\n\n<b>Just Check Help Button For More Info</b>!!."""

    ABOUT_TXT = """--> My Name : {}
   
• <b>Devoloped By</b> : @MythoSerial ❤️
This bot can Provide You Many Mythology show on your request.\n\nThank You 😇.
"""
                  
    DISCLAIMER_TXT =  """<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪᴅᴅᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.
</b>"""

    SOURCE_TXT = """
<b>Hᴇʏ, Tʜɪs ɪs ᴀ Oᴘᴇɴ Sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ.

Tʜɪs Bᴏᴛ ʜᴀs Lᴀᴛᴇsᴛ ᴀɴᴅ Aᴅᴠᴀɴᴄᴇᴅ Fᴇᴀᴛᴜʀᴇs⚡️

Fork our repository and give star ⭐- <a href='https://github.com/Kushalhk/AutoFilter'>📥 ᴄʟɪᴄᴋ ʜᴇʀᴇ 📥</a></b>
"""
    
    KUSHAL_TXT = """ 
<b>🔥 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🔥

➻ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ
➻ ᴅɪʀᴇᴄᴛ ғɪʟᴇs
➻ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ
➻ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ
➻ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs
➻ ғᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ 
➻ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ ɪғ ᴀᴠᴀɪʟᴀʙʟᴇ

‼️ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄʜᴇᴄᴋ ᴀʟʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs ᴀɴᴅ ɪᴛ's ᴘʀɪᴄᴇs.</b>"""

    
    SETTINGS_TXT = """
Hᴇʟᴘ : <b>Sᴇᴛᴛɪɴɢꜱ</b>
    
◈ sᴇᴛᴛɪɴɢs ɪs ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ғᴇᴀᴛᴜʀᴇ ɪɴ ᴛʜɪs ʙᴏᴛ.
◈ ʏᴏᴜ ᴄᴀɴ ᴇᴀsɪʟʏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>Nᴏᴛᴇ :</b>
1. ᴏɴʟʏ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs.
2. ɪᴛ ᴡᴏʀᴋs ᴏɴʟʏ ᴡʜᴇɴ ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /connect - ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ʙᴏᴛ
• /settings - ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ """

    TELEGRAPH_TXT = """ Hᴇʟᴘ : <b>Tᴇʟᴇɢʀᴀᴘʜ</b>

<b>Nᴏᴛᴇ</b>: ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴘᴍꜱ. ᴀʟꜱᴏ ᴄᴀɴ ʙᴇ ᴜꜱᴇ ʙʏ ᴇᴠᴇʀʏᴏɴᴇ.

<b>Cᴏᴍᴍᴀɴᴅs & Usᴀɢᴇ :</b>
• /telegraph - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ 𝟻ᴍʙ"""

    FONT_TXT = """Hᴇʟᴘ : <b>Fᴏɴᴛ</b>

<b>Nᴏᴛᴇ</b>: ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛꜱ ꜱᴛʏʟᴇ, ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴍᴇ ʟɪᴋᴇ ᴛʜɪꜱ ꜰᴏʀᴍᴀᴛ. 

<code>/font TG_LINKS_CHANNEL</code>"""

    MANUELFILTER_TXT = """Hᴇʟᴘ : <b>Fɪʟᴛᴇʀꜱ</b>
    
◈ ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ.

<b>Nᴏᴛᴇ :</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /filter - ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
• /filters - ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ
• /del - ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)"""

    BUTTON_TXT = """Hᴇʟᴘ : <b>Bᴜᴛᴛᴏɴꜱ</b>
    
◈ ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.

<b>Nᴏᴛᴇ :</b>
𝟷. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
𝟸. ᴛʜɪꜱ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
𝟹. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ

ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ :
<code>[Button Text](buttonurl:https://t.me/TG_LINKS_CHANNEL)</code>

ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ :
<code>[Button Text](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""

    AUTOFILTER_TXT = """Hᴇʟᴘ : <b>Aᴜᴛᴏ Fɪʟᴛᴇʀ</b>
    
<b>Nᴏᴛᴇ :</b> Fɪʟᴇ Iɴᴅᴇx
𝟷. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ.
𝟸. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇꜱ.
𝟹. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇꜱ. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.

<b>Nᴏᴛᴇ :</b> Aᴜᴛᴏ Fɪʟᴛᴇʀ
𝟷. Aᴅᴅ ᴛʜᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
𝟸. Usᴇ /connect ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ ᴛʜᴇ ʙᴏᴛ.
𝟹. Usᴇ /settings ᴏɴ ʙᴏᴛ's ᴘᴍ ᴀɴᴅ ᴛᴜʀɴ ᴏɴ AᴜᴛᴏFɪʟᴛᴇʀ ᴏɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ."""

    
    HELP_TXT = """ <b>Help</b>

◈ <b> Search With Proper Format !! ✨ </b>

• <code>RadhaKrishn S1 E1</code> ✅
• <code>Mahabharat S01E01</code>  ✅

<b>More Use</b> /Serials

<b>➙ Don't Spam in Bot !!</b> 🚨

~ <b>Note 📍 :</b> ᴀʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀꜰᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇꜱ ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ."""

    CONNECTION_TXT = """Hᴇʟᴘ : <b>Cᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>
    
◈ ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴘᴍ ꜰᴏʀ ᴍᴀɴᴀɢɪɴɢ ꜰɪʟᴛᴇʀꜱ 
◈ ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

<b>Nᴏᴛᴇ :</b>
1. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. ꜱᴇɴᴅ /ᴄᴏɴɴᴇᴄᴛ ꜰᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴘᴍ

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /connect  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴘᴍ
• /disconnect  - ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ
• /connections - ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ"""

    EXTRAMOD_TXT = """Hᴇʟᴘ : <b>Exᴛʀᴀ Mᴏᴅᴜʟᴇs</b>
    
<b>Nᴏᴛᴇ :</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ꜰᴇᴀᴛᴜʀᴇꜱ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /id - ɢᴇᴛ ɪᴅ ᴏꜰ ᴀ ꜱᴘᴇᴄɪꜰɪᴇᴅ ᴜꜱᴇʀ.
• /info  - ɢᴇᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ.
• /imdb  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ.
• /search  - ɢᴇᴛ ᴛʜᴇ ꜰɪʟᴍ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ."""

    ADMIN_TXT = """<b>Nᴏᴛᴇ :</b> Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Wᴏʀᴋs Fᴏʀ Mʏ Aᴅᴍɪɴs.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /logs - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ
• /stats - ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏꜰ ꜰɪʟᴇꜱ ɪɴ ᴅʙ. <b>[Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</b>
• /delete - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.
• /users - ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.
• /chats - ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ
• /leave  - ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.
• /disable  -  ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.
• /ban  - ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ.
• /unban  - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.
• /channel - ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ. 
• /broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ. 
• /grp_broadcast - Tᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.
• /gfilter - ᴛᴏ ᴀᴅᴅ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs. 
• /gfilters - ᴛᴏ ᴠɪᴇᴡ ʟɪsᴛ ᴏғ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs. 
• /delg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ. 
• /request - ᴛᴏ sᴇɴᴅ ᴀ ᴍᴏᴠɪᴇ/sᴇʀɪᴇs ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴs. ᴏɴʟʏ ᴡᴏʀᴋs ᴏɴ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ. <b>[Tʜɪs Cᴏᴍᴍᴀɴᴅ Cᴀɴ Bᴇ Usᴇᴅ Bʏ Aɴʏᴏɴᴇ]</b>
• /delallg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢғɪʟᴛᴇʀs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.
• /deletefiles - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴄᴀᴍʀɪᴘ ᴀɴᴅ ᴘʀᴇ-ᴅᴠᴅ ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ."""

    STICKER_TXT = """<b>yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅᴀɴy  ꜱᴛɪᴄᴋᴇʀꜱ ɪᴅ.
• ᴜꜱᴀɢᴇ :ᴛᴏ ɢᴇᴛ ꜱᴛɪᴄᴋᴇʀ
 
⭕ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ
◉ Reply To Any Sticker [/stickerid]

/𝐬𝐭𝐢𝐜𝐤𝐞𝐫𝐢𝐝 𝐬𝐭𝐢𝐜𝐤𝐞𝐫 𝐢𝐝

</b>"""
 
    STATUS_TXT = """<b>⍟─────[ <b>Bᴏᴛ Sᴛᴀᴛᴜs</b> ]─────⍟
    
★ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ : <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : <code>{}</code>
★ ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ : <code>{}</code>
★ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code>
★ ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ : <code>{}</code>

•❅──────✧❅✦❅✧──────❅•</b>"""


    LOG_TEXT_G = """<b>#NewGroup
Gʀᴏᴜᴘ = {}(<code>{}</code>)
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}</b>"""

    LOG_TEXT_P = """<b>#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}</b>"""

    ALRT_TXT = """<b>ʜᴇʟʟᴏ {},
ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ʏᴏᴜʀ ᴍᴏᴠɪᴇ ʀᴇQᴜᴇꜱᴛ,
ʀᴇǫᴜᴇꜱᴛ ʏᴏᴜʀ'ꜱ...</b>"""

    OLD_ALRT_TXT = """<b>Search Again!</b>"""

    CUDNT_FND = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}
ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?</b>"""

    I_CUDNT = """<b>sᴏʀʀʏ ɴᴏ ꜰɪʟᴇs ᴡᴇʀᴇ ꜰᴏᴜɴᴅ ꜰᴏʀ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ {} 😕

Mᴏᴠɪᴇs Nᴏᴛ Aᴠᴀɪʟᴀʙʟᴇ Rᴇᴀsᴏɴ:
𝟷. ᴏ.ᴛ.ᴛ ᴏʀ ᴅᴠᴅ ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ
𝟸. ᴛʏᴘᴇ ɴᴀᴍᴇ ᴡɪᴛʜ ʏᴇᴀʀ
𝟹. ᴍᴏᴠɪᴇ ɪs ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ ʀᴇᴘᴏʀᴛ ᴛᴏ ᴀᴅᴍɪɴs @TG_Bots_Supporter</b>"""

    I_CUD_NT = """<b>ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ {}.
ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ꜱᴘᴇʟʟɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ ᴏʀ ɪᴍᴅʙ...</b>"""

    MVE_NT_FND = """<b>Not available!</b>"""

    TOP_ALRT_MSG = """<b>Cʜᴇᴄᴋɪɴɢ Iɴ Dᴀᴛᴀʙᴀsᴇ...</b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️</b>"""
    
    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠

ᴀꜰᴛᴇʀ 5 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ

ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ"""

    

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯

ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

ᴇxᴀᴍᴘʟᴇ : Loki S01E01

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)"""

    NORSLTS = """
★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★

𝗜𝗗 <b>: {}</b>

𝗡𝗮𝗺𝗲 <b>: {}</b>

𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>🥲"""

    CAPTION = """{f_caption}"""
    
#🗂 𝗙𝗶𝗹𝗲: <b><font class=smcp>{file_name}</font></b>
#📀 𝗦𝗶𝘇𝗲: <b><font class=smcp>{file_size}</font></b>

#<b>🔰 Cʀᴇᴀᴛᴏʀ : <a href="https://t.me/KUSHALHK">𝐊𝐔𝐒𝐇𝐀𝐋</a>
#🔰 Cʜᴀɴɴᴇʟ : <a href="https://t.me/TG_LINKS_CHANNEL">𝐌𝐎𝐕𝐈𝐄𝐒 𝐂𝐇𝐀𝐍𝐍𝐄𝐋</a>
#🔰 Gʀᴏᴜᴘ : <a href="https://t.me/movies_hub_official1">𝐌𝐎𝐕𝐈𝐄 𝐑𝐄𝐐𝐔𝐄𝐒𝐓 𝐆𝐑𝐎𝐔𝐏</a></b>"""
    
    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🧿 𝐓𝐈𝐓𝐋𝐄: <a href={url}>{title}</a>
🎭 𝐆𝐄𝐍𝐑𝐄𝐒: {genres}
📆 𝐘𝐄𝐀𝐑: <a href={url}/releaseinfo>{year}</a>
🌟 𝐑𝐀𝐓𝐈𝐍𝐆: <a href={url}/ratings>{rating}</a> / 10 (Based on {votes} user ratings)</b>
☀️ 𝐋𝐀𝐍𝐆𝐔𝐀𝐆𝐄 : <code>{languages}</code></a>
📀 𝐑𝐔𝐍𝐓𝐈𝐌𝐄: {runtime} Minutes</a>

<b>👨‍💼 Requested by : {message.from_user.mention}</b>"""

    
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    GFILTER_TXT = """Hᴇʟᴘ : <b>Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs</b>
    
◈ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.
    
<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /gfilter - Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.
• /gfilters - Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.
• /delg - Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.
• /delallg - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ."""
    
    FILE_STORE_TXT = """Hᴇʟᴘ : <b>Fɪʟᴇ Sᴛᴏʀᴇ</b>
    
◈ Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.

<b>Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ :</b>
• /batch - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.
• /link - ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.
• /pbatch - ᴊᴜsᴛ ʟɪᴋᴇ <code>/batch</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.
• /plink - ᴊᴜsᴛ ʟɪᴋᴇ <code>/link</code>, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ."""

    CHECK_TXT = """
<b>🔥 ᴄʜᴏᴏsᴇ ʏᴏᴜʀ sᴜɪᴛᴀʙʟᴇ ᴘʟᴀɴ ᴀɴᴅ ᴘᴀʏ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ғᴇᴇs ᴜsɪɴɢ ᴀɴʏ ᴜᴘɪ ᴀᴘᴘ. 

ᴘʟᴀɴ ᴀ : 𝟷 ᴡᴇᴇᴋ / ₹𝟷𝟻
ᴘʟᴀɴ ʙ : 𝟷 ᴍᴏɴᴛʜ / ₹𝟹𝟿
ᴘʟᴀɴ ᴄ : 𝟷 ʏᴇᴀʀ / ₹𝟹𝟼𝟶

➻ ᴜᴘɪ ɪᴅ : harikushal234@paytm

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    PLAN1_TXT = """
<b>🔥 ᴘᴀʏ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ғᴇᴇs ₹𝟷𝟻 ғᴏʀ 𝟷 ᴡᴇᴇᴋ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss ᴡɪᴛʜ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ. 

➻ ᴜᴘɪ ɪᴅ : harikushal234@paytm

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    PLAN2_TXT = """
<b>🔥 ᴘᴀʏ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ғᴇᴇs ₹𝟹𝟿 ғᴏʀ 𝟷 ᴍᴏɴᴛʜ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss ᴡɪᴛʜ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ. 

➻ ᴜᴘɪ ɪᴅ : harikushal234@paytm

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    PLAN3_TXT = """
<b>🔥 ᴘᴀʏ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ғᴇᴇs ₹𝟹𝟼𝟶 ғᴏʀ 𝟷 ʏᴇᴀʀ ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇss ᴡɪᴛʜ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ. 

➻ ᴜᴘɪ ɪᴅ : harikushal234@paytm

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>ᴠ𝟹.𝟶 [ Sᴛᴀʙʟᴇ ]</code></b>"""

# serials

    SERIALS_TXT = """<b>Select The Year To Get Serial !!</b>\n\n<b>For e.g Mahabharat Serial Released In 2013 You Can Select Year 2013 To Get That Serial</b> !! 🙆"""
    Y_TXT = """<b>Here Is Available Serials In These Year</b> !! 📅\n\n<b>Click Below 👇 To Choose Serials</b>"""
    
    LUV_KUSH = """<b>Uttar Ramayan</b> - Luv Kush Leela\n\n<b>Total Episode :</b> <code>39</code>\n\n<b>About :</b>Luv and Kush, the sons of Lord Rama and Sita, support their mother during her exile from Ayodhya. When they visit Ayodhya, a shocking truth is revealed to them.\n\n<b>How To Search Episode ⁉️</b>\n<code>Luv Kush S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    SHRI_KRISHNA = """<b>Shri Krishna</b>\n\n<b>Total Episode :</b> <code>221</code>\n\n<b>About :</b> When evil takes over the world, Lord Vishnu incarnates into the world as Shri Krishna for the protection of the righteous and the destruction of the wicked.\n\n<b>How To Search Episode ⁉️</b>\n<code>Shri Krishna S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!""" 
    JAI_HANUMAN = """<b>Jai Hanuman</b>\n\n<b>Total Episode :</b> <code>89</code>\n\n<b>About :</b> Jai Hanuman - Sankat Mochan Naam Tiharo is an Indian television mythology drama series that premiered from 23 August 2022 on Dangal TV. Produced by Alind Srivastava and Nissar Parvez under Peninsula Pictures, it stars Akshay Dogra, Madirakshi Mundle, Amar Upadhyay and Apara Mehta\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    MAHABHARAT_OLD = """"<b>Mahabharat (1998)</b>\n\n<b>Total Episode :</b> <code>94</code>\n\n<b>About :</b> When differences between the Kaurava and the Pandava clans, who belong to the same family line, lead them to the threshold of war, Lord Krishna decides to step in and take control of the situation.\n\n<b>How To Search Episode ⁉️</b>\n<code>Mahabharat 1988 S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    JAI_MAHALAKSHMI = """<b>Jai Mahalakshmi</b>\n\n<b>Total Episode :</b> <code>56</code>\n\n<b>About :</b> Goddess Lakshmi is the supreme goddess of wealth and prosperity, Devi Durga took the intense form of Mahalakshmi to protect the world when Lakshmi disappeared preceding Samudra Manthan.\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Mahalakshmi S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    SHIV_MAHAPURAN = """<b>Shiv Mahapuran</b>\n\n<b>Total Episode :</b> <code>61</code>\n\n<b>About :</b> The story of Indian God Shiv. It includes various stories of demons and Gods involved in Hindu Mythology.\n\n<b>How To Search Episode ⁉️</b>\n<code>Shiv Mahapuran S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    MEERA = """<b>Meera 2008</b>\n\n<b>Total Episode :</b> <code>134</code>\n\n<b>About :</b> Meera, a young Rajput princess, is overcome with love and devotion to Lord Krishna and sacrifices everything in her life to become a saint and poet.\n\n<b>How To Search Episode ⁉️</b>\n<code>Meera S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    LITTLE_KRISHNA = """<b>Little Krishna</b>\n\n<b>Total Episode :</b> <code>13</code>\n\n<b>About :</b> Little Krishna, a mischievous child, lives in the village of Vrindavan. He decides to save the villagers from an evil king, Kamsa, who sends ferocious demons upon them.\n\n<b>How To Search Episode ⁉️</b>\n<code>Little Krishna S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    DWARKADHEESH = """<b>Dwarkadheesh</b>\n\n<b>Total Episode :</b> <code>204</code>\n\n<b>About :</b> After becoming the king of Dwarka, Lord Krishna becomes a protector and maintains relationships with his family members and loved ones.\n\n<b>How To Search Episode ⁉️</b>\n<code>Dwarkadheesh S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    DKDM = """<b>Devon Ke Dev Mahadev</b>\n\n<b>Total Episode :</b> <code>820</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    BUDDHA = """<b>Buddha</b>\n\n<b>Total Episode :</b> <code>55</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    MAHABHARAT_NEW = """<b>MahaBharat (2013)</b>\n\n<b>Total Episode :</b> <code>267</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    HATIM = """<b>The Adventures Of Hatim</b>\n\n<b>Total Episode :</b> <code>68</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    SURYAPUTRA_KARN = """<b>Suryaputra Karn</b>\n\n<b>Total Episode :</b> <code>307</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    SIYA_KE_RAM = """<b>Siya Ke Ram</b>\n\n<b>Total Episode :</b> <code>304</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    KRISHNA_BALRAM = """<b>Krishna Balram</b>\n\n<b>Total Episode :</b> <code>65</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    MAA_SHAKTI = """<b>Maa Shakti</b>\n\n<b>Total Episode :</b> <code>78</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    KBM_GANESH_KI_SAVARI = """<b>Kaise Bane Mushak Ganeshji Ki Savari?</b>\n\n<b>Total Episode :</b> <code>8</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    RADHAKRISHN = """<b>Radhakrishn</b>\n\n<b>Total Episode :</b> <code>1145</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    KARN_SANGINI = """<b>Karn Sangini</b>\n\n<b>Total Episode :</b> <code>90</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    M_VADH = """<b>Mahishasura Vadh</b>\n\n<b>Total Episode :</b> <code>10</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    SB_MAHAPURAN = """<b>Shiv Mahapuran</b>\n\n<b>Total Episode :</b> <code>61</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    JJMV = """<b>Jag Jaanani Maa Vaishnodevi</b>\n\n<b>Total Episode :</b> <code>207</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    NAMAH = """<b>Namah Lakshmi Narayan</b>\n\n<b>Total Episode :</b> <code>65</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    DEVA_SHREE_GANESHA = """<b>Deva Shree Ganesha</b>\n\n<b>Total Episode :</b> <code>11</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    DEV_ADI_PARASHAKTI = """<b>Devi Adi Parashakti</b>\n\n<b>Total Episode :</b> <code>87</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    KAHAT_HANUMAN_JSRAM = """<b>Kahat Hanuman Jaishree Ram</b>\n\n<b>Total Episode :</b> <code>120</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    BAAL_SHIV = """<b>Baal Shiv</b>\n\n<b>Total Episode :</b> <code>215</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    JKLK = """<b>Jai Kanhaiya Lal Ki</b>\n\n<b>Total Episode :</b> <code>185</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    KASHIBAI = """<b>Kashibai</b>\n\n<b>Total Episode :</b> <code>201</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    THE_LEGEND_OF_HANUMAN = """<b>The Legend of Hanuman</b>\n\n<b>Total Episode :</b> <code>32</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    BRIJ_KE_GOPAL = """<b>Brij Ke Gopal</b>\n\n<b>Total Episode :</b> <code>48</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    GARUD = """<b>Dharm Yoddha Garud</b>\n\n<b>Total Episode :</b> <code>234</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    PARSHURAM = """<b>Parshuram</b>\n\n<b>Total Episode :</b> <code>160</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    K_SHANIDEV = """<b>Karmadhikari Shanidev</b>\n\n<b>Total Episode :</b> <code>39</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    SHIV_SHAKTI = """<b>Shiv Shakti</b>\n\n<b>Total Episode :</b> <code>Running...</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    SHRIMAD_RAMAYAN = """<b>Shrimad Ramayan</b>\n\n<b>Total Episode :</b> <code>Running...</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    C_HANUMAN = """<b>Chiranjeevi Hanuman</b>\n\n<b>Total Episode :</b> <code>Coming Soon..</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    P_ASHOK = """<b>Prachand Ashok</b>\n\n<b>Total Episode :</b> <code>Running...</code>\n\n<b>About :</b> paste\n\n<b>How To Search Episode ⁉️</b>\n<code>Jai Hanuman S01E01</code>\n\n<b>Uploaded By</b> : @Radhekrishn_bot !!"""
    LOGO = """
 ____  ___    ____   __  ____  ____ 
(_  _)/ __)  (  _ \ /  \(_  _)(__  )
  )( ( (_ \   ) _ ((  O ) )(   / _/ 
 (__) \___/  (____/ \__/ (__) (____)"""
