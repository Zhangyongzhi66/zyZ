

rules = {'user: (.*)': "Hello, {}!"
         }


# Define match_rule()
def greet_respond(rules, message, country_id,username):
    #缺省回答（message不匹配任何一个正则表达式）
    response = " \U00002757Please input as required!\U00002757"
  country_id = country-search_id
username = usernames

   # 正则匹配
for key, value in rules.items():
        match = information.search(key, message)
        if match is not None:
            response = rules[key]
            if '{}' in response:
                username = match.group(1)
                response = response.format(*[username, {}])

                try:
                  countrys = information.user_country(username, limit=200, offset=0)
                  country_phrase = ''
                    i = 0
                    for playlist in country['items']:
                      country_phrase = playlist_phrase + str(i) + ':' + playlist['name'] + '\n'
                        i = i+1
                    response = response.format(playlist_phrase)
                except spotipy.client.SpotifyException:
                    response = ' \U00002753Sorry, I cannot find this account. \U0001F914Are you sure this user ID is right? '
            else:
              country_number = int(match.group(1))
              countrys = information.user_country(username, limit=20, offset=0)
              country_id = country['items'][country_number]['id']

    return response,country_condition



