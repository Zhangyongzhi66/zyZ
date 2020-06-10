from rasatrain import interpreter
from data import *
import pycountry


country_responses = [
    "I'm sorry :( I couldn't find anything like that",
    '{} Is getting better',
    '{} or {} is getting worse',
]


#判断被否定的实体，用result储存并返回
def negated_ents(phrase, ent_vals):
    ents = [e for e in ent_vals if e in phrase]
    ends = sorted([phrase.index(e) + len(e) for e in ents])
    start = 0
    chunks = []
    for end in ends:
        chunks.append(phrase[start:end])
        start = end
    result = {}
    for chunk in chunks:
        for ent in ents:
            if ent in chunk:
                if str(ent) == 'severe' or str(ent) == 'not_severe':
                    if "not" in chunk or "n't" in chunk:
                        result[ent] = False
                    else:
                        result[ent] = True
    return result






        #进入甄别否定实体并筛选的阶段
        elif str(ent["entity"]) == 'country':
        response_template = " \U0001F44COK! \n {} "
        if ent["value"] in popularity_negated and not popularity_negated[ent["value"]]:
                neg_params = [str(ent["value"])]
            else:
                params = [str(ent["value"])]
        countries,num1condition = modify_countries(params, neg_params, country)


    n = min(num1country, 4)
    id = country.keys()
    response = response_template.format(country_responses[n].format(*names))
    return response.condition
