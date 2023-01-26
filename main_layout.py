# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_layout.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDoubleSpinBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 446)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        my_icon = QIcon()
        my_icon.addFile("./icon.png")
        MainWindow.setWindowIcon(my_icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.rcms_id_input = QLineEdit(self.centralwidget)
        self.rcms_id_input.setObjectName(u"rcms_id_input")
        self.rcms_id_input.setGeometry(QRect(10, 10, 300, 25))
        self.rcms_id_input.setFont(font)
        self.rcms_pwd_input = QLineEdit(self.centralwidget)
        self.rcms_pwd_input.setObjectName(u"rcms_pwd_input")
        self.rcms_pwd_input.setGeometry(QRect(10, 43, 300, 25))
        self.rcms_pwd_input.setFont(font)
        self.render_delay_label = QLabel(self.centralwidget)
        self.render_delay_label.setObjectName(u"render_delay_label")
        self.render_delay_label.setGeometry(QRect(10, 76, 125, 25))
        self.render_delay_label.setFont(font)
        self.anti_auto_label = QLabel(self.centralwidget)
        self.anti_auto_label.setObjectName(u"anti_auto_label")
        self.anti_auto_label.setGeometry(QRect(10, 109, 125, 25))
        self.anti_auto_label.setFont(font)
        self.render_delay = QDoubleSpinBox(self.centralwidget)
        self.render_delay.setObjectName(u"render_delay")
        self.render_delay.setGeometry(QRect(143, 76, 167, 25))
        self.render_delay.setFont(font)
        self.render_delay.setMinimum(1.000000000000000)
        self.render_delay.setMaximum(1000.000000000000000)
        self.render_delay.setValue(3.000000000000000)
        self.anti_auto = QDoubleSpinBox(self.centralwidget)
        self.anti_auto.setObjectName(u"anti_auto")
        self.anti_auto.setGeometry(QRect(143, 109, 167, 25))
        self.anti_auto.setFont(font)
        self.anti_auto.setDecimals(2)
        self.anti_auto.setMinimum(0.000000000000000)
        self.anti_auto.setMaximum(1000.000000000000000)
        self.anti_auto.setValue(1.000000000000000)
        self.schedule_time_label = QLabel(self.centralwidget)
        self.schedule_time_label.setObjectName(u"schedule_time_label")
        self.schedule_time_label.setGeometry(QRect(10, 142, 111, 25))
        self.schedule_time_label.setFont(font)
        self.schedule_time = QTimeEdit(self.centralwidget)
        self.schedule_time.setObjectName(u"schedule_time")
        self.schedule_time.setGeometry(QRect(129, 142, 132, 25))
        self.schedule_time.setFont(font)
        self.schedule_time.setAlignment(Qt.AlignCenter)
        self.schedule_time.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.schedule_time.setCurrentSection(QDateTimeEdit.HourSection)
        self.schedule_time.setCurrentSectionIndex(0)
        self.schedule_time.setTimeSpec(Qt.UTC)
        self.schedule_time.setTime(QTime(0, 0, 0))
        self.add_schedule_time_btn = QPushButton(self.centralwidget)
        self.add_schedule_time_btn.setObjectName(u"add_schedule_time_btn")
        self.add_schedule_time_btn.setGeometry(QRect(269, 142, 41, 25))
        self.add_schedule_time_btn.setFont(font)
        self.added_schedule_list = QTextBrowser(self.centralwidget)
        self.added_schedule_list.setObjectName(u"added_schedule_list")
        self.added_schedule_list.setGeometry(QRect(10, 175, 300, 200))
        self.added_schedule_list.setFont(font)
        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(235, 383, 75, 25))
        self.start_btn.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Auto RCMS for LJM", None))
        self.rcms_id_input.setStatusTip("RCMS 계정의 아이디를 입력해주세요")
        self.rcms_id_input.setPlaceholderText(QCoreApplication.translate("MainWindow", "RCMS 계정 아이디", None))
        self.rcms_pwd_input.setStatusTip("RCMS 계정의 비밀번호를 입력해주세요")
        self.rcms_pwd_input.setPlaceholderText(QCoreApplication.translate("MainWindow", "RCMS 계정 비밀번호", None))
        self.render_delay_label.setStatusTip("화면이 렌더링 되는 시간을 고려한 동작 딜레이")
        self.render_delay_label.setText(QCoreApplication.translate("MainWindow", "화면 렌더 딜레이", None))
        self.anti_auto_label.setStatusTip("로봇 감지나 애니메이션 효과를 고려한 동작 딜레이")
        self.anti_auto_label.setText(QCoreApplication.translate("MainWindow", "로봇 방지 딜레이", None))
        self.render_delay.setStatusTip("초(1.00 ~ 1000.00)")
        self.anti_auto.setStatusTip("초(1.00 ~ 1000.00)")
        self.start_btn.setStatusTip("작업 시작")
        self.start_btn.setText(QCoreApplication.translate("MainWindow", "실행", None))
        self.schedule_time.setStatusTip("hh:mm(00:00~23:59)")
        self.schedule_time.setDisplayFormat(QCoreApplication.translate("MainWindow", "hh:mm", None))
        self.added_schedule_list.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.schedule_time_label.setStatusTip("프로그램이 켜진 동안에 자동 실행될 시각을 설정하세요")
        self.schedule_time_label.setText(QCoreApplication.translate("MainWindow", "자동 실행 시각 설정", None))
        self.add_schedule_time_btn.setText(QCoreApplication.translate("MainWindow", "추가", None))
