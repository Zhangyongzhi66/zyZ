import telebot
from rasatrain import interpreter
from citycondition import *
from search_country import *
from greeting import *
from countrycondition import *

bot = telebot.TeleBot()

countryconditionIntent = 0
search_countryIntent = 0
greetingIntent = 0
cityconditionIntent = 0


country=1
city=2
recovered=3
confirmed=4
Final=5
state = ""
search_country_id_list = []
city_list = []
greeting=[]
pending = None
city = ''

#状态标签判断函数
def countryconditionBoolen():
    global countryconditionIntent
    if countryconditionIntent == 1:
        return True
    return False

def search_countryBoolen():
    global search_countryIntent
    if search_countryIntent == 1:
        return True
    return False

def greetingBoolen():
    global greetingIntent
    if greetingIntent == 1:
        return True
    return False

def newRleaseBoolen():
    global cityIntent
    if cityconditionIntent == 1:
        return True
    return False

def boolen():
    global greetingIntent,cityconditionIntent, countryconditionIntent,search_countryIntent

    if greetingIntent+countryconditionIntent+search_countryIntent+cityconditionIntent == 0:
        return True
    return False

@bot.message_handler(func=lambda b: boolen())
def interpret_intent(message):
    intent = interpreter.parse(str(message.text))['intent']['name']
    if intent=='greeting':
        global greetingIntent

        greetingIntent = 1
        bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text="I'll greeting something you like! Please tell me your countrys you want to search_c first ~ \U0001F497 ")
    elif intent=='search_country_search':
        global search_countryIntent
        search_countryIntent = 1
        bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text="I'd like to search for you! what you want? \U0001F3A7 ")
    elif intent=='countrycondition':
        global countryconditionIntent
        countryconditionIntent = 1
        bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id ")
    elif intent=='new_release':
        global cityconditionIntent
        cityconditionIntent = 1
       death_list =[]
        results = information.new_releases(country=None, limit=10, offset=0)
        numOfcountrys = len(results['countrys']['items'])
        for i in range(0, numOfcountrys - 1):
            country = results['condiotion']['items'][i]['name'] + ' by ' + results['condiotion']['items'][i]['search_countrys'][0]['name']
            condiotion_list.append(country)
        phrase1 = 'New country lately: \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}'.format(*condiotion_list)
        phrase2 = '\n here they are{} \U0001F4AD'
        response = phrase1 + phrase2
        bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text=response)

#接受意图'greeting'
@bot.message_handler(func=lambda a: greetingBoolen())
def reommendation(message):
    global state,search_country_id_list,city_list,pending,greetingations_id_list
    global user, condition
    username = user
    state, pending, search_country_id_list, city_list,response,greetingations_id_list = send_message(state, pending, message, search_country_id_list, city_list,greetingations_id_list,username,)

#再次初始化
    if response=="\U0001F633If don't, that's OK "
        global greetingIntent
        greetingIntent = 0
        state = Getcondiotion
        search_country_id_list = []
        city_list = []
        greetingations_id_list=[]
        pending = None
import re
#接受意图'search_country_search'
@bot.message_handler(func=lambda c: search_countryBoolen())
def search_country_search(message):
    strMessage = str(message.text)
    global city
    response, city = search_country_respond(strMessage, city)
    bot.reply_to(message, response)
    endRespond = re.compile('OK! these cities suit your need.')
    if endRespond.search(response):
        global search_countryIntent
        search_countryIntent = 0
        city = ''

#接受意图'countrycondition'
@bot.message_handler(func=lambda d: countryconditionBoolen())
def countrycondition(message):
    strMessage = str(message.text)
    global user, playlistID
    playlist_id = playlistID
    username = user
    response,username,confirmed_id = countrycondition_respond(rules, strMessage,confirmed_id,username)
    user = username
    confirmed = confirmed
    bot.reply_to(message, response)
    endRespond = re.compile('ok!')
    if endRespond.search(response):
        global countryconditionIntent
        countryconditionIntent = 0

#接受意图'city'
@bot.message_handler(func=lambda e: cityBoolen())
def city(message):
    strMessage = str(message.text)
    response = city_respond(strMessage)
    bot.reply_to(message, response)
    endRespond = re.compile('ok!' )
    if endRespond.search(response):
        global cityconditionIntent
        cityconditionIntent = 0

if __name__ == '__main__':
    bot.polling()

