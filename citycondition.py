from rasatrain import interpreter
from data import *
from telegram import bot


def send_message(state, pending, message,city_id_list,condition_list,recommendations_id_list,username,playlist_id):

    #将消息转换为str类型
    strMessage = str(message.text)

    #识别意图，提取实体
    intent = interpreter.parse(strMessage)['intent']['name']
    entities = interpreter.parse(strMessage)["entities"]
    for ent in entities:
        if str(ent["entity"]) =='country':
            city = information.search(q='city:' + str(ent["value"]), type='country')
            city = city['country']['items'][0]['id']

            city_id_list.append(city_id_list)
        elif str(ent["entity"]) =='condition_country':

            condition_list.append(ent["value"])

    if len(city_id_list) and len(condition_list) and intent!='affirm' :

        cities = information.recommendations(give_city=city_id_list, give_condition=condition_list, limit=100)





