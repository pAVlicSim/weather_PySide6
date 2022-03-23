import form

form.Ui_MainWindow.label_date_2.setText(f'Погода: {weather_dict["name_city"]}   '
                                     f'{dt.fromtimestamp(weather_now["dt"]):%A %d.%m.%y  %H:%M}')
        self.ui.label_temp.setText(f'Температура: {weather_now["temp"]: .1f}℃\n'
                                   f'По ощущениям: {weather_now["feels_like"]: .1f}℃')
        self.ui.label_pressure.setText(f'Атмосферное давление:\n{weather_now["pres