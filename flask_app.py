##################################################################
#                                                                #
#  copyright Eytan Goldshmidt & Yoshef Kahalani (2020)           #
#                 part of project NewsBot                        #
#                                                                #
##################################################################

from typing import List, Tuple

import telepot
import urllib3
from flask import Flask, request
from telepot.namedtuple import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from BotConfig import *
from ToolsFlaskBot import *

MAX_MESSAGE_SIZE = 4095

secret = "7bd8040d-baff-41c2-b16f-cdffb6e168f0"

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default' : urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (
    urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

bot = telepot.Bot(TOKEN)
bot.setWebhook("https://{}.pythonanywhere.com/{}".format(PYTHONANYWHERE_NAME, secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def answer() :
    global user
    global count
    user = None
    message_id = None
    count = count + 1
    update = request.get_json()

    try :
        if "message" not in update :
            print("problem with 'message'")
            print(str(update))
        message = update["message"]
        print("message{}: {}".format(count, message))
        if "text" not in message :
            print("problem with 'text'")
            print(str(message))
        if "chat" not in message :
            print("problem with chat")
            print(str(message))

        chat = message["chat"]
        chat_id = chat["id"]
        user = message["from"]

        message_id = message["message_id"]

        text = message["text"]

        ## todo: send the file
    except :
        print(update)
        text = str(update)

    return "ERROR"
