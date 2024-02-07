class script(object):
    START_TXT = """<b>Hey {}</b> 👋🏻
    
Welcome To <b>𝕽α∂нαкяιѕнη</b> 😇
Here You Can Find Many <b>Mythology</b> Serials.
    
➺ <b>Use</b>: /serials. •
    
<b>👇 Check Help Button For More Info</b>!!.
    """

    ABOUT_TXT = """--> My Name : {}
   
• <b>Devoloped By</b> : @Sandip10x ❤️
This bot can Provide You Many Mythology show on your request.

• <b>Join Update Channel:</b> (t.me/Radhakriishn) ✨
Thank You 😇.
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

<code>/font Text</code>"""

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

    
    HELP_TXT = """<b><u>Help Message</u></b>

◈ <b>Search With Proper Format !! ✨</b>

• <code>RadhaKrishn S1 E1</code> ✅
• <code>Mahabharat S01E01</code> ✅
• 

<b>See List of All Serials:</b> /serials

<b>➙ Please Don't Spam in Bot !!</b> 🚨

~ <b><u>Note</u> 📍:</b> All Files will delete after 10 minutes to avoid copyright issues."""

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
    Y_TXT = """<b>Here Is Available Serials In These Year</b> !!📅\n\n<b>Click Below 👇 To Choose Serials</b>"""
    
    LUV_KUSH = """<b>Uttar Ramayan</b> - Luv Kush Leela ✨
    
<b>Total Episode :</b> <code>39</code>

<b>About :</b> Luv and Kush, the sons of Lord Rama and Sita, support their mother during her exile from Ayodhya. When they visit Ayodhya, a shocking truth is revealed to them.

<b>How To Search Episode ⁉️</b>
<code>Luv Kush S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SHRI_KRISHNA = """<b>Shri Krishna</b> ✨
    
<b>Total Episode :</b> <code>221</code>

<b>About :</b> When evil takes over the world, Lord Vishnu incarnates into the world as Shri Krishna for the protection of the righteous and the destruction of the wicked.

<b>How To Search Episode ⁉️</b>
<code>Shri Krishna S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JAI_HANUMAN = """<b>Jai Hanuman</b> ✨
    
<b>Total Episode :</b> <code>89</code>

<b>About :</b> Jai Hanuman - Sankat Mochan Naam Tiharo is an Indian television mythology drama series that premiered from 23 August 2022 on Dangal TV. Produced by Alind Srivastava and Nissar Parvez under Peninsula Pictures, it stars Akshay Dogra, Madirakshi Mundle, Amar Upadhyay and Apara Mehta.

<b>How To Search Episode ⁉️</b>
<code>Jai Hanuman S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    MAHABHARAT_OLD = """<b>Mahabharat (1998)</b> ✨
    
<b>Total Episode :</b> <code>94</code>

<b>About :</b> When differences between the Kaurava and the Pandava clans, who belong to the same family line, lead them to the threshold of war, Lord Krishna decides to step in and take control of the situation.

<b>How To Search Episode ⁉️</b>
<code>Mahabharat 1988 S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JAI_MAHALAKSHMI = """<b>Jai Mahalakshmi</b> ✨
    
<b>Total Episode :</b> <code>56</code>

<b>About :</b> Goddess Lakshmi is the supreme goddess of wealth and prosperity, Devi Durga took the intense form of Mahalakshmi to protect the world when Lakshmi disappeared preceding Samudra Manthan.

<b>How To Search Episode ⁉️</b>
<code>Jai Mahalakshmi S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JAI_MAHALAKSHMI = """<b>Shiv Mahapuran</b> ✨
    
<b>Total Episode :</b> <code>61</code>

<b>About :</b> The story of Indian God Shiv. It includes various stories of demons and Gods involved in Hindu Mythology.

<b>How To Search Episode ⁉️</b>
<code>Shiv Mahapuran S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    MEERA = """<b>Meera 2008</b> ✨
    
<b>Total Episode :</b> <code>134</code>

<b>About :</b> Meera, a young Rajput princess, is overcome with love and devotion to Lord Krishna and sacrifices everything in her life to become a saint and poet.

<b>How To Search Episode ⁉️</b>
<code>Meera S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    LITTLE_KRISHNA = """<b>Little Krishna</b> ✨
    
