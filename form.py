# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QScrollArea, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(868, 622)
        MainWindow.setStyleSheet(u"font: italic 16pt \"Nimbus Roman [urw]\";")
        self.action_charts48hours = QAction(MainWindow)
        self.action_charts48hours.setObjectName(u"action_charts48hours")
        self.action_charts48hours.setCheckable(True)
        self.action_chartsWeek = QAction(MainWindow)
        self.action_chartsWeek.setObjectName(u"action_chartsWeek")
        self.action_chartsWeek.setCheckable(True)
        self.action_uvi = QAction(MainWindow)
        self.action_uvi.setObjectName(u"action_uvi")
        self.action_uvi.setCheckable(True)
        self.action_wind = QAction(MainWindow)
        self.action_wind.setObjectName(u"action_wind")
        self.action_wind.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"font: italic 16pt \"Nimbus Roman [urw]\";")
        self.tab_now = QWidget()
        self.tab_now.setObjectName(u"tab_now")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_now)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_title = QLabel(self.tab_now)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 50))
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_title)

        self.label_weather = QLabel(self.tab_now)
        self.label_weather.setObjectName(u"label_weather")
        self.label_weather.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_weather)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_now, "")
        self.tab_hourly = QWidget()
        self.tab_hourly.setObjectName(u"tab_hourly")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_hourly)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.tab_hourly)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 824, 480))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget_hourly = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget_hourly.columnCount() < 10):
            self.tableWidget_hourly.setColumnCount(10)
        if (self.tableWidget_hourly.rowCount() < 48):
            self.tableWidget_hourly.setRowCount(48)
        self.tableWidget_hourly.setObjectName(u"tableWidget_hourly")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget_hourly.sizePolicy().hasHeightForWidth())
        self.tableWidget_hourly.setSizePolicy(sizePolicy)
        self.tableWidget_hourly.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_hourly.setTextElideMode(Qt.ElideNone)
        self.tableWidget_hourly.setRowCount(48)
        self.tableWidget_hourly.setColumnCount(10)
        self.tableWidget_hourly.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_hourly.horizontalHeader().setHighlightSections(False)
        self.tableWidget_hourly.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_hourly.verticalHeader().setMinimumSectionSize(80)
        self.tableWidget_hourly.verticalHeader().setDefaultSectionSize(80)
        self.tableWidget_hourly.verticalHeader().setHighlightSections(False)
        self.tableWidget_hourly.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_hourly.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_4.addWidget(self.tableWidget_hourly)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab_hourly, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_25 = QLabel(self.tab_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_26 = QLabel(self.tab_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_4.addWidget(self.label_26, 0, 1, 1, 1)

        self.label_27 = QLabel(self.tab_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_4.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_28 = QLabel(self.tab_3)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_4.addWidget(self.label_28, 2, 0, 1, 1)

        self.label_29 = QLabel(self.tab_3)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_4.addWidget(self.label_29, 3, 0, 1, 1)

        self.label_30 = QLabel(self.tab_3)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_4.addWidget(self.label_30, 1, 1, 1, 1)

        self.label_31 = QLabel(self.tab_3)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_4.addWidget(self.label_31, 2, 1, 1, 1)

        self.label_32 = QLabel(self.tab_3)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_4.addWidget(self.label_32, 3, 1, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_4)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_33 = QLabel(self.tab_3)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 0, 0, 1, 1)

        self.label_36 = QLabel(self.tab_3)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 3, 0, 1, 1)

        self.label_35 = QLabel(self.tab_3)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 2, 0, 1, 1)

        self.label_34 = QLabel(self.tab_3)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_6.addWidget(self.label_34, 1, 0, 1, 1)

        self.label_37 = QLabel(self.tab_3)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 0, 1, 1, 1)

        self.label_38 = QLabel(self.tab_3)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 1, 1, 1, 1)

        self.label_39 = QLabel(self.tab_3)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 2, 1, 1, 1)

        self.label_40 = QLabel(self.tab_3)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 3, 1, 1, 1)


        self.horizontalLayout_5.addLayout(self.gridLayout_6)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")

        self.horizontalLayout_5.addLayout(self.gridLayout_7)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.horizontalLayout_5.addLayout(self.gridLayout_8)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")

        self.horizontalLayout_5.addLayout(self.gridLayout_9)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")

        self.horizontalLayout_5.addLayout(self.gridLayout_11)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")

        self.horizontalLayout_5.addLayout(self.gridLayout_10)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.horizontalLayout_5.addLayout(self.gridLayout_5)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_3, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 868, 31))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_charts48hours)
        self.menu.addAction(self.action_chartsWeek)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0451 \u043e \u043f\u043e\u0433\u043e\u0434\u0435", None))
        self.action_charts48hours.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0434\u0432\u043e\u0435 \u0441\u0443\u0442\u043e\u043a", None))
        self.action_chartsWeek.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.action_uvi.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0424", None))
        self.action_wind.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0442\u0435\u0440", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_weather.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_now), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430 \u0441\u0435\u0439\u0447\u0430\u0441", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hourly), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u043e \u043d\u0430 \u0434\u0432\u0430 \u0434\u043d\u044f", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430 \u043d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
    # retranslateUi

