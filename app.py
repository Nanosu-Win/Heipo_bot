import telebot
from flask import Flask, request
import os
import requests
from bs4 import BeautifulSoup

#You can try out the bot on telegram @heipo_bot

bot_token = 'bot_token'
bot = telebot.TeleBot(token=bot_token)
server = Flask(__name__)

def find_at(msg):
    for text in msg:
        if '@' in text:
            return text

def find_at(msg):
    for text in msg:
        if '#' in text:
            return text


@bot.message_handler(commands=['start'])
def greeting(message):
    bot.reply_to(message, "Hello " + message.from_user.first_name +
                 "\nThis is a non-profit miniproject that anyone can use.\n"+
                 "Use /help for more information =)")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "@(name without bracket) for instagram\n"
                          "#(name without bracket) for twitter\n"
                          "/news for news from Website")

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_instagram(message):
    texts = message.text.split() #to split words into lists
    at_text = find_at(texts)

    bot.reply_to(message,'https://instagram.com/{}'.format(at_text[1:]))

@bot.message_handler(func=lambda msg: msg.text is not None and '#' in msg.text)
def at_twitter(message):
    texts = message.text.split() #to split words into lists
    at_text = find_at(texts)

    bot.reply_to(message,'https://twitter.com/hashtag/{}'.format(at_text[1:]))


@bot.message_handler(commands='news') #getting information from various websites
def at_news(message):
    url_get = requests.get("website")
    url_text = url_get.text

    soup_text = BeautifulSoup(url_text, "html.parser")
    single_story = soup_text.findAll("h3", {"class": "teaser__heading"})

    def search()

    search()

@server.route('/' + bot_token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='herokuwebsite' + bot_token)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