<b>Total Episode :</b> <code>13</code>

<b>About :</b> Little Krishna, a mischievous child, lives in the village of Vrindavan. He decides to save the villagers from an evil king, Kamsa, who sends ferocious demons upon them.

<b>How To Search Episode ⁉️</b>
<code>Little Krishna S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    DWARKADHEESH = """<b>Dwarkadheesh</b> ✨
    
<b>Total Episode :</b> <code>204</code>

<b>About :</b> After becoming the king of Dwarka, Lord Krishna becomes a protector and maintains relationships with his family members and loved ones.

<b>How To Search Episode ⁉️</b>
<code>Dwarkadheesh S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    DKDM = """<b>Devon Ke Dev Mahadev</b> ✨
    
<b>Total Episode :</b> <code>820</code>

<b>About :</b> Lord Shiva, an ascetic, and his divine consort, Goddess Shakti, create the universe. However, they separate for the sake of it and are reunited when she is reincarnated as Goddess Parvati.

<b>How To Search Episode ⁉️</b>
<code>Devon ke Dev Mahadev S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    BUDDHA = """<b>Buddha</b> ✨
    
<b>Total Episode :</b> <code>55</code>

<b>About :</b> Prince Siddhartha's father shelters him from witnessing the sufferings of life. However, being curious by nature, he comes across the various stages of suffering and sets out to attain enlightenment.

<b>How To Search Episode ⁉️</b>
<code>Buddha S01 E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    MAHABHARAT_NEW = """<b>MahaBharat (2013)</b> ✨
    
<b>Total Episode :</b> <code>267</code>

<b>About :</b> The mother of all wars, the epitome of all rivalries, the cauldron of emotions, insecurities, jealousies, and power play - Mahabharat!

<b>How To Search Episode ⁉️</b>
<code>Mahabharat S01E01 HS</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    HATIM = """<b>The Adventures Of Hatim</b> ✨
    
<b>Total Episode :</b> <code>68</code>

<b>About :</b> Hatim, the Prince of Yemen, lives a graceful life. However, things change when he has to solve the seven riddles to defeat the wicked sorcerer Zargam.

<b>How To Search Episode ⁉️</b>
<code>Hatim S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SURYAPUTRA_KARN = """<b>Suryaputra Karn</b> ✨
    
<b>Total Episode :</b> <code>307</code>

<b>About :</b> Karna, son of Surya and Kunti and the doyen of archers, endures a challenging journey on his way to becoming one of the greatest warriors of the Mahabharata.

<b>How To Search Episode ⁉️</b>
<code>Suryaputra karn E1</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SIYA_KE_RAM = """<b>Siya Ke Ram</b> ✨
    
<b>Total Episode :</b> <code>304</code>

<b>About :</b> After their marriage, Rama and Shinta must go into exile because Queen Kaikeyi wants her son Bharata to assume the throne. Their relationship is tested again when Shinta is kidnapped by Rahwana.

<b>How To Search Episode ⁉️</b>
<code>Siya ke ram S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KRISHNA_BALRAM = """<b>Krishna Balram</b> ✨
    
<b>Total Episode :</b> <code>65</code>

<b>About :</b> Follow through the thrilling capers and chilling escapades of Krishna and Balram, with Radha, and friends in this all new, action packed, adrenaline churning series.

<b>How To Search Episode ⁉️</b>
<code>Krishna Balram S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    MAA_SHAKTI = """<b>Maa Shakti</b> ✨
    
<b>Total Episode :</b> <code>78</code>

<b>About :</b> Take a look at the depiction of Maa Shakti who is known as the divine force in Hinduism. She is considered the source of power and creation and can transform herself into various forms.

<b>How To Search Episode ⁉️</b>
<code>Maa Shakti S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KBM_GANESH_KI_SAVARI = """<b>Kaise Bane Mushak Ganeshji Ki Savari?</b> ✨
    
<b>Total Episode :</b> <code>08</code>

<b>About :</b> Ganesh arrives in Devlok and engages in a fierce battle with Mushikasur. Ganesh seeks Somnandi's help to fight Mushikasur and his army of mice...

