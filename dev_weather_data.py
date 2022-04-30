from pprint import pprint

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QPointF, QDateTime
from weather_main import weather_dict
from datetime import datetime as dt

weather_now = weather_dict['current']
weather_hourly = weather_dict['hourly']
weather_week = weather_dict['daily']
pprint(weather_now)


def create_label_now_text() -> dict:
    label_now_text = {
        'title': f"{dt.fromtimestamp(weather_now['dt']): %A  %d.%m.%y  %H:%M:%S}   {weather_dict['name_city']}",
        'weather': f"Сейчас: \n"
                   f"{weather_now['weather'][0]['description']}\n"
                   f"Температура воздуха: {weather_now['temp']: .1f}℃.  "
                   f"По ощущениям: {weather_now['feels_like']: .1f}℃\n"
                   f"Облачность: {weather_now['clouds']}%  Точка росы: {weather_now['dew_point']: .1f}\n"
                   f"Влажность: {weather_now['humidity']}%\n"
                   f"Ветер.  Направление: {wind_deg_tosStr(weather_now['wind_deg'])}   "
                   f"Скорость: {weather_now['wind_speed']: .1f} м/с"
                   f"Порывы до: {weather_now['wind_gust']: .1f}м/с\n"
                   f"Атмосферное давление: {weather_now['pressure']} гПа  "
                   f"Индекс ультрафиолета: {weather_now['uvi']}\n"
                   f"Видимость:  {weather_now['visibility']}"
                   f"Восход солнца: {dt.fromtimestamp(weather_now['sunrise']): %H:%M} "
                   f"Закат: {dt.fromtimestamp(weather_now['sunset']): %H:%M}"}
    return label_now_text


class TableHourlyData:
    def __init__(self):
        self.data_table_dict = {}
        self.vertical_headers = []
        self.horizontal_headers = ('Темп.', 'по ощущениям', 'Давл.', 'Влаж.', 'Ветер.', 'Точ. росы', 'Ультраф.',
                                   'Облач.')
        self.create_headers()
        self.create_items()

    def create_headers(self):
        for i in range(len(weather_hourly)):
            self.vertical_headers.append(f"{dt.fromtimestamp(weather_hourly[i]['dt']):%a   %H:%M}")

    def create_items(self):
        temp_list = []
        feels_list = []
        pressure_list = []
        humidity_lst = []
        wind_list = []
        dew_point_list = []
        uvi_list = []
        clouds_list = []

        for i in range(len(weather_hourly)):
            temp_list.append(f"{weather_hourly[i]['temp']: .1f}℃")
            feels_list.append(f"{weather_hourly[i]['feels_like']: .1f}℃")
            pressure_list.append(f"{weather_hourly[i]['pressure']}гПа")
            humidity_lst.append(f"{weather_hourly[i]['humidity']}%")
            wind_list.append(f"{weather_hourly[i]['wind_speed']:.1f}м/с - {weather_hourly[i]['wind_gust']:.1f}м/с\n"
                             f"Направление: {wind_deg_tosStr(weather_hourly[i]['wind_deg'])}")
            dew_point_list.append(f"{weather_hourly[i]['dew_point']}℃")
            uvi_list.append(f"{weather_hourly[i]['uvi']}")
            clouds_list.append(f"{weather_hourly[i]['clouds']}%")

        self.data_table_dict['temp'] = temp_list
        self.data_table_dict['pressure'] = pressure_list
        self.data_table_dict['humidity'] = humidity_lst
        self.data_table_dict['wind'] = wind_list
        self.data_table_dict['dew_point'] = dew_point_list
        self.data_table_dict['uvi'] = uvi_list
        self.data_table_dict['clouds'] = clouds_list
        self.data_table_dict['feels'] = feels_list


def create_data() -> dict:
    chart_data = {}
    temp_data = []
    feels_data = []
    humidity_data = []
    press_data = []
    uvi_data = []
    time_data = []
    dt_data = []
    for i in weather_hourly:
        temp_data.append(round((i['temp'])))
        feels_data.append(round(i['feels_like'], 1))
        humidity_data.append(i['humidity'])
        press_data.append(i['pressure'])
        time_data.append(QDateTime.fromSecsSinceEpoch(i['dt']))
        dt_data.append(i['dt'])
        uvi_data.append(i['uvi'])

    chart_data['temp'] = temp_data
    chart_data['press'] = press_data
    chart_data['humidity'] = humidity_data
    chart_data['feels'] = feels_data
    chart_data['time'] = time_data
    chart_data['dt'] = dt_data
    chart_data['uvi'] = uvi_data
    return chart_data


class HourlyChartsData:
    def __init__(self):
        self.temp_series = chart_points(create_data()['dt'], create_data()['temp'])
        self.feels_series = chart_points(create_data()['dt'], create_data()['feels'])
        self.pressSeries = chart_points(create_data()['dt'], create_data()['press'])
        self.humiditySeries = chart_points(create_data()['dt'], create_data()['humidity'])
        self.uviSeries = chart_points(create_data()['dt'], create_data()['uvi'])
        self.x_axisMin = x_axis_range(create_data()['time'])[0]
        self.x_axsMax = x_axis_range(create_data()['time'])[1]
        self.y_tempAxisMin = y_axis_range([create_data()['temp'], create_data()['feels']])[0]
        self.y_tempAxisMax = y_axis_range([create_data()['temp'], create_data()['feels']])[1]
        self.y_pressAxisMin = y_axis_range([create_data()['press']])[0]
        self.y_pressAxisMax = y_axis_range([create_data()['press']])[1]
        self.y_humidityAxisMin = y_axis_range([create_data()['humidity']])[0]
        self.y_humidityAxisMax = y_axis_range([create_data()['humidity']])[1]
        self.y_uviAxisMin = y_axis_range([create_data()['uvi']])[0]
        self.y_uviAxisMax = y_axis_range([create_data()['uvi']])[1]


def x_axis_range(qdates: list):
    return [min(qdates), max(qdates)]


def y_axis_range(y_axes: list):
    n = int
    full_axes = sum(y_axes, [])
    for n in range(1, 5):
        if ((int(max(set(full_axes))) + 2) - (int(min(set(full_axes))) - n)) % 2 == 0:
            print((int(max(set(full_axes))) + 2) - (int(min(set(full_axes))) - n) % 2)
            break
        else:
            n += 1
    return [int(min(set(full_axes))) - n, int(max(set(full_axes))) + 2]


def chart_points(dates: list, chart_list: list):
    return list(map(QPointF, dates, chart_list))


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


def wind_deg_tosStr(deg: int):
    deg_lists = ([i for i in range(22, 337)])
    if deg in deg_lists[22: 66]:
        degStr = 'северо-восточный'
    elif deg in deg_lists[67: 111]:
        degStr = 'восточный'
    elif deg in deg_lists[112: 156]:
        degStr = 'юго-восточный'
    elif deg in deg_lists[157: 201]:
        degStr = 'южный'
    elif deg in deg_lists[202: 246]:
        degStr = 'юго-западный'
    elif deg in deg_lists[246: 291]:
        degStr = 'западный'
    elif deg in deg_lists[291: 336]:
        degStr = 'северо-западный'
    else:
        degStr = 'северный'
    return degStr


class WeekData:
    def __init__(self):
        self.week_data = {}

    def create_week_data(self):
        pass
