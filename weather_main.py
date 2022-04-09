import sys
from pprint import pprint

from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PySide6.QtCore import Qt
import create_weather_data
import create_weather_dict
from form import Ui_MainWindow
from graphics_dialog import GraphicsDialog

weather_dict = create_weather_dict.load_weather(create_weather_dict.load_geolocation('Москва'))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        label_now_text = create_weather_data.LabelNowText()
        table_hourly_data = create_weather_data.TableHourlyData()
        self.ui.label_title.setText(label_now_text.label_now_text['title'])
        self.ui.label_weather.setText(label_now_text.label_now_text['weather'])
        self.ui.tableWidget_hourly.setHorizontalHeaderLabels(table_hourly_data.horizontal_headers)
        self.ui.tableWidget_hourly.setVerticalHeaderLabels(table_hourly_data.vertical_headers)
        self.my_delegate = create_weather_data.AlignDelegate(self.ui.tableWidget_hourly)
        # pprint(weather_dict['hourly'][0])
        for i in range(self.ui.tableWidget_hourly.rowCount()):
            self.ui.tableWidget_hourly.setItem(i, 0, QTableWidgetItem(table_hourly_data.data_table_dict['temp'][i]))
            self.ui.tableWidget_hourly.setItem(i, 1, QTableWidgetItem(table_hourly_data.data_table_dict['pressure'][i]))
            self.ui.tableWidget_hourly.setItem(i, 2, QTableWidgetItem(table_hourly_data.data_table_dict['humidity'][i]))
            self.ui.tableWidget_hourly.setItem(i, 3, QTableWidgetItem(table_hourly_data.data_table_dict['wind'][i]))
            self.ui.tableWidget_hourly.setItem(i, 4,
                                               QTableWidgetItem(table_hourly_data.data_table_dict['dew_point'][i]))
            self.ui.tableWidget_hourly.setItem(i, 5, QTableWidgetItem(table_hourly_data.data_table_dict['uvi'][i]))
            self.ui.tableWidget_hourly.setItem(i, 6, QTableWidgetItem(table_hourly_data.data_table_dict['clouds'][i]))
        self.ui.tableWidget_hourly.setItemDelegate(self.my_delegate)
        self.ui.tableWidget_hourly.resizeColumnsToContents()

        self.graphics_dialog = GraphicsDialog()
        self.ui.action_temp.triggered.connect(self.dialog_show)

    def dialog_show(self):
        self.graphics_dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
