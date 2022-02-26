import asyncio
import locale
import sys
from pprint import pprint
from time import strftime, localtime

import aiohttp as aiohttp
from PySide6.QtCharts import QChartView, QChart, QBarCategoryAxis, QValueAxis, QSplineSeries
from PySide6.QtCore import QPoint
from PySide6.QtGui import QPainter, QColor, QFont, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMessageBox
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim

from graphiks_dialog import Ui_Dialog
from my_pen import MyPen
from weather import Ui_Form


def wind_deg_to_str(deg: int) -> str:
    wind = ''
    if 0 <= deg <= 12 or 348 <= deg <= 359:
        wind = 'С'
    elif 13 <= deg <= 32:
        wind = 'ССВ'
    elif 33 <= deg <= 57:
        wind = 'СВ'
    elif 58 <= deg <= 87:
        wind = 'СВВ'
    elif 88 <= deg <= 102:
        wind = 'В'
    elif 103 <= deg <= 122:
        wind = 'ЮВВ'
    elif 123 <= deg <= 147:
        wind = 'ЮВ'
    elif 146 <= deg <= 167:
        wind = 'ЮЮВ'
    elif 168 <= deg <= 192:
        wind = 'Ю'
    elif 193 <= deg <= 212:
        wind = 'ЮЮЗ'
    elif 213 <= deg <= 237:
        wind = 'ЮЗ'
    elif 238 <= deg <= 257:
        wind = 'ЮЗЗ'
    elif 258 <= deg <= 282:
        wind = 'З'
    elif 283 <= deg <= 302:
        wind = 'СЗЗ'
    elif 303 <= deg <= 327:
        wind = 'СЗ'
    elif 328 <= deg <= 347:
        wind = 'ССЗ'
    return wind


weather_dict = {}
history_list = []


async def load_weather_dict(city_geolocation: list):
    global weather_dict
    if city_geolocation is not None:
        base_url = 'http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={' \
                   '}&appid=7ce6c84dd325b5a80620aa9add3c0b91&units=metric&lang=ru&exclude=minutely,hourly,alerts'
        weather_now = base_url.format(city_geolocation[0][0], city_geolocation[0][1])
        async with aiohttp.ClientSession() as session:  # [3]
            async with session.get(weather_now) as weather_now:  # [4]
                print(weather_now.status)
                if weather_now.status == 200:
                    locale.setlocale(locale.LC_ALL, '')
                    weather_dict = await weather_now.json()  # [5]
                    weather_dict['city_name'] = city_geolocation[1]
                else:
                    print("Сбой в работе программы")
    else:
        pass
    pprint(weather_dict)


def geolocation_from_name(name_city: str) -> list:
    geolocator = Nominatim(user_agent='main')
    try:
        location = geolocator.geocode(name_city)
        location_list = [location.latitude, location.longitude]
        print('location_list', location_list)
        return [location_list, name_city]
    except AttributeError:
        print('attr_error')
        create_dialog_warning('Ошибка ввода', 'Проверьте название города\nкоторый вы ввели!')
    except GeocoderUnavailable:
        create_dialog_warning('Нет соединения  с интернетом', 'Проверьте соединение\nс интернетом')
        pprint('GeocoderUnavailable')


def create_dialog_warning(title: str, message: str):
    return QMessageBox.warning(window, title, message, QMessageBox.Ok)


