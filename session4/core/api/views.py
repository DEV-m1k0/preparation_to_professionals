from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework import status
from models.models import *
from datetime import date
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions
from datetime import datetime
import random
from django.db.models import Q


"""
Файл с апишками
"""

class CalendarEventAPIView(generics.DestroyAPIView, generics.CreateAPIView):
    serializer_class = EventSerializers

    def delete(self, request, *args, **kwargs):
        
        employee_name = request.GET.get("employee")
        event_date = datetime.strptime(request.GET.get('date'), '%d.%m.%Y %H:%M:%S')

        # try:
        employee_obj = Employee.objects.get(username=employee_name)
        Event.objects.filter(Q(responsible_worker=employee_obj) & (Q(date_since=event_date) | Q(date_until=event_date))).first().delete()
        return Response(
            {
                "message": f"Обучение с Промежутком с датой {event_date.strftime('%d.%m.%Y %H:%M')} удален"
            }, status=status.HTTP_200_OK
        )
        # except:
        #     return Response(
        #         {
        #             "error": f"Произошла ошибка при удалении обучения с Промежутком с датой {event_date.strftime('%d.%m.%Y %H:%M')}"
        #         }, status=status.HTTP_400_BAD_REQUEST
        #     )

    def create(self, request, *args, **kwargs):
        employee_name = request.GET.get('employee')
        event_title = request.GET.get('event_title')
        date_since = datetime.strptime(request.GET.get('date_since'), '%d.%m.%Y %H:%M')
        date_before = datetime.strptime(request.GET.get('date_until'), '%d.%m.%Y %H:%M')

        print(date_since, type(date_since))
        
        employee_obj = Employee.objects.get(username=employee_name)

        try:
            Event.objects.create(title=event_title, responsible_worker=employee_obj, date_since=date_since, date_until=date_before)
            return Response({
                "message": f"Обучение {event_title} с датой {date_since} до {date_before} создано"
            }, status=status.HTTP_201_CREATED)
        except:
            return Response(
                {
                    "error": f"Произошла ошибка при создании обучения {event_title}"
                }, status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        employee_name = request.GET.get("employee")
        some_date: str = request.GET.get("date")

        
        employee_obj = Employee.objects.get(username=employee_name)
        vacation_obj = CalendarVacation.objects.filter(Q(employee=employee_obj) & (Q(date_since=datetime.strptime(some_date, "%d.%m.%Y")) | Q(date_until=datetime.strptime(some_date, "%d.%m.%Y")))).first()

        try:
            if str(vacation_obj.date_since) == datetime.strptime(some_date, "%d.%m.%Y").strftime("%Y-%m-%d"):
                vacation_obj.delete()
                return Response({
                    "message": f"Пропуск с даты {some_date} удален"
                }, status=status.HTTP_200_OK)
        except:
            return Response({
                "message": f"Произошла ошибка при удалении пропуска с датой {some_date}"
            }, status=status.HTTP_400_BAD_REQUEST)
        


class CalendarVacationAPIView(generics.DestroyAPIView, generics.CreateAPIView):
    serializer_class = VacationDateSerializers

    def create(self, request, *args, **kwargs):
        employee_name = request.GET.get('employee')
        date_since = datetime.strptime(request.GET.get('date_since'), '%d.%m.%Y')
        date_before = datetime.strptime(request.GET.get('date_before'), '%d.%m.%Y')
        
        employee_obj = Employee.objects.get(username=employee_name)

        try:
            CalendarVacation.objects.create(employee=employee_obj, date_since=date_since, date_until=date_before)
            return Response({
                "message": f"Пропуск с датой {date_since} до {date_before} создан"
            }, status=status.HTTP_201_CREATED)
        except:
            return Response({
                "message": f"Произошла ошибка при создании пропуска с датой {date_since} до {date_before}"
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        employee_name = request.GET.get("employee")
        some_date: str = request.GET.get("date")

        
        employee_obj = Employee.objects.get(username=employee_name)
        vacation_obj = CalendarVacation.objects.filter(Q(employee=employee_obj) & (Q(date_since=datetime.strptime(some_date, "%d.%m.%Y")) | Q(date_until=datetime.strptime(some_date, "%d.%m.%Y")))).first()

        try:
            if str(vacation_obj.date_since) == datetime.strptime(some_date, "%d.%m.%Y").strftime("%Y-%m-%d"):
                vacation_obj.delete()
                return Response({
                    "message": f"Пропуск с даты {some_date} удален"
                }, status=status.HTTP_200_OK)
        except:
            return Response({
                "message": f"Произошла ошибка при удалении пропуска с датой {some_date}"
            }, status=status.HTTP_400_BAD_REQUEST)


class CalendarSkipAPIView(generics.DestroyAPIView, generics.CreateAPIView):
    serializer_class = CalendarSkipSerializer

    def create(self, request, *args, **kwargs):
        employee_name = request.GET.get('employee')
        date_since = datetime.strptime(request.GET.get('date_since'), '%d.%m.%Y')
        date_before = datetime.strptime(request.GET.get('date_before'), '%d.%m.%Y')
        
        employee_obj = Employee.objects.get(username=employee_name)

        try:
            CalendarSkip.objects.create(employee=employee_obj, date_since=date_since, date_until=date_before)
            return Response({
                "message": f"Пропуск с датой {date_since} до {date_before} создан"
            }, status=status.HTTP_201_CREATED)
        except:
            return Response({
                "message": f"Произошла ошибка при создании пропуска с датой {date_since} до {date_before}"
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        employee_name = request.GET.get("employee")
        some_date: str = request.GET.get("date")

        
        employee_obj = Employee.objects.get(username=employee_name)
        skip_obj = CalendarSkip.objects.filter(Q(employee=employee_obj) & (Q(date_since=datetime.strptime(some_date, "%d.%m.%Y")) | Q(date_until=datetime.strptime(some_date, "%d.%m.%Y")))).first()

        try:
            if str(skip_obj.date_since) == datetime.strptime(some_date, "%d.%m.%Y").strftime("%Y-%m-%d"):
                skip_obj.delete()
                return Response({
                    "message": f"Пропуск с даты {some_date} удален"
                }, status=status.HTTP_200_OK)
        except:
            return Response({
                "message": f"Произошла ошибка при удалении пропуска с датой {some_date}"
            }, status=status.HTTP_400_BAD_REQUEST)


class DocumentListAPIView(generics.ListAPIView):
    """
    Получение всех документов
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DocumentCreateAPIView(generics.CreateAPIView):
    """
    Создание документов
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DocumentCommentListAPIView(generics.ListAPIView):
    """
    Получение комментариев к документам
    """
    queryset = DocumentComment.objects.all()
    serializer_class = DocumentCommentSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, documentId: int, *args, **kwargs):
        try:
            doc_comment = DocumentComment.objects.get(pk=documentId)
            serializer = DocumentCommentSerializer(doc_comment)
            return Response(serializer.data)
        except:
            return Response({
                "timestamp": datetime.now(),
                "message": "Не найдены комментарии для документа",
                "errorCode": random.randint(1000, 9999)
            }, status=404)


class EmployeeDismissAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get("employee") is not None:
            employee_name: str = request.GET.get("employee")
            try:
                employer = Employee.objects.get(username=employee_name)
                employer_events = Event.objects.filter(responsible_worker=employer.pk)
                if employer_events.count() == 0:
                    employer.is_active = False
                    employer.date_of_dismissal = date.today()
                    employer.save()
                    return Response({
                        "message": f"Пользователя {employee_name} отстранен от работы"
                    })
                else:
                    return Response({
                        "error": f"Пользователь {employee_name} имеет события в рамках которых он работает"
                    }, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({
                    "error": f"пользователь {employee_name} не найден"
                }, status=status.HTTP_404_NOT_FOUND)
        return Response({
            "error": "employee parameter is required"
        }, status=status.HTTP_400_BAD_REQUEST)

class SkipDateByEmployeeListAPIView(ListAPIView):
    queryset = CalendarSkip.objects.all()
    serializer_class = SkipDataSerializers

    def get(self, request, *args, **kwargs):
        if request.GET.get("employee") is not None:
            employee_name: str = request.GET.get("employee")
            try:
                employer = Employee.objects.get(username=employee_name)
                skips = CalendarSkip.objects.filter(employee=employer.pk)
                serializer = SkipDataSerializers(skips, many=True)
                return Response(serializer.data)
            except:
                return Response({
                    "error": f"пользователь {employee_name} не найден"
                }, status=status.HTTP_404_NOT_FOUND)
        return super().get(request, *args, **kwargs)
    

class VacationDateByEmployeeListAPIView(ListAPIView):
    queryset = CalendarVacation.objects.all()
    serializer_class = VacationDateSerializers

    def get(self, request, *args, **kwargs):
        if request.GET.get("employee") is not None:
            employee_name: str = request.GET.get("employee")
            try:
                employer = Employee.objects.get(username=employee_name)
                vacations = CalendarVacation.objects.filter(employee=employer.pk)
                serializer = VacationDateSerializers(vacations, many=True)
                return Response(serializer.data)
            except:
                return Response({
                    "error": f"пользователь {employee_name} не найден"
                }, status=status.HTTP_404_NOT_FOUND)
        return super().get(request, *args, **kwargs)


class EventByResponsiblePeople(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDataSerializers

    def get(self, request, *args, **kwargs):
        if request.GET.get("responsible") is not None:
            employee_name: str = request.GET.get("responsible")
            try:
                employer = Employee.objects.get(username=employee_name)
                events = Event.objects.filter(responsible_worker=employer.pk)
                print(events)
                serializer = EventDataSerializers(events, many=True)
                return Response(serializer.data)
            except:
                return Response({
                    "error": f"пользователь {employee_name} не найден"
                }, status=status.HTTP_404_NOT_FOUND)
        return super().get(request, *args, **kwargs)

class CabineRetriveAPIView(RetrieveAPIView):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializers

    def get(self, request, name: str, *args, **kwargs):
        try:
            cabinet = Cabinet.objects.get(title=name)
            serializer = CabinetSerializers(cabinet)
            return Response(serializer.data)
        except:
            return Response()


class CabineListAPIView(ListAPIView):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializers


class JobTitleListAPIView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = JobTitleSerializers


class JobTitleByNameAPIView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = JobTitleSerializers

    def get(self, request, name: str, *args, **kwargs):
        try:
            job_title = Position.objects.get(title=name)
            serializer = JobTitleSerializers(job_title)
            return Response(serializer.data)
        except:
            return Response()


class OrganizationListApiView(ListAPIView):
    serializer_class = OrgarizationsSerializer
    queryset = Organization.objects.all().order_by("pk")


class OrganizationByNameListApiView(ListAPIView):
    serializer_class = OrgarizationsSerializer
    queryset = Organization.objects.all()

    def get(self, request, name: str, *args, **kwargs):
        try:
            organizaation = Organization.objects.get(title=name)
            serializer = OrgarizationsSerializer(organizaation)
            return Response(serializer.data)
        except:
            return Response()
        

class OrganizationByIdAPIView(ListAPIView):
    serializer_class = OrgarizationsSerializer
    queryset = Organization.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            org_pk = request.GET.get('pk')
            org = Organization.objects.get(pk=org_pk)
            return Response(OrgarizationsSerializer(org).data)
        except:
            return Response()


class SubDivisionListApiView(ListAPIView):
    serializer_class = SubDivisionsSerializer
    queryset = Subdivision.objects.all()


class SubDivisionByNameListApiView(ListAPIView):
    serializer_class = SubDivisionsSerializer
    queryset = Subdivision.objects.all()


    def get(self, request, name: str, *args, **kwargs):
        try:
            sub_division = Subdivision.objects.get(title=name)
            serializer = SubDivisionsSerializer(sub_division)
            return Response(serializer.data)
        except: 
            return Response

class SubSubDivisionListApiView(ListAPIView):
    serializer_class = SubSubDivisionsSerializer
    queryset = SubSubDivision.objects.all()


class SubSubDivisionByNameListApiView(ListAPIView):
    serializer_class = SubSubDivisionsSerializer
    queryset = SubSubDivision.objects.all()

    def get(self, request, name: str, *args, **kwargs):
        try:
            sub_sub_division = SubSubDivision.objects.get(title=name)
            serializer = SubDivisionsSerializer(sub_sub_division)
            return Response(serializer.data)
        except: 
            return Response


class EmployeeListApiView(ListAPIView, CreateAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employee.objects.filter(is_active=True)


class EmployeeUpdateApiView(UpdateAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employee.objects.all()


class EmployeeSearchByNameApiView(ListAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employee.objects.all()

    def get(self, request, name: str, *args, **kwargs):
        try:
            employee = Employee.objects.get(username=name)
            serializer = EmployeesSerializer(employee)
            return Response(serializer.data)
        except:
            return Response()

class EmployeeSearchByDepartmentApiView(ListAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employee.objects.filter()

    def get(self, request, department: str, *args, **kwargs):
        try:
            organization = Organization.objects.get(title=department)
            serializer = EmployeesSerializer(Employee.objects.filter(organization=organization), many=True)
            return Response(serializer.data)
        except:
            pass
        try:
            sub_division = Subdivision.objects.get(title=department)
            serializer = EmployeesSerializer(Employee.objects.filter(subdivision=sub_division), many=True)
            return Response(serializer.data)
        except:
            pass
        try:
            sub_sub_division = SubSubDivision.objects.get(title=department)
            employees = Employee.objects.filter(sub_sub_division=sub_sub_division)
            serializer = EmployeesSerializer(employees, many=True)
            return Response(serializer.data)
        except:
            pass
        return Response()