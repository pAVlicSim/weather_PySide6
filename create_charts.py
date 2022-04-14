
from PySide6.QtCharts import QChart, QChartView, QSplineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt, QPoint, QPointF, QDateTime
from PySide6.QtGui import QPainter, QPen, QColor, QScreen
from PySide6.QtWidgets import QDialog, QVBoxLayout, QApplication, QButtonGroup, QHBoxLayout, QRadioButton
import create_weather_data


class TempChart(QChart):
    def __init__(self):
        super().__init__()
        graph_data = create_weather_data.GraphData()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        #
        self._y_axes = QValueAxis()
        self._y_axes.setRange(graph_data.yTemp_min_max[0], graph_data.yTemp_min_max[1])
        self._y_axes.setTickCount((graph_data.yTemp_min_max[1] - graph_data.yTemp_min_max[0]) / 2)
        self._y_axes.setTitleText('Градусы')
        #
        self._x_axes = QDateTimeAxis()
        self._x_axes.setFormat('ddd HH:MM')
        self._x_axes.setLabelsColor('orange')
        self._x_axes.setTickCount(24)
        self._x_axes.setLabelsAngle(290)
        self._x_axes.setTitleText('Часы')
        self._x_axes.setTitleBrush(QColor('orange'))
        self._x_axes.setRange(graph_data.x_axis_range[0], graph_data.x_axis_range[1])

        self.temp_series = QSplineSeries()
        self.temp_series.setName('Температура')
        self.temp_series.append(graph_data.temp_graph)
        self.temp_series.setPen(QPen(Qt.red, 3))

        self.feels_series = QSplineSeries()
        self.feels_series.setName('По ощущениям')
        self.feels_series.setPen(QPen(QColor('#FF7F7A'), 3))
        self.feels_series.append(graph_data.feels_graph)

        self.addAxis(self._y_axes, Qt.AlignLeft)
        self.addAxis(self._x_axes, Qt.AlignBottom)
        self.addSeries(self.feels_series)
        self.addSeries(self.temp_series)
        self.temp_series.attachAxis(self._y_axes)
        self.feels_series.attachAxis(self._y_axes)


class PressChart(QChart):
    def __init__(self):
        super().__init__()

        graph_data = create_weather_data.GraphData()
        self.setTheme(QChart.ChartThemeBlueCerulean)
        #
        self._x_axes = QDateTimeAxis()
        self._x_axes.setFormat('ddd HH:MM')
        self._x_axes.setLabelsColor('orange')
        self._x_axes.setTickCount(24)
        self._x_axes.setLabelsAngle(290)
        self._x_axes.setTitleText('Часы')
        self._x_axes.setTitleBrush(QColor('orange'))
        self._x_axes.setRange(graph_data.x_axis_range[0], graph_data.x_axis_range[1])

        self._yPress_axis = QValueAxis()
        self._yPress_axis.setRange(graph_data.yPress_min_max[0], graph_data.yPress_min_max[1])
        self._yPress_axis.setTitleText('гПа')

        self.press_series = QSplineSeries()
        self.press_series.append(graph_data.press_graph)
        self.press_series.setName('Давление')
        self.press_series.setPen(QPen(QColor('#7AE0FF'), 3))

        self.addAxis(self._yPress_axis, Qt.AlignLeft)
        self.addAxis(self._x_axes, Qt.AlignBottom)
        self.addSeries(self.press_series)
        self.press_series.attachAxis(self._yPress_axis)
