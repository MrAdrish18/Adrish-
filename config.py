from multiprocessing.connection import Connection
from os import environ
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


class Config(object):
        #Your telegram BOT username(without @) : get it from @BotFather
        BOT_USERNAME = environ.get("BOT_USERNAME")
        #Your telegram BOT API token : get it from @BotFather
        BOT_TOKEN = environ.get("BOT_TOKEN")
        #API_ID of your Telegram Account my.telegram.org/apps
        API_ID = int(environ.get("API_ID"))
        #API_HASH of your Telegram Account my.telegram.org/apps
        API_HASH = environ.get("API_HASH")
        #API_ID of your Telegram Account my.telegram.org/apps
        API_ID1 = int(environ.get("API_ID1"))
        #API_HASH of your Telegram Account my.telegram.org/apps
        API_HASH1 = environ.get("API_HASH1")
        #Your telegram user id
        OWNER_ID = environ.get("OWNER_ID")
        #For logs channel to note down important bot level events, recommend to make this public. ex: '-123456'
        LOG_GROUP_ID = environ.get("LOG_GROUP_ID")
        #Get From Here.https://www.mongodb.com/ (Same as MONGO_URL but give differant value for this) 
        BASE_DB = environ.get("BASE_DB")
        #Get From Here.https://www.mongodb.com/
        MONGO_URL = environ.get("MONGO_URL")
        #Don't change this value:https://arq.hamker.in
        ARQ_API_URL = environ.get("ARQ_API_URL")
        #Get this from @ARQRobot.
        ARQ_API_KEY = environ.get("ARQ_API_KEY")
        #now you can set custom command handler for rose like : / ! ,
        COMMAND_PREFIXES = environ.get("COMMAND_PREFIXES")
        #The Telegram channel id you want focus user.(User can't start your bot without join it)
        F_SUB_CHANNEL = environ.get("F_SUB_CHANNEL")

class var(object):
        #Rose group start message here 
        group_start_text = "Hey :) PM me if you have any questions on how to use me!"
        #Rose help menu text message here 
        help_text = """
**Welcome to help menu**

I'm a group management bot with some useful features.
You can choose an option below, by clicking a button.
If you have any bugs or questions on how to use me, 
have a look at my Support group [Support](https://t.me/Adrish_Support), or head to @im_Adrish.

**All commands can be used with the following: / **"""
        #Adrish start menu conections(split commands on start)
        Connection_text_start = "** Run /connections to view or disconnect from groups!**"
        #Adrish private start message here
        pm_start_text = """
Hey there {},my name is {}
An  advanced telegram Group management Bot For helpYou Protect Your Groups & Suit For All Your Needs.feel free to add me to your groups! """
        #Languages change text menu here 
        lang_text = "Choose Your languages"

        #Languages change button menu here this will show current languages rose can message
        lang_keyboard = InlineKeyboardMarkup(
                [
                        [
                                InlineKeyboardButton(text="🇱🇷 English", callback_data="languages_en")
                        ],
                        [
                                InlineKeyboardButton(text="🇱🇰 සිංහල", callback_data="languages_si"), 
                                InlineKeyboardButton(text="🇮🇳 हिन्दी", callback_data="languages_hi")
                        ], 
                        [
                                InlineKeyboardButton(text="🇮🇹 Italiano", callback_data="languages_it"), 
                                InlineKeyboardButton(text="🇮🇳 తెలుగు", callback_data="languages_ta")
                        ], 
                        [
                                InlineKeyboardButton(text="🇮🇩 Indonesia", callback_data="languages_id"), 
                                InlineKeyboardButton(text="🇦🇪 عربي", callback_data="languages_ar")
                        ], 
                        [
                                InlineKeyboardButton(text="🇮🇳 മലയാളം", callback_data="languages_ml"), 
                                InlineKeyboardButton(text="🇲🇼 Chichewa", callback_data="languages_ny")
                        ], 
                        [
                                InlineKeyboardButton(text="🇩🇪 German", callback_data="languages_ge"), 
                                InlineKeyboardButton(text="🇷🇺 Russian", callback_data="languages_ru")
                        ], 
                        [
                                InlineKeyboardButton("« Back", callback_data='startcq')
                        ]
                ]
)
        #Rose informations button menu here
        about_buttons = InlineKeyboardMarkup(
                [
                        [
                                InlineKeyboardButton(text="👥Support Group", url="https://t.me/Adrish_support"),
                                InlineKeyboardButton(text="👤News Channel", url="https://t.me/AdrishFederation")
                        ], 
                        [ 
                                InlineKeyboardButton(text="⚒ Source Code", url="https://te.legra.ph/file/b6da0a42b0ef916e4ab45.mp4"),
                                InlineKeyboardButton(text="📓 Documentation", url="https://t.me/im_Adrish")
                        ], 
                        [
                                InlineKeyboardButton(text="🖥 How To Deploy Me", url="https://t.me/AdrishFed")
                        ],
                        [
                                InlineKeyboardButton("« Back", callback_data='startcq')
                        ]
                ]
)
        #Rose private start button menu here
        home_keyboard_pm = InlineKeyboardMarkup(
                [
                        [
                                InlineKeyboardButton(text="Add Me To Your Chat 🎉",url=f"http://t.me/{Config.BOT_USERNAME}?startgroup=new")
                        ],
                        [
                                InlineKeyboardButton(text="About ✨",callback_data="_about"),
                                InlineKeyboardButton(text="languages 🌏",callback_data="_langs")
                        ],
                        [
                                InlineKeyboardButton(text="Help Menu ⚒",callback_data="bot_commands")
                        ],
                        [
                                InlineKeyboardButton(text="Website 💭",url=f"https://adrish.ml"),
                                InlineKeyboardButton(text="News Channel 📢",url=f"https://t.me/AdrishFederation")
                        ]
                ]
)
        
