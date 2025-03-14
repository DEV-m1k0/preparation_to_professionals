from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

"""
Файл со всеми моделями в системе
"""


class SubSubDivision(models.Model):
    "Модель с подподразделениями"
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Subdivision(models.Model):
    "Модель с подразделениями"
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255, null=True)
    responsible = models.ForeignKey("Employee", on_delete=models.SET_NULL, related_name="responsible", null=True)
    sub_sub_division = models.ManyToManyField(SubSubDivision, blank=True)

    def __str__(self):
        return self.title
    

class Organization(models.Model):
    "Модель с организациями"
    title = models.CharField(max_length=255)
    subdivisions = models.ManyToManyField(Subdivision, related_name="subdivisions", blank=True)

    def __str__(self):
        return self.title


class Position(models.Model):
    "Модель с должностями сотрудников"
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.title)


class Cabinet(models.Model):
    "Модель с кабинетами"
    title = models.CharField(max_length=10, unique=True)


class CalendarSkip(models.Model):
    "Модель с календарем пропусков"
    employee = models.ForeignKey("Employee", null=True, on_delete=models.SET_NULL)
    date_since = models.DateField(null=True, blank=True)
    date_until = models.DateField(null=True, blank=True)


class CalendarVacation(models.Model):
    "Модель с календарем отпусков"
    employee = models.ForeignKey("Employee", null=True, on_delete=models.SET_NULL)
    date_since = models.DateField(null=True, blank=True)
    date_until = models.DateField(null=True, blank=True)
    

class Event(models.Model):
    "Модель с событиями"
    title = models.CharField(max_length=255)
    date_since = models.DateTimeField()
    date_until = models.DateTimeField()
    description = models.TextField(max_length=255, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    responsible_worker = models.ForeignKey("Employee", related_name="responsible_workers", null=True, blank=True, on_delete=models.SET_NULL)
    event_type_id = models.ForeignKey("EventType", on_delete=models.CASCADE, related_name="event_type", blank=True, null=True)
    education_id = models.ForeignKey("Education", on_delete=models.CASCADE, related_name="education", blank=True, null=True)
    people = models.ManyToManyField("Employee", blank=True)

class EducationType(models.Model):
    "Модель с типом обучения"
    title = models.CharField(max_length=255)


class MaterialStatus(models.Model):
    "Модель со статусом материалла"
    title = models.CharField(max_length=255)


class MaterialType(models.Model):
    "Модель с типом материала"
    title = models.CharField(max_length=255)


class MaterialArea(models.Model):
    "Модель с областью материала"
    title = models.CharField(max_length=255)


class Material(models.Model):
    "Модель с материаллами"
    title = models.CharField(max_length=255)
    date_aprove = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)
    status_id = models.ForeignKey("MaterialStatus", on_delete=models.CASCADE, related_name="status")
    type_id = models.ForeignKey("MaterialType", on_delete=models.CASCADE, related_name="type")
    area_id = models.ForeignKey("MaterialArea", on_delete=models.CASCADE, related_name="area")
    author = models.CharField(max_length=255)
    file = models.FileField(null=True, blank=True)


class Education(models.Model):
    "Модель с обучнением"
    materials = models.ManyToManyField("Material", blank=True, related_name="materials")
    education_type_id = models.ForeignKey("EducationType", on_delete=models.CASCADE, related_name="education_type")


class EventType(models.Model):
    "Модель с типом мероприятия"
    title = models.CharField(max_length=255)


class Employee(AbstractUser):
    "Модель с сотрудниками"
    full_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    position_id = models.ForeignKey("Position", on_delete=models.SET_NULL, null=True, related_name="position")
    work_phone = models.CharField(max_length=20, null=True)
    cabinet_id = models.ForeignKey("Cabinet", on_delete=models.SET_NULL, null=True, related_name="cabinet")
    boss_id = models.ForeignKey("Employee", on_delete=models.SET_NULL, related_name="boss", null=True)
    helper_id = models.ForeignKey("Employee", on_delete=models.SET_NULL, related_name="helper", null=True)
    organization = models.ForeignKey("Organization", null=True, on_delete=models.SET_NULL)
    subdivision = models.ForeignKey("SubDivision", on_delete=models.SET_NULL, null=True, related_name="employee_subdivision")
    sub_sub_division = models.ForeignKey("SubSubDivision", on_delete=models.SET_NULL, null=True, related_name="employye_sub_sub_division")
    more_info = models.TextField(max_length=255, null=True)
    birthday = models.DateField(null=True)
    personal_phone = models.CharField(max_length=20, null=True)
    date_of_dismissal = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.username)


class DocumentCategory(models.Model):
    "Модель с категориями документа"
    title = models.CharField(max_length=255)


class DocumentComment(models.Model):
    "Модель с комментариями документа"
    document_id = models.ForeignKey("Document", on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("Employee", on_delete=models.CASCADE)

    def __str__(self):
        return self.text



class Document(models.Model):
    "Модель с документами"
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField("DocumentCategory", blank=True)
    has_comment = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)