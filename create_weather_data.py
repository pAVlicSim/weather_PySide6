from pprint import pprint
from typing import List, Tuple, Any

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QPointF, QPoint, QDateTime

from weather_main import weather_dict
from datetime import datetime as dt

weather_now = weather_dict['current']
weather_hourly = weather_dict['hourly']
weather_week = weather_dict['daily']


class LabelNowText:
    def __init__(self):
        self.label_now_text = {}
        self.create_label_now_text()

    def create_label_now_text(self):
        self.label_now_text = {
            'title': f"{dt.fromtimestamp(weather_now['dt']): %A  %d.%m.%y  %H:%M:%S}   {weather_dict['name_city']}"
                     f"     {weather_now['weather'][0]['description']}",
            'weather': f"Температура воздуха: {weather_now['temp']}℃.  По ощущениям: {weather_now['feels_like']}℃\n"
                       f"Облачность: {weather_now['clouds']}%  Точка росы: {weather_now['dew_point']}\n"
                       f"Влажность: {weather_now['humidity']}%\n"
                       f"Ветер.  Направление: {weather_now['wind_deg']}   Скорость: {weather_now['wind_speed']} м/с"
                       f"Порывы до: {weather_now['wind_gust']}м/с\n"
                       f"Атмосферное давление: {weather_now['pressure']} гПа  "
                       f"Индекс ультрафиолета: {weather_now['uvi']}\n"
                       f"Восход солнца: {dt.fromtimestamp(weather_now['sunrise']): %H:%M} "
                       f"Закат: {dt.fromtimestamp(weather_now['sunset']): %H:%M}"}


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
                             f"Направление: {weather_hourly[i]['wind_deg']}")
            dew_point_list.append(f"{weather_hourly[i]['dew_point']}℃")
            uvi_list.append(f"{weather_hourly[i]['uvi']}")
            clouds_list.append(f"{weather_hourly[i]['clouds']}")

        self.data_table_dict['temp'] = temp_list
        self.data_table_dict['pressure'] = pressure_list
        self.data_table_dict['humidity'] = humidity_lst
        self.data_table_dict['wind'] = wind_list
        self.data_table_dict['dew_point'] = dew_point_list
        self.data_table_dict['uvi'] = uvi_list
        self.data_table_dict['clouds'] = clouds_list
        self.data_table_dict['feels'] = feels_list


class GraphData:
    def __init__(self):
        self.x_axis_range = []
        self.temp_graph = []
        self.feels_graph = []
        self.press_graph = []
        self.x_axis_list = []
        self.yTemp_min_max = []
        self.yPress_min_max = []
        self.temp_date()

    def temp_date(self):
        date_list = []
        temp_list = []
        feels_list = []
        press_list = []
        qdata_time_list = []
        for i in range(len(weather_hourly)):
            qdata_time_list.append(QDateTime.fromSecsSinceEpoch(weather_hourly[i]['dt']))
            date_list.append(weather_hourly[i]['dt'])
            temp_list.append(round(weather_hourly[i]['temp']))
            feels_list.append(weather_hourly[i]['feels_like'])
            press_list.append(weather_hourly[i]['pressure'])
            self.x_axis_list.append(weather_hourly[i]['dt'])

        self.x_axis_range.append(min(qdata_time_list))
        self.x_axis_range.append(max(qdata_time_list))
        self.temp_graph = list(map(QPointF, date_list, temp_list))
        self.feels_graph = list(map(QPointF, date_list, feels_list))
        self.press_graph = list(map(QPointF, date_list, press_list))
        self.yTemp_min_max.append(int(min(feels_list)) - 1)
        self.yTemp_min_max.append(int(max(temp_list)) + 1)
        self.yPress_min_max.append(min(press_list) - 2)
        self.yPress_min_max.append(max(press_list) + 2)

        print(self.yTemp_min_max[1] - self.yTemp_min_max[0])
        # pprint(qdata_time_list)
        # pprint(temp_list)
        # pprint(self.temp_graph)


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter
