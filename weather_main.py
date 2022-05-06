import sys
from pprint import pprint

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

import dw_dict
import dw_data
from form import Ui_MainWindow
from dialog_charts_ import DialogCarts

weather_dict = dw_dict.load_weather(dw_dict.load_geolocation('Москва'))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        f = open('my_qssStyle.qss', 'r')
        with f:
            qss = f.read()
        self.setStyleSheet(qss)
        thd = dw_data.TableHourlyData()
        wd = dw_data.WeekData()
        self.ui.label_title.setText(dw_data.create_label_now_text()['title'])
        self.ui.label_weather.setText(dw_data.create_label_now_text()['weather'])
        self.ui.tableWidget_hourly.setHorizontalHeaderLabels(thd.horizontal_headers)
        self.ui.tableWidget_hourly.setVerticalHeaderLabels(thd.vertical_headers)
        self.my_alignDelegate = dw_data.AlignDelegate()
        self.my_iconDelegate = dw_data.IconDelegate()

        for i in range(self.ui.tableWidget_hourly.rowCount()):
            self.ui.tableWidget_hourly.setItem(i, 0, QTableWidgetItem(
                QIcon(f"weather_icons/{thd.data_table_dict['icon'][i]}.png"), ''))
            self.ui.tableWidget_hourly.setItem(i, 1, QTableWidgetItem(thd.data_table_dict['temp'][i]))
            self.ui.tableWidget_hourly.setItem(i, 2, QTableWidgetItem(thd.data_table_dict['feels'][i]))
            self.ui.tableWidget_hourly.setItem(i, 3, QTableWidgetItem(thd.data_table_dict['pressure'][i]))
            self.ui.tableWidget_hourly.setItem(i, 4, QTableWidgetItem(thd.data_table_dict['humidity'][i]))
            self.ui.tableWidget_hourly.setItem(i, 5, QTableWidgetItem(thd.data_table_dict['wind'][i]))
            self.ui.tableWidget_hourly.setItem(i, 6,
                                               QTableWidgetItem(thd.data_table_dict['dew_point'][i]))
            self.ui.tableWidget_hourly.setItem(i, 7, QTableWidgetItem(thd.data_table_dict['uvi'][i]))
            self.ui.tableWidget_hourly.setItem(i, 8, QTableWidgetItem(thd.data_table_dict['clouds'][i]))
            self.ui.tableWidget_hourly.setItem(i, 9, QTableWidgetItem(thd.data_table_dict['precipitation'][i]))
        self.ui.tableWidget_hourly.setItemDelegate(self.my_alignDelegate)
        self.ui.tableWidget_hourly.setItemDelegateForColumn(0, self.my_iconDelegate)
        self.ui.tableWidget_hourly.resizeColumnsToContents()

        label_icon_lst = [self.ui.icon_0, self.ui.icon_1, self.ui.icon_2, self.ui.icon_3, self.ui.icon_4,
                          self.ui.icon_5, self.ui.icon_6, self.ui.icon_7]
        label_text_lst = [self.ui.label_0, self.ui.label_1, self.ui.label_2, self.ui.label_3, self.ui.label_4,
                          self.ui.label_5, self.ui.label_6, self.ui.label_7]

        for i in range(len(label_icon_lst)):
            label_icon_lst[i].setPixmap(QPixmap(f"weather_icons/{wd.week_data['icon'][i]}.png"))
            label_text_lst[i].setText(wd.week_data['weather'][i])

        self.dialog_charts = DialogCarts()
        self.ui.action_charts48hours.triggered.connect(self.dialog_show)

    def dialog_show(self):
        self.dialog_charts.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    # f = open('my_qssStyle.qss', 'r')
    # with f:
    #     qss = f.read()
    window.setWindowIcon(QIcon('program_icon.png'))
    window.resize(1250, 700)
    window.show()

    sys.exit(app.exec())
