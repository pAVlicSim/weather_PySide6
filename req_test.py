from pprint import pprint
from typing import Any

import requests
import socket

location_list = ['Москва']
weather_key = 'a4af42f30a2642699b4193057211810'
_ip = ''


def my_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        loc_ip = st.getsockname()[0]
    except Exception:
        loc_ip = '127.0.0.1'
    finally:
        st.close()
    return loc_ip


print(my_ip())
print(type(my_ip()))


# def my_location():
#     reg = requests.get('http://api.weatherapi.com/v1/ip.json?key={0}&q={1}'.format(weather_key, '192.168.1.82'))
#     print(reg.status_code)
#     if reg.status_code == 200:
#         pprint(reg.json())
#
#
# my_location()

def load_forecast():
    reg = requests.get('http://api.weatherapi.com/v1/forecast.json?key={0}&q={1}&days=8&lang=RU'.
                       format(weather_key, 'Москва'))
    if reg.status_code == 200:
        # pprint(reg.json())
        weather: Any = reg.json()
        print('len forecast:', len(weather['forecast']['forecastday']))
    return weather


pprint(load_forecast())
