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
    QVBoxLayout, QWidget, QTableWidgetItem, QAbstractItemView,
    QMessageBox)
from api import *
import bcrypt
from datetime import date, datetime, timezone
import add_employee_dialog, edit_employee, re, add_skip, add_event, logging


"""
Диалоговые окна для настольного приложения
"""

class AddNewEvent(QDialog):
    def __init__(self, prev_obj, employee_name: str):
        super().__init__()

        self.ui = add_event.Ui_Dialog()
        self.ui.setupUi(self)

        self.employee_name = employee_name
        self.prev_obj = prev_obj

        self.ui.pushButton_add.clicked.connect(self.save)

    def save(self):
        title = self.ui.lineEdit_title.text()
        date_start = self.ui.dateTimeEdit_since.text()
        date_end = self.ui.dateTimeEdit_until.text()

        if add_event_by_employee(title, self.employee_name, date_start, date_end):
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Сохранение отпуска")
            msg_box.setText("Отпуск сохранен")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            self.close()

            self.prev_obj.setup()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка сохранения")
            msg_box.setText("Произошла ошибка при сохранении пропуска")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()



class AddNewVacation(QDialog):
    def __init__(self, prev_obj, employee_name: str):
        super().__init__()

        self.ui = add_skip.Ui_Dialog()
        self.ui.setupUi(self)

        self.employee_name = employee_name
        self.prev_obj = prev_obj

        self.ui.pushButton_add.clicked.connect(self.save)


    def save(self):
        date_start = self.ui.dateEdit_since.text()
        date_end = self.ui.dateEdit_before.text()

        if add_vacation_by_employee(self.employee_name, date_start, date_end):
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Сохранение отпуска")
            msg_box.setText("Отпуск сохранен")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            self.close()

            self.prev_obj.setup()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка сохранения")
            msg_box.setText("Произошла ошибка при сохранении пропуска")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()  

class AddNewSkip(QDialog):
    def __init__(self, prev_obj, employee_name: str):
        super().__init__()

        self.ui = add_skip.Ui_Dialog()
        self.ui.setupUi(self)

        self.employee_name = employee_name
        self.prev_obj = prev_obj

        self.ui.pushButton_add.clicked.connect(self.save)


    def save(self):
        date_start = self.ui.dateEdit_since.text()
        date_end = self.ui.dateEdit_before.text()

        if add_skip_by_employee(self.employee_name, date_start, date_end):
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Сохранение пропуска")
            msg_box.setText("Пропуск сохранен")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()
            self.close()

            self.prev_obj.setup()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Ошибка сохранения")
            msg_box.setText("Произошла ошибка при сохранении пропуска")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg_box.exec()        




