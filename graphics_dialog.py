import os

from PySide6.QtCharts import QChart, QChartView, QSplineSeries, QValueAxis, QDateTimeAxis
from PySide6.QtCore import Qt, QPoint, QPointF, QDateTime
from PySide6.QtGui import QPainter, QPen, QColor, QScreen
from PySide6.QtWidgets import QDialog, QVBoxLayout, QApplication
import create_weather_data


class GraphicsDialog(QDialog):
    def __init__(self):
        super().__init__()
        scr = QScreen()
        SrcSize = QScreen.availableGeometry(QApplication.primaryScreen()).width()
        print(SrcSize)
        self.resize(QScreen.availableGeometry(QApplication.primaryScreen()).width(), 500)
        self.verticalLayout = QVBoxLayout(self)
        self.setLayout(self.verticalLayout)
        self.temp_chart = QChart()
        self._y_axes = QValueAxis()
        self._x_axes = QDateTimeAxis()
        self.temp_series = QSplineSeries()
        self.temp_series.setName('Temp.')
        self.temp_series.setPen(QPen(Qt.red, 3))
        graph_data = create_weather_data.GraphData()
        self.temp_series.append(graph_data.temp_graph)
        self.temp_chart.addSeries(self.temp_series)
        self._y_axes.setRange(graph_data.y_axis_range[0], graph_data.y_axis_range[1])
        self._y_axes.setTickCount(10)
        self._y_axes.setTickInterval(2.0)
        self._x_axes.setFormat('d HH:MM')
        self._x_axes.setLabelsColor('blue')
        self._x_axes.setTickCount(24)
        self._x_axes.setLabelsAngle(290)
        self._x_axes.setRange(graph_data.x_axis_range[0], graph_data.x_axis_range[1])
        self.temp_chart.addAxis(self._y_axes, Qt.AlignLeft)
        self.temp_chart.addAxis(self._x_axes, Qt.AlignBottom)

        self.graph_view = QChartView(self.temp_chart)
        self.graph_view.setRenderHint(QPainter.Antialiasing)
        self.verticalLayout.addWidget(self.graph_view)
