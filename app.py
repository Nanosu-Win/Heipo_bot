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
                          "/news for news from CNA Website")

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


'''@bot.message_handler(commands='news')
def at_news(message):
    url_get = requests.get("https://www.channelnewsasia.com/news/singapore")
    url_text = url_get.text

    soup_text = BeautifulSoup(url_text, "html.parser")
    single_story = soup_text.findAll("h3", {"class": "teaser__heading"})

    def search():

        bool = True
        while bool == True:
            title0 = single_story[0].a.text
            link0 = single_story[0].a.get("href")
            title1 = single_story[1].a.text
            link1 = single_story[1].a.get("href")
            title2 = single_story[2].a.text
            link2 = single_story[2].a.get("href")
            title3 = single_story[3].a.text
            link3 = single_story[3].a.get("href")
            title4 = single_story[4].a.text
            link4 = single_story[4].a.get("href")
            title5 = single_story[5].a.text
            link5 = single_story[5].a.get("href")
            title6 = single_story[6].a.text
            link6 = single_story[6].a.get("href")
            title7 = single_story[7].a.text
            link7 = single_story[7].a.get("href")
            title8 = single_story[8].a.text
            link8 = single_story[8].a.get("href")
            title9 = single_story[9].a.text
            link9 = single_story[9].a.get("href")
            title10 = single_story[10].a.text
            link10 = single_story[10].a.get("href")
            title11 = single_story[11].a.text
            link11 = single_story[11].a.get("href")

            bool = False

    # ",".join(list_news)
        bot.reply_to(message,
        title0 + "\n" +
        "www.channelnewsasia.com"+link0 + "\n\n"+
        title1 + "\n"+
        "www.channelnewsasia.com"+link1 + "\n\n"+
        title2 + "\n"+
        "www.channelnewsasia.com"+link2 + "\n\n"+
        title3 + "\n"+
        "www.channelnewsasia.com"+link3 + "\n\n"+
        title4 + "\n"+
        "www.channelnewsasia.com"+link4 + "\n\n"+
        title5 + "\n"+
        "www.channelnewsasia.com"+link5 + "\n\n"+
        title6 + "\n"+
        "www.channelnewsasia.com"+link6 + "\n\n"+
        title7 + "\n"+
        "www.channelnewsasia.com"+link7 + "\n\n"+
        title8 + "\n"+
        "www.channelnewsasia.com"+link8 + "\n\n"+
        title9 + "\n"+
        "www.channelnewsasia.com"+link9 + "\n\n"+
        title10 + "\n"+
        "www.channelnewsasia.com"+link10 + "\n\n"+
        title11 + "\n"+
        "www.channelnewsasia.com"+link11 + "\n\n")

    search()'''

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