<b>How To Search Episode ⁉️</b>
<code>KBMGKS S01 E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    RADHAKRISHN = """<b>Radhakrishn (2018)</b> ✨
    
<b>Total Episode :</b> <code>1145</code>

<b>About :</b> Lord Krishna and Radha share pure love for one another but things take a turn when Radha receives a curse that she will be separated from him.

<b>How To Search Episode ⁉️</b>
<code>Radhakrishn S1 E1</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KARN_SANGINI = """<b>Karn Sangini</b> ✨
    
<b>Total Episode :</b> <code>90</code>

<b>About :</b> Urvi is a princess of noble birth and her parents want her to marry her childhood friend Arjun. However, she falls for the Karna, a man of low caste and invites a whole set of problems.

<b>How To Search Episode ⁉️</b>
<code>Karn Sangini S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    M_VADH = """<b>Mahishasura Vadh</b> ✨
    
<b>Total Episode :</b> <code>10</code>

<b>About :</b> Mahishasura Vadh is a mini-series based on the remarkable story of how Goddess Durga killed the powerful buffalo demon Mahishasura, exemplifying...

<b>How To Search Episode ⁉️</b>
<code>Mahishasur vadh S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SB_MAHAPURAN = """<b>Shrimad Bhagwat Mahapuran</b> ✨
    
<b>Total Episode :</b> <code>00</code>

<b>About :</b> In a divine discourse with Radha, Lord Krishna takes it upon himself to explain texts from the ancient and fabled Srimad Bhagwat, sacred in Hinduism, which offers mankind profound spiritual knowledge.

<b>How To Search Episode ⁉️</b>
<code>Shrimad Bhagwat Mahapuran S01 E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JJMV = """<b>Jag Jaanani Maa Vaishnodevi</b> ✨
    
<b>Total Episode :</b> <code>207</code>

<b>About :</b> The goddesses combine their powers to create Goddess Vaishnodevi and task her with the responsibility of destroying the forces of evil that threaten to destroy Earth.

<b>How To Search Episode ⁉️</b>
<code>Jag Jaanani Maa Vaishnodevi S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    NAMAH = """<b>Namah Lakshmi Narayan</b> ✨
    
<b>Total Episode :</b> <code>65</code>

<b>About :</b> Eternal friends Lord Mahadev and Lord Narayan are quite different from each other but maintain a harmonious relationship. Soon, things change as their bond is challenged by the arrival of Kalyug.

<b>How To Search Episode ⁉️</b>
<code>Namah Laxmi Narayan S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    DEVA_SHREE_GANESHA = """<b>Deva Shree Ganesha</b> ✨
    
<b>Total Episode :</b> <code>11</code>

<b>About :</b> People celebrate Ganesh Chaturthi, which is dedicated to Lord Ganesh, the remover of obstacles. Devotees bring home idols and adorn them with garlands, perform 'aartis' and distribute sweets.

<b>How To Search Episode ⁉️</b>
<code>Deva Shree Ganesha S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    DEV_ADI_PARASHAKTI = """<b>Devi Adi Parashakti</b> ✨
    
<b>Total Episode :</b> <code>87</code>

<b>About :</b> Devi Adi Parashakti, the goddess of the universe, takes various forms on Earth in order to guide mankind towards humanity and compassion.

<b>How To Search Episode ⁉️</b>
<code>Devi Adi Parashakti S01E01 </code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KAHAT_HANUMAN_JSRAM = """<b>Kahat Hanuman Jaishree Ram</b> ✨
    
<b>Total Episode :</b> <code>120</code>

<b>About</b> : Hanuman, a beloved deity in Hinduism, conquers various obstacles and overcomes insurmountable challenges in his quest to rid the world of evil.

<b>How To Search Episode ⁉️</b>
<code>Kahat Hanuman S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    BAAL_SHIV = """<b>Baal Shiv</b> ✨
    
<b>Total Episode :</b> <code>215</code>

<b>About</b> : Lord Shiva in his younger avatar, faces several challenges as he strives to uphold justice in his realm and facilitates the destruction of evil forces.

<b>How To Search Episode ⁉️</b>
<code>Baal Shiv S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    JKLK = """<b>Jai Kanhaiya Lal Ki</b> ✨
    
<b>Total Episode :</b> <code>185</code>

<b>About</b> : Young Krishna grows up with a strong bond with his mother, Devaki, and his foster-mother, Yashoda. However, his power and strength are tested when he must protect his family and village from the evil Kans.

<b>How To Search Episode ⁉️</b>
<code>Jai kanhaiya Lal ki S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    KASHIBAI = """<b>Kashibai</b> ✨
    
