class script(object):
    START_TXT = """<b>היי {} אני בוט סרטים מתקדם במיוחד שלח לי שם של סרט במדויק ואני יספק לך את הסרטים באיכות מדהימה 👇</b>"""

    HELP_TXT = """<b>היי {} סתם בשביל היופי 👇</b>"""

    PRIVATEBOT_TXT = """<b>Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ

- ›› Mᴜsᴛ Aᴅᴅ Mᴇ Aᴅᴍɪɴ Tᴏ Wᴏʀᴋ Oɴ Tʜɪs Gʀᴏᴜᴘ

- ›› Cʜᴀɴɢᴇ Sᴇᴛᴛɪɴɢ Fᴏʀ Uʀ Gʀᴏᴜᴘ Cʟɪᴄᴋ 👉 /connect

- ›› I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇs/Sᴇʀɪᴇs Dᴏɴ'ᴛ Wᴏʀʀʏ

- ›› Eɴᴊᴏʏ !! Mᴏʀᴇ Iɴғᴏ Usᴇ Uɴᴅᴇʀ Bᴜᴛᴛᴏɴs</b>
"""

    MODS_TXT = """I Hᴀᴠᴇ Mᴀɴʏ Fᴇᴀᴛᴜʀᴇs"""

    PONGD_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""
    
    PONG_TXT = """Cʜᴇᴄᴋ Mʏ Pɪɴɢ Bʏ Cʟɪᴄᴋɪɴɢ 👉 /ping"""

    ABOUT_TXT = """<b>🤖 רובוט מתקדם : <a href=https://t.me/il_333>ᴍᴏᴠɪᴇs ғɪʟᴛᴇʀ ʙᴏᴛ</a>
👨‍💻 מתכנת : <a href=https://t.me/Mods1234>@Mods1234</a>
📝 שפה : ᴘʏʀᴏɢʀᴀᴍ
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3
📡 אוחסן : ғʀᴇᴇ ʜᴏsᴛɪɴɢ
📢 תמיכה בנושא הבוט : <a href=https://t.me/il_334>לחץ כאן</a>
🌟 לקניית בוט כזה : <a href=https://t.me/il_334>לחץ כאן</a></b>"""

    SOURCES_TXT = """לקנייה בוט כזה דברו איתי @Mods1234

- בוט איכותי מאוד <a href=https://t.me/il_334>לחץ כאן</a>

- & לקנייה לחץ למטה 👇 כאן"""

    SOURCE_TXT = """@Mods1234</b>

- בוט איכותי מאוד <a href=https://t.me/il_334>לחץ כאן</a></b>

- דברו איתי 👇 כאן"""

    FONT_TXT = """I Cᴀɴ Gᴇɴᴇʀᴀᴛᴇ Aᴛᴛʀᴀᴄᴛɪᴠᴇ Fᴏɴᴛs Fᴏʀ Yᴏᴜʀ Tᴇxᴛ Sᴇɴᴅ Lɪᴋᴇ Tʜɪs 👇

ᴇɢ :- /font hi da"""

    CARBON_TXT = """/carbon ﹛ ʏᴏᴜʀ ᴛᴇxᴛ ﹜

ᴇɢ :- /carbon hi"""

    SHARE_TXT = """/share ﹛ ʏᴏᴜʀ ᴛᴇxᴛ ﹜

ᴇɢ :- /share hi da"""

    VIDEO_TXT ="""Dᴏᴡɴʟᴏᴀᴅ Aɴʏ Yᴏᴜᴛᴜʙᴇ Vɪᴅᴇᴏ Fʀᴏᴍ Tʜᴇ Vɪᴅᴇᴏ Lɪɴᴋ

• Hᴏᴡ Tᴏ Usᴇ
• Tʏᴘᴇ /video 𝘈𝘯𝘥 (YᴏᴜTᴜʙᴇ Vɪᴅᴇᴏ Lɪɴᴋ)
• Exᴀᴍᴘʟᴇ:
• /video https://youtu.be/kB9TkCscX0"""

    TELE_TXT = """▫️Hᴇʟᴘ: ▪️ Tᴇʟᴇɢʀᴀᴘʜ ▪️
     Tᴇʟᴇɢʀᴀᴘʜ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ
    Usᴀɢᴇ
    🤧 /telegraph - Sᴇɴᴅ Mᴇ Pʜᴏᴛᴏ Oʀ Vɪᴅᴇᴏ Uɴᴅᴇʀ (5ᴍʙ)"""

    MANUELFILTER_TXT = """<b>Hᴏᴡ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Mᴏᴠɪᴇs / Sᴇʀɪᴇs Usɪɴɢ Tʜɪs Bᴏᴛ</b> 😌 🔋

<b>Fɪʀsᴛ Jᴏɪɴ Tʜɪs Gʀᴏᴜᴩ » https://t.me/il_334</b>

<b>Sᴇɴᴅ Yᴏᴜ Wᴀɴᴛ Mᴏᴠɪᴇs Oʀ Sᴇʀɪᴇs Nᴀᴍᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴩᴇʟʟɪɴɢ</b>

<b>Aɴᴅ Bᴏᴛ Wɪʟʟ Sᴇɴᴅ Yᴏᴜ Asᴋᴇᴅ Fɪʟᴇ</b>

<b>Hᴏᴡ Tᴏ Oᴩᴇɴ Bᴏᴛ Sᴇɴᴅᴇᴅ Fɪʟᴇ Lɪɴᴋ. » <a href=https://t.me/il_334/13>ᴛᴜᴛᴏʀɪᴀʟ</a>.﹤/b>"""

    CONTACT_TXT = """<b>
<b>»» ° Oɴʟʏ Cᴏɴᴛᴀᴄᴛ Fᴏʀ Pᴀɪᴅ Wᴏʀᴋs / Pʀᴏʙʟᴇᴍ / Dᴏᴜʙᴛ / Cᴏʟʟᴀʙ / Hᴇʟᴩ °</b>

<b>»» Iғ U Cᴏɴᴛᴀᴄᴛ Mᴇ Sᴇᴇ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴs 😙</b>
"""

    STATUS_TXT = """<b><u>Cᴜʀʀᴇɴᴛ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs</b></u>
    
<b>📑 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👩🏻‍💻 ᴜsᴇʀs: <code>{}</code>
👥 ɢʀᴏᴜᴘs: <code>{}</code>
🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code>
🗄️ ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code></b>
"""
    LOG_TEXT_G = """<b> #NewGroup
👥 ɢʀᴏᴜᴘ 👥 = {}(<code>{}</code>)
😇 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs 😇 = <code>{}</code>
💌 ᴀᴅᴅᴇᴅ ʙʏ 💌 - {} </b>
"""
    LOG_TEXT_P = """<b> #NewUser
ɪᴅ ♥️- <code>{}</code>
ɴᴀᴍᴇ 💥- {} </b>
"""
