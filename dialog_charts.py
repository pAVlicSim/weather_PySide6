# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_charts.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                               QRadioButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_Dialog_charts(object):
    def setupUi(self, Dialog_charts):
        if not Dialog_charts.objectName():
            Dialog_charts.setObjectName(u"Dialog_charts")
        Dialog_charts.resize(707, 400)
        Dialog_charts.setStyleSheet(u"font: italic 12pt \"Sans Serif\";")
        self.verticalLayout_2 = QVBoxLayout(Dialog_charts)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog_charts)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.radioButton_temp = QRadioButton(Dialog_charts)
        self.radioButton_temp.setObjectName(u"radioButton_temp")

        self.horizontalLayout.addWidget(self.radioButton_temp)

        self.radioButton_press = QRadioButton(Dialog_charts)
        self.radioButton_press.setObjectName(u"radioButton_press")

        self.horizontalLayout.addWidget(self.radioButton_press)

        self.radioButton_humidity = QRadioButton(Dialog_charts)
        self.radioButton_humidity.setObjectName(u"radioButton_humidity")

        self.horizontalLayout.addWidget(self.radioButton_humidity)

        self.radioButton_uvi = QRadioButton(Dialog_charts)
        self.radioButton_uvi.setObjectName(u"radioButton_uvi")

        self.horizontalLayout.addWidget(self.radioButton_uvi)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog_charts)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.radio_temp_day = QRadioButton(Dialog_charts)
        self.radio_temp_day.setObjectName(u"radio_temp_day")

        self.horizontalLayout_2.addWidget(self.radio_temp_day)

        self.radio_temp_night = QRadioButton(Dialog_charts)
        self.radio_temp_night.setObjectName(u"radio_temp_night")

        self.horizontalLayout_2.addWidget(self.radio_temp_night)

        self.radio_week_press = QRadioButton(Dialog_charts)
        self.radio_week_press.setObjectName(u"radio_week_press")

        self.horizontalLayout_2.addWidget(self.radio_week_press)

        self.radio_week_humidity = QRadioButton(Dialog_charts)
        self.radio_week_humidity.setObjectName(u"radio_week_humidity")

        self.horizontalLayout_2.addWidget(self.radio_week_humidity)

        self.radio_week_uvi = QRadioButton(Dialog_charts)
        self.radio_week_uvi.setObjectName(u"radio_week_uvi")

        self.horizontalLayout_2.addWidget(self.radio_week_uvi)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog_charts)

        QMetaObject.connectSlotsByName(Dialog_charts)
    # setupUi

    def retranslateUi(self, Dialog_charts):
        Dialog_charts.setWindowTitle(QCoreApplication.translate("Dialog_charts",
                                                                u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 \u043f\u043e\u0433\u043e\u0434\u044b",
                                                                None))
        self.label.setText(
            QCoreApplication.translate("Dialog_charts", u"\u041d\u0430 \u0434\u0432\u0430 \u0434\u043d\u044f:", None))
        self.radioButton_temp.setText(QCoreApplication.translate("Dialog_charts",
                                                                 u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430",
                                                                 None))
        self.radioButton_press.setText(
            QCoreApplication.translate("Dialog_charts", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.radioButton_humidity.setText(
            QCoreApplication.translate("Dialog_charts", u"\u0412\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c",
                                       None))
        self.radioButton_uvi.setText(QCoreApplication.translate("Dialog_charts", u"\u0423/\u0424", None))
        self.label_2.setText(
            QCoreApplication.translate("Dialog_charts", u"\u041d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e:", None))
        self.radio_temp_day.setText(
            QCoreApplication.translate("Dialog_charts", u"\u0422\u0435\u043c\u043f. \u0434\u043d\u0451\u043c", None))
        self.radio_temp_night.setText(
            QCoreApplication.translate("Dialog_charts", u"\u0422\u0435\u043c\u043f. \u043d\u043e\u0447\u044c\u044e",
                                       None))
        self.radio_week_press.setText(QCoreApplication.translate("Dialog_charts",
                                                                 u"\u0410\u0442\u043c. \u0434\u0430\u0432\u043b\u0435\u043d\u0438\u0435",
                                                                 None))
        self.radio_week_humidity.setText(
            QCoreApplication.translate("Dialog_charts", u"\u0412\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c",
                                       None))
        self.radio_week_uvi.setText(QCoreApplication.translate("Dialog_charts",
                                                               u"\u0423\u043b\u044c\u0442\u0440\u0430\u0444\u0438\u043e\u043b\u0435\u0442",
                                                               None))
    # retranslateUi