<b>Total Episode :</b> <code>201</code>

<b>About</b> : Kashibai is raised as a spoiled child. She faces challenges as an adult when her husband Peshwa works to expand the Maratha empire and she must prove her capabilities to become an administrator.

<b>How To Search Episode ⁉️</b>
<code>Kashibai S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    THE_LEGEND_OF_HANUMAN = """<b>The Legend of Hanuman</b> ✨
    
<b>Total Episode :</b> <code>32</code>

<b>About</b> : Lord Mahadev is reborn as Hanuman to serve Lord Rama, and becomes a beacon of hope amidst the harrowing darkness.

<b>How To Search Episode ⁉️</b>
<code>The Legend of Hanuman S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    BRIJ_KE_GOPAL = """<b>Brij Ke Gopal</b> ✨
    
<b>Total Episode :</b> <code>48</code>

<b>About</b> : Lord Krishna incarnates as a human on Earth to end the agony of his devotees and battle against evil, restoring the faith of people in good.

<b>How To Search Episode ⁉️</b>
<code>Brij ke Gopal S1 Episode 1</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    GARUD = """<b>Dharm Yoddha Garud</b> ✨
    
<b>Total Episode :</b> <code>234</code>

<b>About</b> : Garud, a mighty warrior, strives to maintain peace and fights injustice. He faces off powerful adversaries while protecting and helping those in need.

<b>How To Search Episode ⁉️</b>
<code>Garud S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    PARSHURAM = """<b>Parshuram</b> ✨
    
<b>Total Episode :</b> <code>160</code>

<b>About</b> : Parashurama, the sixth incarnation of the God Vishnu, comes to Earth with the sole purpose of fighting off all evil and protecting humans.

<b>How To Search Episode ⁉️</b>
<code>Parshuram S01 E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    K_SHANIDEV = """<b>Karmadhikari Shanidev</b> ✨
    
<b>Total Episode :</b> <code>39</code>

<b>About</b> : Karmadhikari Shanidev is an Indian Mythology television series produced by Triangle Film Company and premiered on 11 December 2023 on Shemaroo TV.

<b>How To Search Episode ⁉️</b>
<code>Karmadhikari Shanidev S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SHIV_SHAKTI = """<b>Shiv Shakti</b> ✨
    
<b>Total Episode :</b> <code>Running...</code>

<b>About</b> : Lord Shiva and his wife, Goddess Parvati, navigate their relationship and duties and offer sacrifices and brave separation to selflessly care for humanity.

<b>How To Search Episode ⁉️</b>
<code>Shiv Shakti S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    SHRIMAD_RAMAYAN = """<b>Shrimad Ramayan</b> ✨
    
<b>Total Episode :</b> <code>Running...</code>

<b>About</b> : A religious leader reads out the Ramayana and explains it to a large gathering of devotees in a brief, simple and easy-to-understand manner.

<b>How To Search Episode ⁉️</b>
<code>Shrimad Ramayan S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    P_ASHOK = """<b>Prachand Ashok</b> ✨
    
<b>Total Episode :</b> <code>Running...</code>

<b>About</b> : Prachand Ashoka is an upcoming historical soap opera produced by Balaji Telefilms. It stars Adnan Khan, Simba Nagpal, Tanusri Dasgupta and Mallika Singh. The serial story is based on the story of Emperor Ashoka. The show will be aired on Colors TV in January 2024.

<b>How To Search Episode ⁉️</b>
<code>Pracchand Ashok S01E01</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    C_HANUMAN = """<b>Chiranjeevi Hanuman</b> ✨
    
<b>Total Episode :</b> <code>Coming Soon...</code>

<b>About</b> : Coming Soon

<b>How To Search Episode ⁉️</b>
<code>Not Released Yet !!</code>

~ just copy the above and paste it below. ~ 
<b>Uploaded By</b> : @Radhekrishn_bot !!
"""
    LOGO = """
 ____  ___    ____   __  ____  ____ 
(_  _)/ __)  (  _ \ /  \(_  _)(__  )
  )( ( (_ \   ) _ ((  O ) )(   / _/ 
 (__) \___/  (____/ \__/ (__) (____)"""
