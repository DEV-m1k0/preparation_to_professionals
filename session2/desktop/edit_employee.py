# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_employee.ui'
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
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(800, 600))
        Dialog.setMaximumSize(QSize(800, 600))
        Dialog.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"background-color: white;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 363, 928))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: black;")

        self.verticalLayout_2.addWidget(self.label_2)

        self.input_full_name_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.input_full_name_2.setObjectName(u"input_full_name_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_full_name_2.sizePolicy().hasHeightForWidth())
        self.input_full_name_2.setSizePolicy(sizePolicy1)
        self.input_full_name_2.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setKerning(True)
        self.input_full_name_2.setFont(font)
        self.input_full_name_2.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_2.addWidget(self.input_full_name_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: black;")

        self.verticalLayout_6.addWidget(self.label_6)

        self.input_date_of_birth_2 = QDateEdit(self.scrollAreaWidgetContents)
        self.input_date_of_birth_2.setObjectName(u"input_date_of_birth_2")
        sizePolicy1.setHeightForWidth(self.input_date_of_birth_2.sizePolicy().hasHeightForWidth())
        self.input_date_of_birth_2.setSizePolicy(sizePolicy1)
        self.input_date_of_birth_2.setMinimumSize(QSize(0, 30))
        self.input_date_of_birth_2.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_6.addWidget(self.input_date_of_birth_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: black;")

        self.verticalLayout_7.addWidget(self.label_7)

        self.input_home_number_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.input_home_number_2.setObjectName(u"input_home_number_2")
        sizePolicy1.setHeightForWidth(self.input_home_number_2.sizePolicy().hasHeightForWidth())
        self.input_home_number_2.setSizePolicy(sizePolicy1)
        self.input_home_number_2.setMinimumSize(QSize(0, 30))
        self.input_home_number_2.setFont(font)
        self.input_home_number_2.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_7.addWidget(self.input_home_number_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: black;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.input_work_phone = QLineEdit(self.scrollAreaWidgetContents)
        self.input_work_phone.setObjectName(u"input_work_phone")
        sizePolicy1.setHeightForWidth(self.input_work_phone.sizePolicy().hasHeightForWidth())
        self.input_work_phone.setSizePolicy(sizePolicy1)
        self.input_work_phone.setMinimumSize(QSize(0, 30))
        self.input_work_phone.setFont(font)
        self.input_work_phone.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_3.addWidget(self.input_work_phone)


        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: black;")

        self.verticalLayout_8.addWidget(self.label_8)

        self.input_work_email = QLineEdit(self.scrollAreaWidgetContents)
        self.input_work_email.setObjectName(u"input_work_email")
        sizePolicy1.setHeightForWidth(self.input_work_email.sizePolicy().hasHeightForWidth())
        self.input_work_email.setSizePolicy(sizePolicy1)
        self.input_work_email.setMinimumSize(QSize(0, 30))
        self.input_work_email.setFont(font)
        self.input_work_email.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"	color: black;\n"
"	border: 1px solid black;\n"
"}")

        self.verticalLayout_8.addWidget(self.input_work_email)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: black;")

        self.verticalLayout_13.addWidget(self.label_13)

        self.optional_job_titles = QComboBox(self.scrollAreaWidgetContents)
        self.optional_job_titles.setObjectName(u"optional_job_titles")
        sizePolicy1.setHeightForWidth(self.optional_job_titles.sizePolicy().hasHeightForWidth())
        self.optional_job_titles.setSizePolicy(sizePolicy1)
        self.optional_job_titles.setMinimumSize(QSize(0, 30))
        self.optional_job_titles.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_13.addWidget(self.optional_job_titles)


        self.verticalLayout_9.addLayout(self.verticalLayout_13)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: black;")

        self.verticalLayout_11.addWidget(self.label_11)

        self.optional_cabinets = QComboBox(self.scrollAreaWidgetContents)
        self.optional_cabinets.setObjectName(u"optional_cabinets")
        sizePolicy1.setHeightForWidth(self.optional_cabinets.sizePolicy().hasHeightForWidth())
        self.optional_cabinets.setSizePolicy(sizePolicy1)
        self.optional_cabinets.setMinimumSize(QSize(0, 30))
        self.optional_cabinets.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_11.addWidget(self.optional_cabinets)


        self.verticalLayout_9.addLayout(self.verticalLayout_11)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: black;")

        self.verticalLayout_14.addWidget(self.label_9)

        self.optional_boss = QComboBox(self.scrollAreaWidgetContents)
        self.optional_boss.setObjectName(u"optional_boss")
        sizePolicy1.setHeightForWidth(self.optional_boss.sizePolicy().hasHeightForWidth())
        self.optional_boss.setSizePolicy(sizePolicy1)
        self.optional_boss.setMinimumSize(QSize(0, 30))
        self.optional_boss.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_14.addWidget(self.optional_boss)


        self.verticalLayout_9.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: black;")

        self.verticalLayout_15.addWidget(self.label_14)

        self.optional_helpers_2 = QComboBox(self.scrollAreaWidgetContents)
        self.optional_helpers_2.setObjectName(u"optional_helpers_2")
        sizePolicy1.setHeightForWidth(self.optional_helpers_2.sizePolicy().hasHeightForWidth())
        self.optional_helpers_2.setSizePolicy(sizePolicy1)
        self.optional_helpers_2.setMinimumSize(QSize(0, 30))
        self.optional_helpers_2.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_15.addWidget(self.optional_helpers_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setStyleSheet(u"color: black;")

        self.verticalLayout_16.addWidget(self.label_15)

        self.optional_organizations = QComboBox(self.scrollAreaWidgetContents)
        self.optional_organizations.setObjectName(u"optional_organizations")
        sizePolicy1.setHeightForWidth(self.optional_organizations.sizePolicy().hasHeightForWidth())
        self.optional_organizations.setSizePolicy(sizePolicy1)
        self.optional_organizations.setMinimumSize(QSize(0, 30))
        self.optional_organizations.setMaximumSize(QSize(16777215, 30))
        self.optional_organizations.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_16.addWidget(self.optional_organizations)


        self.verticalLayout_9.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMaximumSize(QSize(16777215, 20))
        self.label_16.setStyleSheet(u"color: black;")

        self.verticalLayout_17.addWidget(self.label_16)

        self.optional_sub_divisions = QComboBox(self.scrollAreaWidgetContents)
        self.optional_sub_divisions.setObjectName(u"optional_sub_divisions")
        sizePolicy1.setHeightForWidth(self.optional_sub_divisions.sizePolicy().hasHeightForWidth())
        self.optional_sub_divisions.setSizePolicy(sizePolicy1)
        self.optional_sub_divisions.setMinimumSize(QSize(0, 30))
        self.optional_sub_divisions.setMaximumSize(QSize(16777215, 30))
        self.optional_sub_divisions.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_17.addWidget(self.optional_sub_divisions)


        self.verticalLayout_9.addLayout(self.verticalLayout_17)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setStyleSheet(u"color: black;")

        self.verticalLayout_10.addWidget(self.label_10)

        self.optional_department = QComboBox(self.scrollAreaWidgetContents)
        self.optional_department.setObjectName(u"optional_department")
        sizePolicy1.setHeightForWidth(self.optional_department.sizePolicy().hasHeightForWidth())
        self.optional_department.setSizePolicy(sizePolicy1)
        self.optional_department.setMinimumSize(QSize(0, 30))
        self.optional_department.setMaximumSize(QSize(16777215, 30))
        self.optional_department.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_10.addWidget(self.optional_department)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: black;")

        self.verticalLayout_12.addWidget(self.label_12)

        self.input_more_info = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.input_more_info.setObjectName(u"input_more_info")
        self.input_more_info.setStyleSheet(u"	background-color: white;\n"
"	color: black;")

        self.verticalLayout_12.addWidget(self.input_more_info)


        self.verticalLayout_9.addLayout(self.verticalLayout_12)

        self.btn_save = QPushButton(self.scrollAreaWidgetContents)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 35))
        self.btn_save.setStyleSheet(u"background-color: green;\n"
"")

        self.verticalLayout_9.addWidget(self.btn_save)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"background-color: white;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollArea_2 = QScrollArea(self.frame_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 353, 500))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.combobox_filtration_by_table = QComboBox(self.scrollAreaWidgetContents_3)
        self.combobox_filtration_by_table.addItem("")
        self.combobox_filtration_by_table.addItem("")
        self.combobox_filtration_by_table.addItem("")
        self.combobox_filtration_by_table.addItem("")
        self.combobox_filtration_by_table.setObjectName(u"combobox_filtration_by_table")
        self.combobox_filtration_by_table.setStyleSheet(u"color: black;")

        self.horizontalLayout_2.addWidget(self.combobox_filtration_by_table)


        self.verticalLayout_20.addLayout(self.horizontalLayout_2)

        self.frame_study_date = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_study_date.setObjectName(u"frame_study_date")
        self.frame_study_date.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_study_date.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_study_date)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_study_date)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: black;")

        self.horizontalLayout_4.addWidget(self.label)

        self.combobox_filtration_by_period_for_study = QComboBox(self.frame_study_date)
        self.combobox_filtration_by_period_for_study.addItem("")
        self.combobox_filtration_by_period_for_study.addItem("")
        self.combobox_filtration_by_period_for_study.addItem("")
        self.combobox_filtration_by_period_for_study.addItem("")
        self.combobox_filtration_by_period_for_study.setObjectName(u"combobox_filtration_by_period_for_study")
        self.combobox_filtration_by_period_for_study.setStyleSheet(u"color: black;")

        self.horizontalLayout_4.addWidget(self.combobox_filtration_by_period_for_study)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tableWidget = QTableWidget(self.frame_study_date)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"color: black;")
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout_5.addWidget(self.tableWidget)


        self.verticalLayout_20.addWidget(self.frame_study_date)

        self.frame_skips_date = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_skips_date.setObjectName(u"frame_skips_date")
        self.frame_skips_date.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_skips_date.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_skips_date)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame_skips_date)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: black;")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.combobox_filtration_by_period_for_skips = QComboBox(self.frame_skips_date)
        self.combobox_filtration_by_period_for_skips.addItem("")
        self.combobox_filtration_by_period_for_skips.addItem("")
        self.combobox_filtration_by_period_for_skips.addItem("")
        self.combobox_filtration_by_period_for_skips.setObjectName(u"combobox_filtration_by_period_for_skips")
        self.combobox_filtration_by_period_for_skips.setStyleSheet(u"color: black;")

        self.horizontalLayout_5.addWidget(self.combobox_filtration_by_period_for_skips)


        self.verticalLayout_18.addLayout(self.horizontalLayout_5)

        self.tableWidget_2 = QTableWidget(self.frame_skips_date)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"color: black;")
        self.tableWidget_2.setSortingEnabled(True)

        self.verticalLayout_18.addWidget(self.tableWidget_2)


        self.verticalLayout_20.addWidget(self.frame_skips_date)

        self.frame_vacation_date = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_vacation_date.setObjectName(u"frame_vacation_date")
        self.frame_vacation_date.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_vacation_date.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_vacation_date)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.frame_vacation_date)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: black;")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.combobox_filtration_by_period_for_vacation = QComboBox(self.frame_vacation_date)
        self.combobox_filtration_by_period_for_vacation.addItem("")
        self.combobox_filtration_by_period_for_vacation.addItem("")
        self.combobox_filtration_by_period_for_vacation.addItem("")
        self.combobox_filtration_by_period_for_vacation.addItem("")
        self.combobox_filtration_by_period_for_vacation.setObjectName(u"combobox_filtration_by_period_for_vacation")
        self.combobox_filtration_by_period_for_vacation.setStyleSheet(u"color: black;")

        self.horizontalLayout_6.addWidget(self.combobox_filtration_by_period_for_vacation)


        self.verticalLayout_19.addLayout(self.horizontalLayout_6)

        self.tableWidget_3 = QTableWidget(self.frame_vacation_date)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"color: black;")
        self.tableWidget_3.setSortingEnabled(True)

        self.verticalLayout_19.addWidget(self.tableWidget_3)


        self.verticalLayout_20.addWidget(self.frame_vacation_date)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_3.addWidget(self.scrollArea_2)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: red;\n"
