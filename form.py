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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QMainWindow,
                               QMenu, QMenuBar, QScrollArea, QSizePolicy,
                               QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 622)
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
        self.tab_week = QWidget()
        self.tab_week.setObjectName(u"tab_week")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_week)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.scrollArea_2 = QScrollArea(self.tab_week)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -1180, 967, 1662))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.icon_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.icon_6.setObjectName(u"icon_6")
        self.icon_6.setFrameShape(QFrame.Box)
        self.icon_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_6, 6, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.label_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFrameShape(QFrame.Box)
        self.label_1.setFrameShadow(QFrame.Plain)
        self.label_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_1, 1, 1, 1, 1)

        self.label_0 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_0.setObjectName(u"label_0")
        self.label_0.setFrameShape(QFrame.Box)
        self.label_0.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_0, 0, 1, 1, 1)

        self.icon_1 = QLabel(self.scrollAreaWidgetContents_2)
        self.icon_1.setObjectName(u"icon_1")
        self.icon_1.setFrameShape(QFrame.Box)
        self.icon_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_1, 1, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)

        self.icon_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.icon_3.setObjectName(u"icon_3")
        self.icon_3.setFrameShape(QFrame.Box)
        self.icon_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_3, 3, 0, 1, 1)

        self.icon_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.icon_5.setObjectName(u"icon_5")
        self.icon_5.setFrameShape(QFrame.Box)
        self.icon_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_5, 5, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 6, 1, 1, 1)

        self.icon_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setFrameShape(QFrame.Box)
        self.icon_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_2, 2, 0, 1, 1)

        self.icon_0 = QLabel(self.scrollAreaWidgetContents_2)
        self.icon_0.setObjectName(u"icon_0")
        self.icon_0.setFrameShape(QFrame.Box)
        self.icon_0.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_0, 0, 0, 1, 1)

        self.icon_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.icon_4.setObjectName(u"icon_4")
        self.icon_4.setFrameShape(QFrame.Box)
        self.icon_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_4, 4, 0, 1, 1)

        self.icon_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.icon_7.setObjectName(u"icon_7")
        self.icon_7.setFrameShape(QFrame.Box)
        self.icon_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.icon_7, 7, 0, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 200)
        self.gridLayout.setRowMinimumHeight(0, 200)
        self.gridLayout.setRowMinimumHeight(1, 200)
        self.gridLayout.setRowMinimumHeight(2, 200)
        self.gridLayout.setRowMinimumHeight(3, 200)
        self.gridLayout.setRowMinimumHeight(4, 200)
        self.gridLayout.setRowMinimumHeight(5, 200)
        self.gridLayout.setRowMinimumHeight(6, 200)
        self.gridLayout.setRowMinimumHeight(7, 200)

        self.verticalLayout_4.addLayout(self.gridLayout)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_6.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_week, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1031, 31))
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

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0451 \u043e \u043f\u043e\u0433\u043e\u0434\u0435",
                                       None))
        self.action_charts48hours.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041d\u0430 \u0434\u0432\u043e\u0435 \u0441\u0443\u0442\u043e\u043a",
                                                                     None))
        self.action_chartsWeek.setText(
            QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.action_uvi.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0424", None))
        self.action_wind.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0442\u0435\u0440", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_weather.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_now), QCoreApplication.translate("MainWindow",
                                                                                                   u"\u041f\u043e\u0433\u043e\u0434\u0430 \u0441\u0435\u0439\u0447\u0430\u0441",
                                                                                                   None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hourly), QCoreApplication.translate("MainWindow",
                                                                                                      u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u043e \u043d\u0430 \u0434\u0432\u0430 \u0434\u043d\u044f",
                                                                                                      None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_0.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_0.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.icon_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_week), QCoreApplication.translate("MainWindow",
                                                                                                    u"\u041f\u043e\u0433\u043e\u0434\u0430 \u043d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e",
                                                                                                    None))
        self.menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
    # retranslateUi

