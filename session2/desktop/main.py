import asyncio, sys, requests, json
from datetime import date
import bcrypt
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform,
    QResizeEvent)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget, QTableWidgetItem, QFileDialog,
    QMessageBox, QTreeWidgetItem, QFrame, QDialog)
from main_window import Ui_MainWindow
from api import *
from dialogs import EditEmployeeDialog, AddEmployeeDialog

"""
Главный файл для запуска настолького приложения
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.employees = get_employees()
        self.cabinets = get_cabinets()
        self.job_titles = get_job_titles()
        self.organizations = [str(org['title']) for org in get_organizations()]
        self.sub_divisions = [str(sub_d['title']) for sub_d in get_subdivisions()]
        self.sub_sub_divisions = [str(sub_sub_d['title']) for sub_sub_d in get_sub_sub_divisions()]

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_tree_widget()

        self.ui.treeWidget_departments.itemClicked.connect(self.item_selected)
        self.ui.employee_add_button.clicked.connect(self.add_employee)
        self.ui.listWidget.itemClicked.connect(self.employee_selected)

        self.selected_department = ""


    def employee_selected(self, item: QListWidgetItem):
        dialog = EditEmployeeDialog(name=item.text(), cabinets=self.cabinets, job_titles=self.job_titles,
                                    organizations=self.organizations, sub_divisions=self.sub_divisions,
                                    sub_sub_divisions=self.sub_sub_divisions, employees=self.employees,
                                    selected_department=self.selected_department)
        dialog.exec()


    def add_employee(self):
        dialog = AddEmployeeDialog(self.employees, self.cabinets,
                              self.job_titles, self.organizations,
                              self.sub_divisions, self.sub_sub_divisions)
        dialog.exec()


    def item_selected(self, item: QTreeWidgetItem, column: int = 0):
        try:
            text = item.text(column).strip()
        except:
            text = item.strip()
        self.selected_department = text
        self.ui.listWidget.clear()
        users = get_employees_by_department(text)
        for user in users:
            item =  QListWidgetItem(f"{user['birthday']}\n{user['username']}\n{user['email']}")
            if user['date_of_dismissal']:
                item.setBackground(QColor('red'))
                self.ui.listWidget.addItem(item)
            else:
                item.setBackground(QColor('#e0f4c8'))
                self.ui.listWidget.addItem(item)



    def setup_tree_widget(self):
        tree_widget = self.ui.treeWidget_departments
        tree_widget.setColumnCount(1)


        organizations = get_organizations()
        for organization in organizations:
            top_lvl = QTreeWidgetItem([organization['title']])
            for subdivision_id in organization["subdivisions"]:
                subdivision = get_subdivision_by_id(subdivision_id)
                bottom_lvl = QTreeWidgetItem([subdivision["title"]])
                top_lvl.addChild(bottom_lvl)
                for sub_sub_division_id in subdivision["sub_sub_division"]:
                    sub_sub_division = get_sub_sub_division_by_id(sub_sub_division_id)
                    if sub_sub_division:
                        next_bottom_lvl = QTreeWidgetItem([sub_sub_division['title']])
                        bottom_lvl.addChild(next_bottom_lvl)
            tree_widget.addTopLevelItem(top_lvl)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
