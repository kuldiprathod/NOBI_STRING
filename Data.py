from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}
Bot For help You to Create Session.
[➼](https://telegra.ph/file/8c0c0dc2721c54857acf0.jpg) So What U Waiting For Generat STRING Session
───────────────────────

If you don't trust this bot, 
1) stop reading this message
2) delete this chat
───────────────────────
Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: [NOBITA!](https://t.me/REPOKIDUNIYA)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("💟 Start Generating Session 💟", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🎉 Start Generating Session 🎉", callback_data="generate")],
        [InlineKeyboardButton("💕 JOIN FOR REPOS 😙✌️", url="https://t.me/REPOKIDUNIYA")],
        [
            InlineKeyboardButton("How to Use 🤭❔", callback_data="help"),
            InlineKeyboardButton("😏 About 😏", callback_data="about")
        ],
        [InlineKeyboardButton("🥱 More Amazing bots 🥱", url="https://t.me/REPOKIDUNIYA")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to Manage group and generate pyrogram and telethon string session by Nobita

Source Code : [Click Here](https://t.me/REPOKIDUNIYA)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @kigo_omfo
    """