"")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0424\u0418\u041e:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u043f\u043e\u0447\u0442\u0430:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0431\u0438\u043d\u0435\u0442:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043c\u043e\u0449\u043d\u0438\u043a:", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0434\u0435\u043b:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f:", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.combobox_filtration_by_table.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435", None))
        self.combobox_filtration_by_table.setItemText(1, QCoreApplication.translate("Dialog", u"\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435", None))
        self.combobox_filtration_by_table.setItemText(2, QCoreApplication.translate("Dialog", u"\u041e\u0442\u043f\u0443\u0441\u043a\u0438", None))
        self.combobox_filtration_by_table.setItemText(3, QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u043f\u0443\u0441\u043a\u0438", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435", None))
        self.combobox_filtration_by_period_for_study.setItemText(0, QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.combobox_filtration_by_period_for_study.setItemText(1, QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0448\u0435\u0434\u0448\u0438\u0435", None))
        self.combobox_filtration_by_period_for_study.setItemText(2, QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435", None))
        self.combobox_filtration_by_period_for_study.setItemText(3, QCoreApplication.translate("Dialog", u"\u0411\u0443\u0434\u0443\u0449\u0438\u0435", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u043b\u043e", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043d\u0435\u0446", None));
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u043f\u0443\u0441\u043a\u0438", None))
        self.combobox_filtration_by_period_for_skips.setItemText(0, QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.combobox_filtration_by_period_for_skips.setItemText(1, QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0448\u0435\u0434\u0448\u0438\u0435", None))
        self.combobox_filtration_by_period_for_skips.setItemText(2, QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435", None))

        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u043b\u043e", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043d\u0435\u0446", None));
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043f\u0443\u0441\u043a\u0438", None))
        self.combobox_filtration_by_period_for_vacation.setItemText(0, QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.combobox_filtration_by_period_for_vacation.setItemText(1, QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0448\u0435\u0434\u0448\u0438\u0435", None))
        self.combobox_filtration_by_period_for_vacation.setItemText(2, QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0435", None))
        self.combobox_filtration_by_period_for_vacation.setItemText(3, QCoreApplication.translate("Dialog", u"\u0411\u0443\u0434\u0443\u0449\u0438\u0435", None))

        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0447\u0430\u043b\u043e", None));
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043d\u0435\u0446", None));
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0423\u0432\u043e\u043b\u0438\u0442\u044c", None))
    # retranslateUi

