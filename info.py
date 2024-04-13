import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '7553555'))
API_HASH = environ.get('API_HASH', 'a80f4ae31a5c9ff669da4d7f19d6f15e')
BOT_TOKEN = environ.get('BOT_TOKEN', "5556803093:AAGrXEJxjANL-X7F46lPhqW-QKUOdf3znBw")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 99999))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/d3553fb949c9cfab3fb50.jpg https://graph.org/file/0ffb1cc06d35e917a72ec.jpg https://graph.org/file/f3fb3fba71030631a4e81.jpg https://graph.org/file/88762f9036355fa959ebe.jpg https://graph.org/file/3aed764415d92f44b4bea.jpg https://graph.org/file/2e5b573e18031c3598b9f.jpg https://graph.org/file/2e5b573e18031c3598b9f.jpg https://graph.org/file/abbab43f9d7473e05758f.jpg https://graph.org/file/c13f98a2af41bdaf30b7b.jpg https://graph.org/file/0b5ff7755e95673536e78.jpg https://graph.org/file/65e79f235e9f6e3994803.jpg https://graph.org/file/c8792929b6c9c51f8d53d.jpg https://graph.org/file/fc9f80637d3f8aaf79e67.jpg https://graph.org/file/2683af8ab72dc938998c5.jpg https://graph.org/file/a303009efbe2d55349a65.jpg https://graph.org/file/3cce014e6279ea52c3708.jpg https://graph.org/file/c21949b0ae9807708335f.jpg https://graph.org/file/753c6b325a4f088374730.jpg https://graph.org/file/7b7e60b561a16f6857275.jpg https://graph.org/file/470dac3c0e65c5eed7a21.jpg https://graph.org/file/c09a16c11c1884c796dbe.jpg https://graph.org/file/50ea0516d60999f35242b.jpg https://graph.org/file/7af01579618500b57dc65.jpg https://graph.org/file/7af01579618500b57dc65.jpg https://graph.org/file/4d6913668505348784ead.jpg https://graph.org/file/82ec44ab0f292cf29591d.jpg https://graph.org/file/427fd328a6b94461bbb3f.jpg https://graph.org/file/24994b6166b85a7e1c96d.jpg https://graph.org/file/a46696b76e2ee9440dc89.jpg https://graph.org/file/3a3956ba102dd741dc5fb.jpg https://graph.org/file/1ecc1d194e9b91fe752b7.jpg https://graph.org/file/2e35179341f18dd6423b7.jpg https://graph.org/file/548ea31088580deb76bb4.jpg https://graph.org/file/472d0c8c6d048830a8473.jpg https://graph.org/file/fd5de18e1e0978b9850d3.jpg https://graph.org/file/c9ac11819db3d97025252.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/b43d3079652654fd8692c.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/b43d3079652654fd8692c.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/b43d3079652654fd8692c.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5383602320').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
reqst_channel = environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Krishn100:Krishn100@cluster0.billeg5.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Krishna 100")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')


# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'paisakamalo.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '16badb4cdfbd26689b88c28d4385b24b5ec85d81')
SECOND_SHORTLINK_URL = environ.get('SECOND_SHORTLINK_URL', 'paisakamalo.in')
SECOND_SHORTLINK_API = environ.get('SECOND_SHORTLINK_API', '16badb4cdfbd26689b88c28d4385b24b5ec85d81')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+QENrEno72xQwOTg1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Radhakriishn')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/MythoSerial/157')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Maintained By: @Sandip10x')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION") f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]

LANGUAGES = ["malayalam", "tamil" ,"english", "hindi", "telugu", "kannada"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
