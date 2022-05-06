from pprint import pprint

from PySide6.QtCharts import QChart, QSplineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QColor, QFont
import dw_data

chart_font = QFont("Sans Serif", 12, QFont.StyleItalic)


class MyXAxis(QDateTimeAxis):
    def __init__(self):
        super().__init__()
        hd = dw_data.HourlyChartsData()
        self.setFormat('ddd HH:MM')
        self.setLabelsColor('orange')
        self.setTickCount(25)
        self.setLabelsAngle(270)
        self.setTitleText('Часы')
        self.setTitleBrush(QColor('orange'))
        self.setRange(hd.x_axisMin, hd.x_axsMax)
        self.setLabelsFont(chart_font)


class MyYAxis(QValueAxis):
    def __init__(self, ax_min: int, ax_max: int, dev: int, name: str):
        super().__init__()
        self.setRange(ax_min, ax_max)
        self.setTickCount((ax_max - ax_min) // dev + 1)
        self.setTitleText(name)
        self.setLabelsFont(chart_font)


class MySplineSeries(QSplineSeries):
    def __init__(self, name: str, list_series: list, color):
        super().__init__()
        self.setName(name)
        self.append(list_series)
        self.setPen(QPen(color, 3))


class TempChart(QChart):
    def __init__(self):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = dw_data.HourlyChartsData()
        #
        self._y_axis = MyYAxis(hd.y_tempAxisMin, hd.y_tempAxisMax, 2, 'Градусы')
        self._x_axis = MyXAxis()

        self.temp_series = MySplineSeries('Температура', hd.temp_series, Qt.red)
        self.feels_series = MySplineSeries('По ощущениям', hd.feels_series, Qt.magenta)

        self.addAxis(self._y_axis, Qt.AlignLeft)
        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addSeries(self.feels_series)
        self.addSeries(self.temp_series)
        self.temp_series.attachAxis(self._y_axis)
        self.feels_series.attachAxis(self._y_axis)


class PressChart(QChart):
    def __init__(self):
        super().__init__()

        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = dw_data.HourlyChartsData()
        #
        self._x_axis = MyXAxis()
        #
        self._yPress_axis = MyYAxis(hd.y_pressAxisMin, hd.y_pressAxisMax, 2, 'гПа')
        #
        self.press_series = MySplineSeries('Давление', hd.pressSeries, Qt.yellow)

        self.addAxis(self._yPress_axis, Qt.AlignLeft)
        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addSeries(self.press_series)
        self.press_series.attachAxis(self._yPress_axis)


class HumidityChart(QChart):
    def __init__(self):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = dw_data.HourlyChartsData()
        #
        self._x_axis = MyXAxis()
        #
        self._yHumidity_axis = MyYAxis(hd.y_humidityAxisMin, hd.y_humidityAxisMax, 10, '%')
        #
        self.humidity_series = MySplineSeries('Влажность', hd.humiditySeries, QColor('#7AE0FF'))
        #
        self.addSeries(self.humidity_series)
        self.addAxis(self._yHumidity_axis, Qt.AlignLeft)
        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.humidity_series.attachAxis(self._yHumidity_axis)


class UviChart(QChart):
    def __init__(self):
        super().__init__()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        hd = dw_data.HourlyChartsData()
        self._x_axis = MyXAxis()
        self._y_axis = MyYAxis(hd.y_uviAxisMin, hd.y_uviAxisMax, 2, 'Коэфф.')
        self.uvi_series = MySplineSeries('Ультрафиолет', hd.uviSeries, QColor('#FF6E1A'))

        self.addAxis(self._x_axis, Qt.AlignBottom)
        self.addAxis(self._y_axis, Qt.AlignLeft)
        self.addSeries(self.uvi_series)
        self.uvi_series.attachAxis(self._y_axis)
