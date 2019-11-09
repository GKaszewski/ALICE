import json, requests
from modules.weather_data import Weather

api_token = '0c8347f39424fe1269bec88abe3bcacc'
api_url_base = 'http://api.openweathermap.org/data/2.5/weather?q='

def get_weather(city, metric=True):
    api_url =''
    if metric == True:
        api_url = '{0}{1}&units=metric&APPID={2}'.format(api_url_base, city, api_token)
    else:
        api_url = '{0}{1}&units=imperial&APPID={2}'.format(api_url_base, city, api_token)
    
    response = requests.get(api_url)
    data = json.loads(response.content.decode('utf-8'))
    weather = Weather(data['weather'][0]['description'], data['main']['temp'], data['main']['temp_max'], data['main']['temp_min'], data['main']['humidity'], data['wind']['speed'], data['sys']['sunrise'], data['sys']['sunset'])
    weather.printData()
    return weather