class EditEmployeeDialog(QDialog):
    def __init__(self, name, employees, cabinets, job_titles,
                 organizations, sub_divisions, sub_sub_divisions,
                 selected_department):
        super().__init__()

        self.name = name
        self.employees = employees
        self.cabinets = cabinets
        self.boss = employees
        self.helpers = employees
        self.job_titles = job_titles
        self.organizations = organizations
        self.sub_divisions = sub_divisions
        self.sub_sub_divisions = sub_sub_divisions
        self.selected_department = selected_department

        self.ui = edit_employee.Ui_Dialog()
        self.ui.setupUi(self)

        self.setup()

        self.ui.btn_save.clicked.connect(self.save)
        self.ui.pushButton.clicked.connect(self.dismiss_employee)
        self.ui.combobox_filtration_by_table.currentTextChanged.connect(self.filtration_by_table)
        self.ui.combobox_filtration_by_period_for_study.currentTextChanged.connect(self.filtration_for_study)
        self.ui.combobox_filtration_by_period_for_skips.currentTextChanged.connect(self.filtration_for_skips)
        self.ui.combobox_filtration_by_period_for_vacation.currentTextChanged.connect(self.filtration_for_vacation)
        self.ui.btn_edit.clicked.connect(self.set_enable_inputs)
        self.ui.tableWidget_skips.itemClicked.connect(self.ask_del_for_skips)
        self.ui.tableWidget_vacations.itemClicked.connect(self.ask_del_for_vacations)
        self.ui.tableWidget_education.itemClicked.connect(self.ask_del_for_education)
        self.ui.pushButton_add_skips.clicked.connect(self.add_skip)
        self.ui.pushButton_add_vacation.clicked.connect(self.add_vacation)
        self.ui.pushButton_add_education.clicked.connect(self.add_education)

    def add_education(self, item: QTableWidgetItem):
        add_new_education = AddNewEvent(self, self.name)
        add_new_education.exec()

    def ask_del_for_education(self, item: QTableWidgetItem):
        text_date = item.text()
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Удаление обучения")
        msg_box.setText(f"Вы уверены, что хотите удалить обучение с датой: {text_date}?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg_box.exec()

        if result == QMessageBox.Yes:
            if item.column() == 0:
                if delete_employee_education_by_name_and_date(self.name, text_date):
                    self.setup()
        else:
            print(f"Отмена удаления отпуска с датой: {text_date}")

    def ask_del_for_vacations(self, item: QTableWidgetItem):
        text_date = item.text()
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Удаление отпуска")
        msg_box.setText(f"Вы уверены, что хотите удалить отпуск с датой: {text_date}?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg_box.exec()

        if result == QMessageBox.Yes:
            if item.column() == 0:
                if delete_employee_vacation_by_name_and_date(self.name, text_date):
                    self.setup()
        else:
            print(f"Отмена удаления отпуска с датой: {text_date}")

    def add_skip(self):
        add_new_skip = AddNewSkip(self, self.name)
        add_new_skip.exec()

    def add_vacation(self):
        add_new_vacation = AddNewVacation(self, self.name)
        add_new_vacation.exec()

    def ask_del_for_skips(self, item: QTableWidgetItem):
        text_date = item.text()
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Удаление пропуска")
        msg_box.setText(f"Вы уверены, что хотите удалить пропуск с датой: {text_date}?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg_box.exec()

        if result == QMessageBox.Yes:
            if item.column() == 0:
                if delete_employee_skip_by_name_and_date(self.name, text_date):
                    self.setup()
        else:
            print(f"Отмена удаления пропуска с датой: {text_date}")

    def set_enable_inputs(self):
        self.ui.input_date_of_birth_2.setEnabled(True)
        self.ui.input_full_name_2.setEnabled(True)
        self.ui.input_home_number_2.setEnabled(True)
        self.ui.input_work_email.setEnabled(True)
        self.ui.input_work_phone.setEnabled(True)
        self.ui.input_more_info.setEnabled(True)
        self.ui.optional_boss.setEnabled(True)
        self.ui.optional_department.setEnabled(True)
        self.ui.optional_cabinets.setEnabled(True)
        self.ui.optional_helpers_2.setEnabled(True)
        self.ui.optional_job_titles.setEnabled(True)
        self.ui.optional_organizations.setEnabled(True)
        self.ui.optional_sub_divisions.setEnabled(True)


    def dismiss_employee(self):
        accept = dismiss_employee_by_name(self.name)
        if not accept:
            QMessageBox.warning(self, "Ошибка",
                                "Не удалось уволить сотрудника. Скорее всего, у него есть незаконченные мероприятия",
                                QMessageBox.StandardButton.Ok)
        else: 
            self.close()

    def formatting_date(self, my_date: str):
        changed_format = date.fromisoformat(my_date).strftime("%d.%m.%Y")
        return changed_format
    def formatting_datetime(self, date: str):
        changed_format = datetime.fromisoformat(date).strftime("%d.%m.%Y %H:%M:%S")
        return changed_format
    
    def proccessing_datetime(self, date: str):
            study_date, study_time = date.split("T")
            year, month, day = study_date.split("-")
            hour, minute, second = study_time[:-1].split(":")
            return datetime(int(year), int(month), int(day),
                            int(hour),int(minute), int(second))
    def proccessing_date(self, my_date: str):
            year, month, day = my_date.split("-")
            return date(int(year), int(month), int(day))
    

    def filtration_for_skips(self, filter_by: str):
        self.ui.tableWidget_skips.clearContents()
        self.ui.tableWidget_skips.setRowCount(0)
        now = date.today()
        if filter_by == "Прошедшие":
            count_rows = 0
            for i in range(len(self.skip_dates)):
                if self.skip_dates[i]["date_until"] is not None:
                    date_since = self.proccessing_date(str(self.skip_dates[i]["date_since"]))
                    date_until = self.proccessing_date(str(self.skip_dates[i]["date_until"]))
                    if date_until <= now:
                        count_rows += 1
                        self.ui.tableWidget_skips.setRowCount(count_rows)
                        q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y"))
                        q_item_date_until = QTableWidgetItem(date_until.strftime("%d.%m.%Y"))
                        self.ui.tableWidget_skips.setItem(count_rows-1, 0, q_item_date_since)
                        self.ui.tableWidget_skips.setItem(count_rows-1, 1, q_item_date_until)
        elif filter_by == "Текущие":
            count_rows = 0
            for i in range(len(self.skip_dates)):
                if self.skip_dates[i]["date_until"] is None:
                    date_since = self.proccessing_date(str(self.skip_dates[i]["date_since"]))
                    count_rows += 1
                    self.ui.tableWidget_skips.setRowCount(count_rows)
                    q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y"))
                    self.ui.tableWidget_skips.setItem(count_rows-1, 0, q_item_date_since)
        else:
            self.ui.tableWidget_skips.setRowCount(len(self.skip_dates))

            for i in range (len(self.skip_dates)):
                date_since = self.formatting_date(self.skip_dates[i]["date_since"])
                date_since_item = QTableWidgetItem(date_since)
                self.ui.tableWidget_skips.setItem(i, 0, date_since_item)
                if self.skip_dates[i]["date_until"] is not None:
                    date_until = self.formatting_date(self.skip_dates[i]["date_until"])
                    date_until_item = QTableWidgetItem(date_until)
                    self.ui.tableWidget_skips.setItem(i, 1, date_until_item)


    def filtration_for_study(self, filter_by: str):
        self.ui.tableWidget_education.clearContents()
        self.ui.tableWidget_education.setRowCount(0)
        now = datetime.now()
        if filter_by == "Прошедшие":
            count_rows = 0
            for i in range(len(self.study_dates)):
                date_since = self.proccessing_datetime(str(self.study_dates[i]["date_since"]))
                date_until = self.proccessing_datetime(str(self.study_dates[i]["date_until"]))
                if date_until < now:
                    count_rows += 1
                    self.ui.tableWidget_education.setRowCount(count_rows)
                    q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y %H:%M:%S"))
                    q_item_date_until = QTableWidgetItem(date_until.strftime("%d.%m.%Y %H:%M:%S"))
                    self.ui.tableWidget_education.setItem(count_rows-1, 0, q_item_date_since)
                    self.ui.tableWidget_education.setItem(count_rows-1, 1, q_item_date_until)
        elif filter_by == "Текущие":
            count_rows = 0
            for i in range(len(self.study_dates)):
                date_since = self.proccessing_datetime(str(self.study_dates[i]["date_since"]))
                date_until = self.proccessing_datetime(str(self.study_dates[i]["date_until"]))
                if date_since <= now <= date_until:
                    count_rows += 1
                    self.ui.tableWidget_education.setRowCount(count_rows)
                    q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y %H:%M:%S"))
                    q_item_date_until = QTableWidgetItem(date_until.strftime("%d.%m.%Y %H:%M:%S"))
                    self.ui.tableWidget_education.setItem(count_rows-1, 0, q_item_date_since)
                    self.ui.tableWidget_education.setItem(count_rows-1, 1, q_item_date_until)
        elif filter_by == "Будущие":
            count_rows = 0
            for i in range(len(self.study_dates)):
                date_since = self.proccessing_datetime(str(self.study_dates[i]["date_since"]))
                date_until = self.proccessing_datetime(str(self.study_dates[i]["date_until"]))
                if now < date_since:
                    count_rows += 1
                    self.ui.tableWidget_education.setRowCount(count_rows)
                    q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y %H:%M:%S"))
                    q_item_date_until = QTableWidgetItem(date_until.strftime("%d.%m.%Y %H:%M:%S"))
                    self.ui.tableWidget_education.setItem(count_rows-1, 0, q_item_date_since)
                    self.ui.tableWidget_education.setItem(count_rows-1, 1, q_item_date_until)
        else:
            self.ui.tableWidget_education.setRowCount(len(self.study_dates))

            for i in range (len(self.study_dates)):
        
                date_since = self.formatting_datetime(self.study_dates[i]["date_since"])
                date_since_item = QTableWidgetItem(date_since)
                self.ui.tableWidget_education.setItem(i, 0, date_since_item)
                date_until = self.formatting_datetime(self.study_dates[i]["date_until"])
                date_until_item = QTableWidgetItem(date_until)
                self.ui.tableWidget_education.setItem(i, 1, date_until_item)
    
    def filtration_for_vacation(self, filter_by: str):
        self.ui.tableWidget_vacations.clearContents()
        self.ui.tableWidget_vacations.setRowCount(0)
        now = date.today()
        if filter_by == "Прошедшие":
            count_rows = 0
            for i in range(len(self.vacation_dates)):
                date_since = self.proccessing_date(str(self.vacation_dates[i]["date_since"]))
                if self.vacation_dates[i]["date_until"] is not None:
                    date_until = self.proccessing_date(str(self.vacation_dates[i]["date_until"]))
                    if date_until < now:
                        count_rows += 1
                        self.ui.tableWidget_vacations.setRowCount(count_rows)
                        q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y"))
                        q_item_date_until = QTableWidgetItem(date_until.strftime("%d.%m.%Y"))
                        self.ui.tableWidget_vacations.setItem(count_rows-1, 0, q_item_date_since)
                        self.ui.tableWidget_vacations.setItem(count_rows-1, 1, q_item_date_until)
        elif filter_by == "Текущие":
            count_rows = 0
            for i in range(len(self.vacation_dates)):
                date_since = self.proccessing_date(str(self.vacation_dates[i]["date_since"]))
                if self.vacation_dates[i]["date_until"] is not None:
                    date_until = self.proccessing_date(str(self.vacation_dates[i]["date_until"]))
                    if date_since <= now <= date_until:
                        count_rows += 1
                        self.ui.tableWidget_vacations.setRowCount(count_rows)
                        q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y"))
                        q_item_date_until = QTableWidgetItem(date_until.strftime("%d.%m.%Y"))
                        self.ui.tableWidget_vacations.setItem(count_rows-1, 0, q_item_date_since)
                        self.ui.tableWidget_vacations.setItem(count_rows-1, 1, q_item_date_until)
                else:
                    count_rows += 1
                    self.ui.tableWidget_vacations.setRowCount(count_rows)
                    q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y"))
                    self.ui.tableWidget_vacations.setItem(count_rows-1, 0, q_item_date_since)
        elif filter_by == "Будущие":
            count_rows = 0
            for i in range(len(self.vacation_dates)):
                date_since = self.proccessing_date(str(self.vacation_dates[i]["date_since"]))
                if self.vacation_dates[i]["date_until"] is not None:
                    date_until = self.proccessing_date(str(self.vacation_dates[i]["date_until"]))
                    if now < date_since:
                        count_rows += 1
                        self.ui.tableWidget_vacations.setRowCount(count_rows)
                        q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y"))
                        q_item_date_until = QTableWidgetItem(date_until.strftime("%d.%m.%Y"))
                        self.ui.tableWidget_vacations.setItem(count_rows-1, 0, q_item_date_since)
                        self.ui.tableWidget_vacations.setItem(count_rows-1, 1, q_item_date_until)
                else:
                    count_rows += 1
                    self.ui.tableWidget_vacations.setRowCount(count_rows)
                    q_item_date_since = QTableWidgetItem(date_since.strftime("%d.%m.%Y"))
                    self.ui.tableWidget_vacations.setItem(count_rows-1, 0, q_item_date_since)
        else:
            self.ui.tableWidget_vacations.setRowCount(len(self.vacation_dates))

            for i in range (len(self.vacation_dates)):
                date_since = self.formatting_date(self.vacation_dates[i]["date_since"])
                date_since_item = QTableWidgetItem(date_since)
                self.ui.tableWidget_vacations.setItem(i, 0, date_since_item)
                date_until = self.formatting_date(self.vacation_dates[i]["date_until"])
                date_until_item = QTableWidgetItem(date_until)
                self.ui.tableWidget_vacations.setItem(i, 1, date_until_item)
                


    def filtration_by_table(self, filter_by: str):
        self.ui.frame_skips_date.setHidden(False)
        self.ui.frame_vacation_date.setHidden(False)
        self.ui.frame_study_date.setHidden(False)
        if filter_by == "Обучение":
            self.ui.frame_skips_date.setHidden(True)
            self.ui.frame_vacation_date.setHidden(True)
        if filter_by == "Отпуски":
            self.ui.frame_study_date.setHidden(True)
            self.ui.frame_skips_date.setHidden(True)
        if filter_by == "Пропуски":
            self.ui.frame_study_date.setHidden(True)
            self.ui.frame_vacation_date.setHidden(True)

    def setup(self):
        self.study_dates = get_study_date_by_employee_name(self.name)
        self.vacation_dates = get_vacations_by_employee_name(self.name)
        self.skip_dates = get_skip_dates_by_employee_name(self.name)

        self.ui.tableWidget_education.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableWidget_skips.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tableWidget_vacations.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_cabinets.addItems(self.cabinets)
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_job_titles.addItems(self.job_titles)
        self.ui.optional_helpers_2.addItems(self.employees)
        self.ui.optional_organizations.addItems(self.organizations)
        self.ui.optional_sub_divisions.addItems(self.sub_divisions)
        self.ui.optional_department.addItems(self.sub_sub_divisions)

        employee = get_employee_by_name(self.name)
        self.employee = employee

        try:
            self.ui.input_full_name_2.setText(employee['username'])
        except:
            pass
        try:
            birthday = employee['birthday'].split("-")
            q_time = QDate()
            q_time.setDate(int(birthday[0]), int(birthday[1]), int(birthday[2]))
            self.ui.input_date_of_birth_2.setDate(q_time)
        except:
            pass
        try:
            self.ui.input_home_number_2.setText(employee['personal_phone'])
        except:
            pass
        try:
            self.ui.input_work_email.setText(employee['email'])
        except:
            pass
        try:
            self.ui.input_work_phone.setText(employee['work_phone'])
        except:
            pass
        try:
            self.ui.input_more_info.setPlainText(employee['more_info'])
        except:
            pass
        
        try:
            print(self.study_dates["error"])
        except:
            self.ui.tableWidget_education.setRowCount(len(self.study_dates))
            for i in range (len(self.study_dates)):
                date_since = self.formatting_datetime(self.study_dates[i]["date_since"])
                date_since_item = QTableWidgetItem(date_since)
                self.ui.tableWidget_education.setItem(i, 0, date_since_item)
                date_until = self.formatting_datetime(self.study_dates[i]["date_until"])
                date_until_item = QTableWidgetItem(date_until)
                self.ui.tableWidget_education.setItem(i, 1, date_until_item)
        try:
            print(self.skip_dates["error"])
        except:
            self.ui.tableWidget_skips.setRowCount(len(self.skip_dates))
            for i in range(len(self.skip_dates)):
                date_since = self.formatting_date(self.skip_dates[i]["date_since"])
                date_since_item = QTableWidgetItem(date_since)
                self.ui.tableWidget_skips.setItem(i, 0, date_since_item)
                if self.skip_dates[i]["date_until"] is not None:
                    date_until = self.formatting_date(self.skip_dates[i]["date_until"])
                    date_until_item = QTableWidgetItem(date_until)
                    self.ui.tableWidget_skips.setItem(i, 1, date_until_item)
        
        try:
            print(self.vacation_dates["error"])
        except:
            self.ui.tableWidget_vacations.setRowCount(len(self.vacation_dates))
            for i in range (len(self.vacation_dates)):
                date_since = self.formatting_date(self.vacation_dates[i]["date_since"])
                date_since_item = QTableWidgetItem(date_since)
                self.ui.tableWidget_vacations.setItem(i, 0, date_since_item)
                if self.vacation_dates[i]["date_until"] is not None:
                    date_until = self.formatting_date(self.vacation_dates[i]["date_until"])
                    date_until_item = QTableWidgetItem(date_until)
                    self.ui.tableWidget_vacations.setItem(i, 1, date_until_item)
        

    def check_phone(self, phone):

        if len(phone) > 20:
            QMessageBox.warning(self, "Предупреждение", "В номере телефона не может быть больше 20 символов.",
                                QMessageBox.StandardButton.Ok)
            return False

        accepted_chars = "0123456789-()#+ "
        
        for char in phone:
            if char not in accepted_chars:
                QMessageBox.warning(self, "Предупреждение", "В номере телефона недопустимые символы.",
                                    QMessageBox.StandardButton.Ok)
                return False
        
        return True
    
    def check_email(self, email):
        pattern = r'^[^@]+@[^@]+\.[^@]+$'
        
        if not re.match(pattern, email):
            QMessageBox.warning(self, "Предупреждение", "Неверный формат email.", QMessageBox.StandardButton.Ok)
            return False
        
        return True

    def save(self):

        if not self.check_phone(self.ui.input_work_phone.text()):
            return False
    
        if not self.check_phone(self.ui.input_home_number_2.text()):
            return False
        
        if not self.check_email(self.ui.input_work_email.text()):
            return False

        full_name = self.ui.input_full_name_2.text()
        date_of_birth = self.ui.input_date_of_birth_2.text()
        more_info = self.ui.input_more_info.toPlainText()
        home_number = self.ui.input_home_number_2.text()
        work_number = self.ui.input_work_phone.text()
        work_email = self.ui.input_work_email.text()

        helper = self.ui.optional_helpers_2.currentText()
        helper_id = get_employee_id_by_name(helper)
        boss = self.ui.optional_boss.currentText()
        boss_id = get_employee_id_by_name(boss)
        job_title = self.ui.optional_job_titles.currentText()
        job_title_id = get_job_title_by_name(job_title)
        cabinet = self.ui.optional_cabinets.currentText()
        cabinet_id = get_cabinet_by_name(cabinet)
        organization = self.ui.optional_organizations.currentText()
        organization_id = get_organization_by_name(organization)
        sub_division = self.ui.optional_sub_divisions.currentText()
        sub_division_id = get_sub_division_by_name(sub_division)
        sub_sub_division = self.ui.optional_department.currentText()
        sub_sub_division_id = get_sub_sub_division_by_name(sub_sub_division)

        day, month, year = date_of_birth.split('.')
        password = bcrypt.hashpw(full_name.encode(), bcrypt.gensalt()).decode()
        birthday = date(int(year), int(month), int(day))

        url = f"http://127.0.0.1:8000/api/v1/employee/{int(self.employee['id'])}"
        response = requests.put(url=url, json={
            "username": full_name,
            "password": password,
            "email": work_email,
            "work_phone": work_number,
            "more_info": more_info,
            "birthday": str(birthday),
            "personal_phone": home_number,
            "position_id": job_title_id,
            "cabinet_id": cabinet_id,
            "boss_id": boss_id,
            "helper_id": helper_id,
            "organization": organization_id,
            "subdivision": sub_division_id,
            "sub_sub_division": sub_sub_division_id
        })
        if response.status_code != 200:
            QMessageBox.warning(self, "Предупреждение", "Пользователь не был добавлен. Скорее всего, не все поля заполнены верно!",
                                QMessageBox.StandardButton.Ok)
        self.close()

        


class AddEmployeeDialog(QDialog):
    def __init__(self, employees, cabinets, job_titles,
                 organizations, sub_divisions, sub_sub_divisions):
        super().__init__()

        self.employees = employees
        self.cabinets = cabinets
        self.boss = employees
        self.helpers = employees
        self.job_titles = job_titles
        self.organizations = organizations
        self.sub_divisions = sub_divisions
        self.sub_sub_divisions = sub_sub_divisions

        self.ui = add_employee_dialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.setup_optional_fields()

        self.ui.btn_save.clicked.connect(self.save)

    def save(self):
        full_name = self.ui.input_full_name.text()
        date_of_birth = self.ui.input_date_of_birth.text()
        more_info = self.ui.input_more_info.toPlainText()
        home_number = self.ui.input_home_number.text()
        work_number = self.ui.input_work_phone.text()
        work_email = self.ui.input_work_email.text()

        helper = self.ui.optional_helpers.currentText()
        helper_id = get_employee_id_by_name(helper)
        boss = self.ui.optional_boss.currentText()
        boss_id = get_employee_id_by_name(boss)
        job_title = self.ui.optional_job_titles.currentText()
        job_title_id = get_job_title_by_name(job_title)
        cabinet = self.ui.optional_cabinets.currentText()
        cabinet_id = get_cabinet_by_name(cabinet)
        organization = self.ui.optional_organizations.currentText()
        organization_id = get_organization_by_name(organization)
        sub_division = self.ui.optional_sub_divisions.currentText()
        sub_division_id = get_sub_division_by_name(sub_division)
        sub_sub_division = self.ui.optional_department.currentText()
        sub_sub_division_id = get_sub_sub_division_by_name(sub_sub_division)

        day, month, year = date_of_birth.split('.')
        password = bcrypt.hashpw(full_name.encode(), bcrypt.gensalt()).decode()
        birthday = date(int(year), int(month), int(day))

        url = "http://127.0.0.1:8000/api/v1/employees"
        response = requests.post(url=url, json={
            "username": full_name,
            "password": password,
            "email": work_email,
            "work_phone": work_number,
            "more_info": more_info,
            "birthday": str(birthday),
            "personal_phone": home_number,
            "position_id": job_title_id,
            "cabinet_id": cabinet_id,
            "boss_id": boss_id,
            "helper_id": helper_id,
            "organization": organization_id,
            "subdivision": sub_division_id,
            "sub_sub_division": sub_sub_division_id
        })
        if response.status_code == 201:
            QMessageBox.information(self, "Успешно", "Пользователь успешно добавлен",
                                    QMessageBox.StandardButton.Ok)
            self.close()
        if response.status_code == 400:
            QMessageBox.warning(self, "Предупреждение", "Пользователь не был добавлен. Скорее всего, не все поля заполнены верно!",
                                QMessageBox.StandardButton.Ok)


    def setup_optional_fields(self):
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_cabinets.addItems(self.cabinets)
        self.ui.optional_boss.addItems(self.employees)
        self.ui.optional_job_titles.addItems(self.job_titles)
        self.ui.optional_helpers.addItems(self.employees)
        self.ui.optional_organizations.addItems(self.organizations)
        self.ui.optional_sub_divisions.addItems(self.sub_divisions)
        self.ui.optional_department.addItems(self.sub_sub_divisions)