class GraphDialog(QDialog):
    dict_graph = {}
    max_min = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        if weather_dict == {}:
            pass
        else:
            self.data_for_graph(weather_dict)
            #
            self.temp_day_pen = MyPen('#00C4FF', 3)
            self.temp_day_feels_like_pen = MyPen('#FF00D9', 3)
            self.pressure_pen = MyPen('#FF002F', 3)
            # инициализация графиков температуры
            self._temp_day_series = QSplineSeries()
            self._temp_day_series.setPen(self.temp_day_pen)
            self._temp_day_series.setName("Дневная температура")
            self._feels_like_series = QSplineSeries()
            self._feels_like_series.setPen(self.temp_day_feels_like_pen)
            self._feels_like_series.setName('Температура по ощущениям')
            self.temp_chart = QChart()
            self.temp_chart.setTitle("График температуры на неделю")
            self.temp_chart.setBackgroundBrush(QColor('#E5FFAD'))
            self._axis_temp_x = QBarCategoryAxis()
            self._axis_temp_x.setGridLinePen(MyPen('#000000', 2))
            self._axis_temp_x.setLabelsFont(QFont("resource.qrl/Libertinus", 12, QFont.Bold))
            self._axis_temp_y = QValueAxis()
            self._axis_temp_y.setGridLinePen(MyPen('#000000', 2))
            self._axis_temp_y.setTickAnchor(0.0)
            self._axis_temp_y.setTickCount(6)
            self._axis_temp_y.setLabelsFont(QFont("resource.qrl/Libertinus", 12, QFont.Bold))
            self._temp_view = QChartView(self.temp_chart)
            self.ui.graphsLayout.addWidget(self._temp_view)
            #
            self._pressure_series = QSplineSeries()
            self._pressure_series.setPen(self.pressure_pen)
            self._pressure_series.setName('Атмосферное давление')
            self.pressure_chart = QChart()
            self.pressure_chart.setTitle('График давления на неделю')
            self.pressure_chart.setBackgroundBrush(QColor('#FFE2AD'))
            self._axis_press_x = QBarCategoryAxis()
            self._axis_press_x.setGridLinePen(MyPen('#000000', 2))
            self._axis_press_x.setLabelsFont(QFont("resource.qrl/Libertinus", 12, QFont.Bold))
            self._axis_press_y = QValueAxis()
            self._axis_press_y.setTickAnchor(1000.0)
            self._axis_press_y.setTickCount(6)
            self._axis_press_y.setGridLinePen(MyPen('#000000', 2))
            self._axis_press_y.setLabelsFont(QFont("resource.qrl/Libertinus", 12, QFont.Bold))
            self._press_view = QChartView(self.pressure_chart)
            self.ui.graphsLayout.addWidget(self._press_view)

            self.charts_update()

    def charts_update(self):
        self._temp_day_series.append(self.dict_graph['tuple_day'])
        self._feels_like_series.append(self.dict_graph['tuple_feels_like'])
        self.temp_chart.addSeries(self._temp_day_series)
        self.temp_chart.addSeries(self._feels_like_series)
        self._axis_temp_x.append(self.dict_graph['week_day'])
        self.temp_chart.setAxisX(self._axis_temp_x, self._temp_day_series)
        self.temp_chart.setAxisX(self._axis_temp_x, self._feels_like_series)
        self._axis_temp_y.setRange(self.dict_graph['max_min'][0], self.dict_graph['max_min'][1])
        self.temp_chart.setAxisY(self._axis_temp_y, self._temp_day_series)
        self.temp_chart.setAxisY(self._axis_temp_y, self._feels_like_series)
        self._temp_view.setRenderHint(QPainter.Antialiasing)
        # create pressure chart
        self._pressure_series.append(self.dict_graph['tuple_press'])
        self.pressure_chart.addSeries(self._pressure_series)
        self._axis_press_x.append(self.dict_graph['week_day'])
        self.pressure_chart.setAxisX(self._axis_press_x, self._pressure_series)
        self._axis_press_y.setRange(self.dict_graph['press_max_min'][0], self.dict_graph['press_max_min'][1])
        self.pressure_chart.setAxisY(self._axis_press_y, self._pressure_series)
        self._press_view.setRenderHint(QPainter.Antialiasing)

    def data_for_graph(self, weather: dict):
        list_date = []
        list_tuple_day = []
        list_max_min_day = []
        list_max_min_feels_like = []
        list_tuple_feel_like = []
        list_tuple_press = []
        list_press_max_min = []
        for i in range(len(weather['daily'])):
            list_date.append(strftime('%d.%m %a', localtime(weather['daily'][i]['dt'])))
            list_tuple_day.append(QPoint(i, weather['daily'][i]['temp']['day']))
            list_max_min_day.append(int(weather['daily'][i]['temp']['day']))
            list_max_min_feels_like.append(int(weather['daily'][i]['feels_like']['day']))
            list_tuple_feel_like.append(QPoint(i, weather['daily'][i]['feels_like']['day']))
            list_tuple_press.append((QPoint(i, weather['daily'][i]['pressure'])))
            list_press_max_min.append(weather_dict['daily'][i]['pressure'])
        list_temp_max_min = list_max_min_day + list_max_min_feels_like
        print(list_temp_max_min)
        max_temp = max(list_temp_max_min)
        min_temp = min(list_temp_max_min)
        print(max_temp, min_temp)
        max_pressure = max(list_press_max_min)
        min_pressure = min(list_press_max_min)
        for i in range(1, 6):
            max_temp += 1
            print(max_temp)
            if max_temp % 5 == 0:
                break
        for i in range(1, 6):
            min_temp -= 1
            if min_temp % 5 == 0:
                break
        for i in range(1, 11):
            max_pressure += 1
            if max_pressure % 10 == 0:
                break
        for i in range(1, 11):
            min_pressure -= 1
            if min_pressure % 10 == 0:
                break
        list_temp_max_min.clear()
        list_press_max_min.clear()
        list_temp_max_min.append(min_temp)
        list_temp_max_min.append(max_temp)
        list_press_max_min.append(min_pressure)
        list_press_max_min.append(max_pressure)
        print(list_temp_max_min)
        self.dict_graph['week_day'] = list_date
        self.dict_graph['tuple_day'] = list_tuple_day
        self.dict_graph['max_min'] = list_temp_max_min
        self.dict_graph['tuple_feels_like'] = list_tuple_feel_like
        self.dict_graph['tuple_press'] = list_tuple_press
        self.dict_graph['press_max_min'] = list_press_max_min
        # pprint(self.dict_graph['tuple_feels_like'])
        print(self.dict_graph['tuple_day'])
        # print(list_date)
        # print(self.dict_graph['max_min'])


