import copy
from pprint import pprint
import requests

weather_key = '7ce6c84dd325b5a80620aa9add3c0b91'


def load_geolocation(name_city: str):
    location_list = []
    reg = requests.get('http://api.openweathermap.org/geo/1.0/direct?q={0}'
                       '&appid={1}'.format(name_city, weather_key))
    if reg.status_code == 200:
        # pprint(reg.json())
        location_list.append(reg.json()[0]['local_names']['ru'])
        location_list.append(reg.json()[0]['lat'])
        location_list.append(reg.json()[0]['lon'])
        # pprint(location_list)
        return location_list


def load_weather(location_lict: list):
    reg = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}&exclude=minutely&units=metric'
                       '&lang=ru&appid=7ce6c84dd325b5a80620aa9add3c0b91'.format(location_lict[1], location_lict[2]))
    if reg.status_code == 200:
        weather = reg.json()
        weather['name_city'] = location_lict[0]
        return weather
