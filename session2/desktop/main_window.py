# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 0))
        MainWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"padding: 0px;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"background-color: #e0f4c8;\n"
"max-height: 100px;\n"
"border: none;")
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.header)
        self.logo.setObjectName(u"logo")
        self.logo.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.logo.setStyleSheet(u"min-width: 80px;\n"
"min-height: 80px;\n"
"max-width: 80px;\n"
"max-height: 80px;\n"
"border-radius: 40%;\n"
"background-color: #78b34b;\n"
"color: black;\n"
"margin-left: 10%;")
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.logo)

        self.page_name = QLabel(self.header)
        self.page_name.setObjectName(u"page_name")
        self.page_name.setStyleSheet(u"max-height: 50px;\n"
"margin-left: 20%;\n"
"margin-right: 40%;\n"
"padding-left: 15%;\n"
"min-width: 200px;\n"
"background-color: white;\n"
"color: black;\n"
"border-radius: 10%;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.page_name)


        self.verticalLayout.addWidget(self.header)

        self.frame_body = QFrame(self.centralwidget)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setStyleSheet(u"padding: 40%;")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_body)
#ifndef Q_OS_MAC
        self.horizontalLayout_2.setSpacing(-1)
#endif
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.treeWidget_departments = QTreeWidget(self.frame_body)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_departments.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_departments.setObjectName(u"treeWidget_departments")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget_departments.sizePolicy().hasHeightForWidth())
        self.treeWidget_departments.setSizePolicy(sizePolicy)
        self.treeWidget_departments.setMinimumSize(QSize(400, 0))
        font = QFont()
        font.setPointSize(16)
        self.treeWidget_departments.setFont(font)
        self.treeWidget_departments.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.treeWidget_departments.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.treeWidget_departments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.treeWidget_departments.setAutoFillBackground(False)
        self.treeWidget_departments.setStyleSheet(u"QTreeView{\n"
"	padding: 0px;\n"
"	background-color: rgb(217, 217, 217);\n"
"	border: 0px;\n"
"}\n"
"QAbstractItemView{\n"
"	padding: 0px;\n"
"}\n"
"QTreeWidget::item{\n"
"	background-color: rgb(224, 244, 200);\n"
"	color: black;\n"
"	min-height: 40px;\n"
"}\n"
"QTreeWidget::item:selected{\n"
"	background-color: rgb(120, 179, 75);\n"
"	color: white;\n"
"}\n"
"")
        self.treeWidget_departments.setLineWidth(0)
        self.treeWidget_departments.setAlternatingRowColors(False)
        self.treeWidget_departments.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.treeWidget_departments.setIndentation(20)
        self.treeWidget_departments.setRootIsDecorated(True)
        self.treeWidget_departments.setUniformRowHeights(False)
        self.treeWidget_departments.setSortingEnabled(False)
        self.treeWidget_departments.setAnimated(True)
        self.treeWidget_departments.setWordWrap(False)
        self.treeWidget_departments.setHeaderHidden(True)
        self.treeWidget_departments.header().setVisible(False)
        self.treeWidget_departments.header().setCascadingSectionResizes(False)

        self.horizontalLayout_2.addWidget(self.treeWidget_departments)

        self.frame_employees = QFrame(self.frame_body)
        self.frame_employees.setObjectName(u"frame_employees")
        self.frame_employees.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_employees.setStyleSheet(u"background-color: #d9d9d9;\n"
"padding: 0;\n"
"border: none;")
        self.frame_employees.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_employees.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_employees)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.frame_employees)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	padding: 10px;\n"
"}\n"
"QListWidget::item{\n"
"	padding: 10 0 10 10;\n"
"	margin-bottom: 5px;\n"
"	color: black;\n"
"	background-color: rgb(224, 244, 200);\n"
"	border-radius: 10px;\n"
"}")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.widget_employee_add = QWidget(self.frame_employees)
        self.widget_employee_add.setObjectName(u"widget_employee_add")
        self.widget_employee_add.setMinimumSize(QSize(0, 75))
        self.widget_employee_add.setMaximumSize(QSize(16777215, 75))
        self.widget_employee_add.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.widget_employee_add.setStyleSheet(u"border: 0px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_employee_add)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.employee_add_button = QPushButton(self.widget_employee_add)
        self.employee_add_button.setObjectName(u"employee_add_button")
        self.employee_add_button.setMinimumSize(QSize(50, 50))
        self.employee_add_button.setMaximumSize(QSize(50, 50))
        self.employee_add_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.employee_add_button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.employee_add_button.setAutoFillBackground(False)
        self.employee_add_button.setStyleSheet(u"background-color: rgb(224, 244, 200);\n"
"color: black;\n"
"font-size: 20px;")

        self.verticalLayout_3.addWidget(self.employee_add_button)


        self.verticalLayout_2.addWidget(self.widget_employee_add)


        self.horizontalLayout_2.addWidget(self.frame_employees)


        self.verticalLayout.addWidget(self.frame_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"\u043b\u043e\u0433\u043e\u0442\u0438\u043f", None))
        self.page_name.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u043e\u043d\u043d\u0430\u044f \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430", None))
        self.employee_add_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

