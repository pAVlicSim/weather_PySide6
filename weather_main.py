import sys
from pprint import pprint
from datetime import datetime as dt
from PySide6.QtWidgets import QMainWindow, QApplication
import create_weather_dict
from form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        weather_dict = create_weather_dict.load_weather(create_weather_dict.load_geolocation('Москва'))
        weather_now = weather_dict['current']
        self.ui.label_title.setText(
            f'{weather_dict["name_city"]}  погода на: {dt.fromtimestamp(weather_now["dt"]):%A %d.%m.%y  %H:%M}')
        self.ui.label_weather.setText(f'Температура: {weather_now["temp"]: .1f}℃\n'
                                      f'По ощущениям: {weather_now["feels_like"]: .1f}℃\n'
                                      f'Атмосферное давление:\n{weather_now["pressure"]}kPa')
        pprint(weather_now)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
