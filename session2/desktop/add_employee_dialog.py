# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_employee_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)
from api import *
import bcrypt
from datetime import date



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(500, 435)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(500, 435))
        Dialog.setMaximumSize(QSize(500, 435))
        Dialog.setStyleSheet(u"background-color: white;")
        Dialog.setModal(True)
        self.verticalLayout_20 = QVBoxLayout(Dialog)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QWidget{\n"
"	background-color: white;\n"
"}")
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_14 = QVBoxLayout(self.tab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(224, 244, 200);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: black;")

        self.verticalLayout_5.addWidget(self.label_5)

        self.input_date_of_birth = QDateEdit(self.frame)
        self.input_date_of_birth.setObjectName(u"input_date_of_birth")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_date_of_birth.sizePolicy().hasHeightForWidth())
        self.input_date_of_birth.setSizePolicy(sizePolicy1)
        self.input_date_of_birth.setMinimumSize(QSize(0, 30))
        self.input_date_of_birth.setStyleSheet(u"background-color: white;\n"
"color: black;")

        self.verticalLayout_5.addWidget(self.input_date_of_birth)


        self.verticalLayout_18.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: black;")

        self.verticalLayout.addWidget(self.label)

        self.input_full_name = QLineEdit(self.frame)
        self.input_full_name.setObjectName(u"input_full_name")
        sizePolicy1.setHeightForWidth(self.input_full_name.sizePolicy().hasHeightForWidth())
        self.input_full_name.setSizePolicy(sizePolicy1)
        self.input_full_name.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setKerning(True)
        self.input_full_name.setFont(font)
        self.input_full_name.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"}")

        self.verticalLayout.addWidget(self.input_full_name)


        self.verticalLayout_18.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: black;")

        self.verticalLayout_4.addWidget(self.label_4)

        self.input_home_number = QLineEdit(self.frame)
        self.input_home_number.setObjectName(u"input_home_number")
        sizePolicy1.setHeightForWidth(self.input_home_number.sizePolicy().hasHeightForWidth())
        self.input_home_number.setSizePolicy(sizePolicy1)
        self.input_home_number.setMinimumSize(QSize(0, 30))
        self.input_home_number.setFont(font)
        self.input_home_number.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"}")

        self.verticalLayout_4.addWidget(self.input_home_number)


        self.verticalLayout_18.addLayout(self.verticalLayout_4)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: black;")

        self.verticalLayout_12.addWidget(self.label_12)

        self.input_more_info = QPlainTextEdit(self.frame)
        self.input_more_info.setObjectName(u"input_more_info")
        self.input_more_info.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_12.addWidget(self.input_more_info)


        self.verticalLayout_18.addLayout(self.verticalLayout_12)


        self.verticalLayout_14.addWidget(self.frame)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.tab_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: white;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(224, 244, 200);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: black;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.input_work_phone = QLineEdit(self.frame_2)
        self.input_work_phone.setObjectName(u"input_work_phone")
        sizePolicy1.setHeightForWidth(self.input_work_phone.sizePolicy().hasHeightForWidth())
        self.input_work_phone.setSizePolicy(sizePolicy1)
        self.input_work_phone.setMinimumSize(QSize(0, 30))
        self.input_work_phone.setFont(font)
        self.input_work_phone.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"}")

        self.verticalLayout_3.addWidget(self.input_work_phone)


        self.verticalLayout_15.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: black;")

        self.verticalLayout_2.addWidget(self.label_2)

        self.input_work_email = QLineEdit(self.frame_2)
        self.input_work_email.setObjectName(u"input_work_email")
        sizePolicy1.setHeightForWidth(self.input_work_email.sizePolicy().hasHeightForWidth())
        self.input_work_email.setSizePolicy(sizePolicy1)
        self.input_work_email.setMinimumSize(QSize(0, 30))
        self.input_work_email.setFont(font)
        self.input_work_email.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.input_work_email)


        self.verticalLayout_15.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(224, 244, 200);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: black;")

        self.verticalLayout_13.addWidget(self.label_13)

        self.optional_job_titles = QComboBox(self.frame_3)
        self.optional_job_titles.setObjectName(u"optional_job_titles")
        sizePolicy1.setHeightForWidth(self.optional_job_titles.sizePolicy().hasHeightForWidth())
        self.optional_job_titles.setSizePolicy(sizePolicy1)
        self.optional_job_titles.setMinimumSize(QSize(0, 30))
        self.optional_job_titles.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_13.addWidget(self.optional_job_titles)


        self.horizontalLayout.addLayout(self.verticalLayout_13)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: black;")

        self.verticalLayout_11.addWidget(self.label_11)

        self.optional_cabinets = QComboBox(self.frame_3)
        self.optional_cabinets.setObjectName(u"optional_cabinets")
        sizePolicy1.setHeightForWidth(self.optional_cabinets.sizePolicy().hasHeightForWidth())
        self.optional_cabinets.setSizePolicy(sizePolicy1)
        self.optional_cabinets.setMinimumSize(QSize(0, 30))
        self.optional_cabinets.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_11.addWidget(self.optional_cabinets)


        self.horizontalLayout.addLayout(self.verticalLayout_11)


        self.verticalLayout_16.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: black;")

        self.verticalLayout_9.addWidget(self.label_9)

        self.optional_boss = QComboBox(self.frame_3)
        self.optional_boss.setObjectName(u"optional_boss")
        sizePolicy1.setHeightForWidth(self.optional_boss.sizePolicy().hasHeightForWidth())
        self.optional_boss.setSizePolicy(sizePolicy1)
        self.optional_boss.setMinimumSize(QSize(0, 30))
        self.optional_boss.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_9.addWidget(self.optional_boss)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: black;")

        self.verticalLayout_10.addWidget(self.label_10)

        self.optional_helpers = QComboBox(self.frame_3)
        self.optional_helpers.setObjectName(u"optional_helpers")
        sizePolicy1.setHeightForWidth(self.optional_helpers.sizePolicy().hasHeightForWidth())
        self.optional_helpers.setSizePolicy(sizePolicy1)
        self.optional_helpers.setMinimumSize(QSize(0, 30))
        self.optional_helpers.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_10.addWidget(self.optional_helpers)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)


        self.verticalLayout_16.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_17.addLayout(self.horizontalLayout_3)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setStyleSheet(u"background-color: rgb(224, 244, 200);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setStyleSheet(u"color: black;")

        self.verticalLayout_7.addWidget(self.label_7)

        self.optional_sub_divisions = QComboBox(self.frame_4)
        self.optional_sub_divisions.setObjectName(u"optional_sub_divisions")
        sizePolicy1.setHeightForWidth(self.optional_sub_divisions.sizePolicy().hasHeightForWidth())
        self.optional_sub_divisions.setSizePolicy(sizePolicy1)
        self.optional_sub_divisions.setMinimumSize(QSize(0, 30))
        self.optional_sub_divisions.setMaximumSize(QSize(16777215, 30))
        self.optional_sub_divisions.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_7.addWidget(self.optional_sub_divisions)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setStyleSheet(u"color: black;")

        self.verticalLayout_6.addWidget(self.label_6)

        self.optional_organizations = QComboBox(self.frame_4)
        self.optional_organizations.setObjectName(u"optional_organizations")
        sizePolicy1.setHeightForWidth(self.optional_organizations.sizePolicy().hasHeightForWidth())
        self.optional_organizations.setSizePolicy(sizePolicy1)
        self.optional_organizations.setMinimumSize(QSize(0, 30))
        self.optional_organizations.setMaximumSize(QSize(16777215, 30))
        self.optional_organizations.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_6.addWidget(self.optional_organizations)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setStyleSheet(u"color: black;")

        self.verticalLayout_8.addWidget(self.label_8)

        self.optional_department = QComboBox(self.frame_4)
        self.optional_department.setObjectName(u"optional_department")
        sizePolicy1.setHeightForWidth(self.optional_department.sizePolicy().hasHeightForWidth())
        self.optional_department.setSizePolicy(sizePolicy1)
        self.optional_department.setMinimumSize(QSize(0, 30))
        self.optional_department.setMaximumSize(QSize(16777215, 30))
        self.optional_department.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_8.addWidget(self.optional_department)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)


        self.verticalLayout_17.addWidget(self.frame_4)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_19.addWidget(self.tabWidget)

        self.btn_save = QPushButton(Dialog)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 35))
        self.btn_save.setStyleSheet(u"background-color: green;\n"
"")

        self.verticalLayout_19.addWidget(self.btn_save)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0424\u0418\u041e:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"\u041b\u0438\u0447\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u043f\u043e\u0447\u0442\u0430:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0431\u0438\u043d\u0435\u0442:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043c\u043e\u0449\u043d\u0438\u043a:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u0435\u043b:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

