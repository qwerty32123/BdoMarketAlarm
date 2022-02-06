import telegram

import discord
#token that can be generated talking with @BotFather on telegram
my_token = '2142530999:AAGStB6oApZiLwE9JZf2VblSLeXwmZrejAk'

def send(msg, token=my_token):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=-752690690, text=msg)


