import requests
url = "https://covid-19-data.p.rapidapi.com/country/code"

querystring = {"format":"json","code":"Beijing"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "0ecde3cef2msh752bcfdf9170163p15b605jsn1749f304a066"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

information=response



#测试
print(response.text)
