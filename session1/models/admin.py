from django.contrib import admin
from models.models import *

"""
Настройка админ панели
"""


admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Cabinet)
admin.site.register(Document)
admin.site.register(DocumentCategory)
admin.site.register(DocumentComment)
admin.site.register(Material)
admin.site.register(MaterialArea)
admin.site.register(MaterialStatus)
admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(Organization)
admin.site.register(Subdivision)
admin.site.register(SubSubDivision)
admin.site.register(CalendarSkip)
admin.site.register(CalendarVacation)
admin.site.register(EducationType)
admin.site.register(MaterialType)
admin.site.register(Education)