class MainWidget(QWidget):
    weather_daily = {}
    weather_now = None

    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.push_source_city.clicked.connect(self.update_weather_from_search)
        self.ui.push_week_graph.clicked.connect(self.graphs_show)
        if self.ui.comboBox_history.currentText() == '':
            pass
        else:
            asyncio.run(load_weather_dict(geolocation_from_name(self.ui.comboBox_history.currentText())))
            self.create_weather_now(weather_dict)
            print(weather_dict)
            self.ui.label_now.setText(self.weather_now)
            self.update_weather_week(weather_dict)

    def graphs_show(self):
        graph_dialog = GraphDialog(self)
        graph_dialog.exec()

    def add_history_item(self):
        if self.ui.enter_city_name.text() == '':
            pass
        else:
            self.ui.comboBox_history.addItem(self.ui.enter_city_name.text())

    def create_weather_now(self, weather: dict):
        self.weather_now = 'Город   {city}    Дата:   {dt}\n{description}\nТемпература  {temp}℃ ' \
                           '   По ощущениям  {feels_like}℃\nИндекс ультрафиолета {uvi}     ' \
                           'Точка росы  {dew_point}℃\nВетер:  Скорость   {speed}м/с    ' \
                           'Направление    {deg}\nПорывы до  {gust}м/с\nДавление {pressure} K/pa    ' \
                           'Влажность {humidity}%\nВосход  {sunrise}    Закат {sunset}'
        format_now_dict = {'city': weather['city_name'],
                           'dt': strftime('%d.%m.%Y   %H:%M:%S', localtime(weather['current']['dt'])),
                           'description': weather['current']['weather'][0]['description'],
                           'temp': str(weather['current']['temp']),
                           'feels_like': str(weather['current']['feels_like']),
                           'dew_point': str(weather['current']['dew_point']),
                           'uvi': str(weather['current']['uvi']),
                           'speed': str(weather['current']['wind_speed']),
                           'deg': wind_deg_to_str(weather['current']['wind_deg']),
                           'gust': str(weather['current'].get('wind_gust', 'нет данных  ')),
                           'pressure': str(weather['current']['pressure']),
                           'humidity': str(weather['current']['humidity']),
                           'sunrise': strftime('%H:%M:%S', localtime(weather['current'].get('sunrise', -10800))),
                           'sunset': strftime('%H:%M:%S', localtime(weather['current'].get('sunset', -10800)))}
        self.weather_now = self.weather_now.format_map(format_now_dict)

    def update_weather_from_search(self):
        if self.ui.enter_city_name.text() == '':
            create_dialog_warning('Ошибка ввода', 'Введите название населённого\nпункта в поле ввода')
        else:
            asyncio.run(load_weather_dict(geolocation_from_name(self.ui.enter_city_name.text())))
            if weather_dict != {}:
                self.create_weather_now(weather_dict)
                self.ui.label_now.setText(self.weather_now)
                self.update_weather_week(weather_dict)
            else:
                pass

    def update_weather_from_history(self, city_name):
        load_weather_dict(geolocation_from_name(city_name))
        print(weather_dict)
        self.create_weather_now(weather_dict)
        self.ui.label_now.setText(self.weather_now)

    def update_weather_week(self, weather: dict):
        self.create_weather_daily(weather)
        self.ui.label_city_week.setText("{}   Погода на неделю".format(self.weather_daily['city_name']))
        self.ui.label_week0.setText(self.weather_daily['day0'])
        self.ui.label_week1.setText(self.weather_daily['day1'])
        self.ui.label_week2.setText(self.weather_daily['day2'])
        self.ui.label_week3.setText(self.weather_daily['day3'])
        self.ui.label_week4.setText(self.weather_daily['day4'])
        self.ui.label_week5.setText(self.weather_daily['day5'])
        self.ui.label_week6.setText(self.weather_daily['day6'])
        self.ui.label_week7.setText(self.weather_daily['day7'])

        self.ui.icon_0.setPixmap(QPixmap('resource.qrl/weather_icon/' + self.weather_daily['icon_list'][0] + '.png'))
        self.ui.icon_1.setPixmap(QPixmap('resource.qrl/weather_icon/' + self.weather_daily['icon_list'][1] + '.png'))
        self.ui.icon_2.setPixmap(QPixmap('resource.qrl/weather_icon/' + self.weather_daily['icon_list'][2] + '.png'))
        self.ui.icon_3.setPixmap(QPixmap('resource.qrl/weather_icon/' + self.weather_daily['icon_list'][3] + '.png'))
        self.ui.icon_4.setPixmap(QPixmap('resource.qrl/weather_icon/' + self.weather_daily['icon_list'][4] + '.png'))
        self.ui.icon_5.setPixmap(QPixmap('resource.qrl/weather_icon/' + self.weather_daily['icon_list'][5] + '.png'))
        self.ui.icon_6.setPixmap(QPixmap('resource.qrl/weather_icon/' + self.weather_daily['icon_list'][6] + '.png'))
        self.ui.icon_7.setPixmap(QPixmap('resource.qrl/weather_icon/' + self.weather_daily['icon_list'][7] + '.png'))

    def create_weather_daily(self, weather: dict):
        icon_list = []
        dt_list = []
        day_str = '   {dt}\n\n   {description}\n  восход {sunrise}\n   закат {sunset}\n   утром {morn}℃\n   ' \
                  'по ощущениям {feels_morn}℃\n    днём {day}℃\n   по ощущениям {feels_day}℃\n   вечером {eve}℃\n   ' \
                  'по ощущениям {feels_eve}℃\n   ночью {night}℃\n   по ощущениям {feels_night}℃\n  ' \
                  'давление {pressure}K/pa\n   влажность {humidity}\n   ветер\n   скорость {speed}м/с\n   ' \
                  'направление {deg}\n   порывы до {gust}м/с\n   облачность {clouds}%\n   индекс у/ф {uvi}\n'
        for i in range(len(weather['daily'])):
            day_dict = {'sunrise': strftime('%H:%M:%S', localtime(weather['daily'][i].get('sunrise', -10800))),
                        'sunset': strftime('%H:%M:%S', localtime(weather['daily'][i].get('sunset', -10800))),
                        'dt': strftime('%A\n   %d.%m.%Y', localtime(weather['daily'][i]['dt'])),
                        'morn': str(weather['daily'][i]['temp']['morn']),
                        'feels_morn': str(weather['daily'][i]['feels_like']['morn']),
                        'day': str(weather['daily'][i]['temp']['day']),
                        'feels_day': str(weather['daily'][i]['feels_like']['day']),
                        'eve': str(weather['daily'][i]['temp']['eve']),
                        'feels_eve': str(weather['daily'][i]['feels_like']['eve']),
                        'night': str(weather['daily'][i]['temp']['night']),
                        'feels_night': str(weather['daily'][i]['feels_like']['night']),
                        'pressure': str(weather['daily'][i]['pressure']),
                        'humidity': str(weather['daily'][i]['humidity']),
                        'speed': str(weather['daily'][i]['wind_speed']),
                        'deg': wind_deg_to_str(weather['daily'][i]['wind_deg']),
                        'gust': str(weather['daily'][i]['wind_gust']),
                        'clouds': str(weather['daily'][i]['clouds']),
                        'uvi': str(weather['daily'][i]['uvi']),
                        'description': weather['daily'][i]['weather'][0]['description']}
            self.weather_daily['day' + str(i)] = day_str.format_map(day_dict)
            icon_list.append(weather_dict['daily'][i]['weather'][0]['icon'])
            dt_list.append(strftime('%A\n%d.%m.%Y', localtime(weather['daily'][i]['dt'])))
        self.weather_daily['city_name'] = weather['city_name']
        self.weather_daily['icon_list'] = icon_list
        self.weather_daily['dt_list'] = dt_list
        pprint(self.weather_daily)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.setWindowTitle('Погода сейчас и на неделю')
    window.show()

    sys.exit(app.exec())
