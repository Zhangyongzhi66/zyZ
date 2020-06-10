from rasatrain import interpreter
from data import *
import pycountry

def county_condition_respond(message):

    #初始化
    country_code = ''
    conidition = []


    #实体识别
    entities = interpreter.parse(message)["entities"]
    for ent in entities:
        if str(ent["entity"]) == 'country':
            print(ent["value"])
            country = ent["value"].capitalize()
            country_code = pycountry.countries.get(name= country).alpha_2
            print(ent["value"])
        if country_code!='':
            print(country_code)
            results = information.contry_condition(country=country_code, limit=100, offset=0)
            numOfAlbums = len(results['condition'])
            for i in range(0,numOfAlbums-1):
              country = results['country']['items']
            information.append(country)

    return  response







