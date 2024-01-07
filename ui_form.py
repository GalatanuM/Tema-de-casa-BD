# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QTimeEdit, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(866, 340)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 851, 291))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.layoutWidget = QWidget(self.page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(370, 60, 110, 160))
        self.layoutWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.layoutWidget1 = QWidget(self.page_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1, 1, 840, 286))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.calendarWidget = QCalendarWidget(self.layoutWidget1)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_4.addWidget(self.calendarWidget)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.timeEdit = QTimeEdit(self.layoutWidget1)
        self.timeEdit.setObjectName(u"timeEdit")

        self.verticalLayout_4.addWidget(self.timeEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.calendarWidget_2 = QCalendarWidget(self.layoutWidget1)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")

        self.verticalLayout_3.addWidget(self.calendarWidget_2)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)

        self.timeEdit_2 = QTimeEdit(self.layoutWidget1)
        self.timeEdit_2.setObjectName(u"timeEdit_2")

        self.verticalLayout_3.addWidget(self.timeEdit_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.pushButton_3 = QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_7.addWidget(self.pushButton_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_7 = QPushButton(self.layoutWidget1)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.listWidget = QListWidget(self.layoutWidget1)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.pushButton_4 = QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_8 = QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_2.addWidget(self.pushButton_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.layoutWidget2 = QWidget(self.page_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(270, 10, 320, 250))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_7)

        self.listWidget_2 = QListWidget(self.layoutWidget2)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_6.addWidget(self.listWidget_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_5 = QPushButton(self.layoutWidget2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.pushButton_9 = QPushButton(self.page_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(380, 230, 91, 24))
        self.layoutWidget3 = QWidget(self.page_4)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(240, 40, 371, 178))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.label_9 = QLabel(self.layoutWidget3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_10)

        self.label_11 = QLabel(self.layoutWidget3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_11)

        self.label_8 = QLabel(self.layoutWidget3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_12)

        self.label_13 = QLabel(self.layoutWidget3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lineEdit_3 = QLineEdit(self.layoutWidget3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_8.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.layoutWidget3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_8.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.layoutWidget3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_8.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.layoutWidget3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_8.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.layoutWidget3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_8.addWidget(self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.layoutWidget3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_8.addWidget(self.lineEdit_8)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.pushButton_10 = QPushButton(self.page_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(389, 260, 71, 24))
        self.stackedWidget.addWidget(self.page_4)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 866, 21))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Password", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"Login", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"Register", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Check-In Date", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"Check-In Hour", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"Check-Out Date", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"Check-Out Hour", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainWindow", u"Check availability", None))
        self.pushButton_7.setText(QCoreApplication.translate("mainWindow", u"Log Out", None))
        self.pushButton_4.setText(QCoreApplication.translate("mainWindow", u"Reserve parking spot", None))
        self.pushButton_8.setText(QCoreApplication.translate("mainWindow", u"My reservations", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"Your reservations", None))
        self.pushButton_5.setText(QCoreApplication.translate("mainWindow", u"Back", None))
        self.pushButton_6.setText(QCoreApplication.translate("mainWindow", u"Cancel reservation", None))
        self.pushButton_9.setText(QCoreApplication.translate("mainWindow", u"Register", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"First name:", None))
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"Last name:", None))
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"Email address:", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"Username:", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"Password:", None))
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"Confirm password:", None))
        self.pushButton_10.setText(QCoreApplication.translate("mainWindow", u"Back", None))
    # retranslateUi

