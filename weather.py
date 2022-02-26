# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                               QLabel, QLayout, QLineEdit, QPushButton,
                               QScrollArea, QSizePolicy, QSpacerItem, QTabWidget,
                               QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(808, 527)
        Form.setStyleSheet(u"font: 16pt \"Noto Sans\";")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.enter_city_name = QLineEdit(Form)
        self.enter_city_name.setObjectName(u"enter_city_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enter_city_name.sizePolicy().hasHeightForWidth())
        self.enter_city_name.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.enter_city_name)

        self.push_source_city = QPushButton(Form)
        self.push_source_city.setObjectName(u"push_source_city")

        self.horizontalLayout.addWidget(self.push_source_city)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox_history = QComboBox(Form)
        self.comboBox_history.setObjectName(u"comboBox_history")
        self.comboBox_history.setMaxCount(30)
        self.comboBox_history.setDuplicatesEnabled(True)

        self.horizontalLayout.addWidget(self.comboBox_history)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.ClosedHandCursor))
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tab__one_day = QWidget()
        self.tab__one_day.setObjectName(u"tab__one_day")
        self.verticalLayout_2 = QVBoxLayout(self.tab__one_day)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.push_now_graph = QPushButton(self.tab__one_day)
        self.push_now_graph.setObjectName(u"push_now_graph")

        self.horizontalLayout_2.addWidget(self.push_now_graph)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_now = QLabel(self.tab__one_day)
        self.label_now.setObjectName(u"label_now")
        self.label_now.setCursor(QCursor(Qt.OpenHandCursor))
        self.label_now.setScaledContents(False)
        self.label_now.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_now)

        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab__one_day, "")
        self.tab_two_days = QWidget()
        self.tab_two_days.setObjectName(u"tab_two_days")
        self.tab_two_days.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalLayout_5 = QVBoxLayout(self.tab_two_days)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.push_dayli_two_graph = QPushButton(self.tab_two_days)
        self.push_dayli_two_graph.setObjectName(u"push_dayli_two_graph")

        self.horizontalLayout_3.addWidget(self.push_dayli_two_graph)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_day1 = QLabel(self.tab_two_days)
        self.label_day1.setObjectName(u"label_day1")
        self.label_day1.setCursor(QCursor(Qt.OpenHandCursor))
        self.label_day1.setAcceptDrops(True)
        self.label_day1.setScaledContents(False)
        self.label_day1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_day1)

        self.label_day2 = QLabel(self.tab_two_days)
        self.label_day2.setObjectName(u"label_day2")
        self.label_day2.setCursor(QCursor(Qt.OpenHandCursor))
        self.label_day2.setScaledContents(False)
        self.label_day2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_day2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_two_days, "")
        self.tab_week = QWidget()
        self.tab_week.setObjectName(u"tab_week")
        self.verticalLayout_7 = QVBoxLayout(self.tab_week)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.push_week_graph = QPushButton(self.tab_week)
        self.push_week_graph.setObjectName(u"push_week_graph")

        self.horizontalLayout_5.addWidget(self.push_week_graph)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.label_city_week = QLabel(self.tab_week)
        self.label_city_week.setObjectName(u"label_city_week")
        self.label_city_week.setScaledContents(True)
        self.label_city_week.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_city_week)

        self.scrollArea = QScrollArea(self.tab_week)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(-1739, 0, 2472, 329))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.icon_0 = QLabel(self.scrollAreaWidgetContents)
        self.icon_0.setObjectName(u"icon_0")
        self.icon_0.setMinimumSize(QSize(300, 100))
        self.icon_0.setFrameShape(QFrame.Box)
        self.icon_0.setFrameShadow(QFrame.Raised)
        self.icon_0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.icon_0)

        self.label_week0 = QLabel(self.scrollAreaWidgetContents)
        self.label_week0.setObjectName(u"label_week0")
        self.label_week0.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_week0)

        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.icon_1 = QLabel(self.scrollAreaWidgetContents)
        self.icon_1.setObjectName(u"icon_1")
        self.icon_1.setMinimumSize(QSize(300, 100))
        self.icon_1.setFrameShape(QFrame.Box)
        self.icon_1.setFrameShadow(QFrame.Raised)
        self.icon_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.icon_1)

        self.label_week1 = QLabel(self.scrollAreaWidgetContents)
        self.label_week1.setObjectName(u"label_week1")
        self.label_week1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_week1)

        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.icon_2 = QLabel(self.scrollAreaWidgetContents)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setMinimumSize(QSize(300, 100))
        self.icon_2.setFrameShape(QFrame.Box)
        self.icon_2.setFrameShadow(QFrame.Raised)
        self.icon_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.icon_2)

        self.label_week2 = QLabel(self.scrollAreaWidgetContents)
        self.label_week2.setObjectName(u"label_week2")
        self.label_week2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_week2)

        self.horizontalLayout_7.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.icon_3 = QLabel(self.scrollAreaWidgetContents)
        self.icon_3.setObjectName(u"icon_3")
        self.icon_3.setMinimumSize(QSize(300, 100))
        self.icon_3.setFrameShape(QFrame.Box)
        self.icon_3.setFrameShadow(QFrame.Raised)
        self.icon_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.icon_3)

        self.label_week3 = QLabel(self.scrollAreaWidgetContents)
        self.label_week3.setObjectName(u"label_week3")
        self.label_week3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_week3)

        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.icon_4 = QLabel(self.scrollAreaWidgetContents)
        self.icon_4.setObjectName(u"icon_4")
        self.icon_4.setMinimumSize(QSize(300, 100))
        self.icon_4.setFrameShape(QFrame.Box)
        self.icon_4.setFrameShadow(QFrame.Raised)
        self.icon_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.icon_4)

        self.label_week4 = QLabel(self.scrollAreaWidgetContents)
        self.label_week4.setObjectName(u"label_week4")
        self.label_week4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_week4)

        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.icon_5 = QLabel(self.scrollAreaWidgetContents)
        self.icon_5.setObjectName(u"icon_5")
        self.icon_5.setMinimumSize(QSize(300, 100))
        self.icon_5.setFrameShape(QFrame.Box)
        self.icon_5.setFrameShadow(QFrame.Raised)
        self.icon_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.icon_5)

        self.label_week5 = QLabel(self.scrollAreaWidgetContents)
        self.label_week5.setObjectName(u"label_week5")
        self.label_week5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_week5)

        self.horizontalLayout_7.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.icon_6 = QLabel(self.scrollAreaWidgetContents)
        self.icon_6.setObjectName(u"icon_6")
        self.icon_6.setMinimumSize(QSize(300, 100))
        self.icon_6.setFrameShape(QFrame.Box)
        self.icon_6.setFrameShadow(QFrame.Raised)
        self.icon_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.icon_6)

        self.label_week6 = QLabel(self.scrollAreaWidgetContents)
        self.label_week6.setObjectName(u"label_week6")
        self.label_week6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_week6)

        self.horizontalLayout_7.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.icon_7 = QLabel(self.scrollAreaWidgetContents)
        self.icon_7.setObjectName(u"icon_7")
        self.icon_7.setMinimumSize(QSize(300, 100))
        self.icon_7.setFrameShape(QFrame.Box)
        self.icon_7.setFrameShadow(QFrame.Raised)
        self.icon_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.icon_7)

        self.label_week7 = QLabel(self.scrollAreaWidgetContents)
        self.label_week7.setObjectName(u"label_week7")
        self.label_week7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_week7)

        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.verticalLayout_6.setStretch(2, 1)

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab_week, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.enter_city_name.setPlaceholderText(QCoreApplication.translate("Form",
                                                                           u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430",
                                                                           None))
        self.push_source_city.setText(
            QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form",
                                                        u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432",
                                                        None))
        self.push_now_graph.setText(
            QCoreApplication.translate("Form", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.label_now.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab__one_day),
                                  QCoreApplication.translate("Form", u"\u0441\u0435\u0439\u0447\u0430\u0441", None))
        self.push_dayli_two_graph.setText(
            QCoreApplication.translate("Form", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.label_day1.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_day2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_two_days), QCoreApplication.translate("Form",
                                                                                                        u"\u043d\u0430 \u0434\u0432\u0430 \u0434\u043d\u044f",
                                                                                                        None))
        self.push_week_graph.setText(
            QCoreApplication.translate("Form", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.label_city_week.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.icon_0.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_week0.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.icon_1.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_week1.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.icon_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_week2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.icon_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_week3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.icon_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_week4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.icon_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_week5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.icon_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_week6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.icon_7.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_week7.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_week), QCoreApplication.translate("Form",
                                                                                                    u"\u043d\u0430 \u043d\u0435\u0434\u0435\u043b\u044e",
                                                                                                    None))
    # retranslateUi
