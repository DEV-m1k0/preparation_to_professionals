from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *

urlpatterns = [
    path("events/date", EventByResponsiblePeople.as_view()),
    path("vacations/date", VacationDateByEmployeeListAPIView.as_view()), 
    path("skips/date", SkipDateByEmployeeListAPIView.as_view()), 
    path("organizations", OrganizationListApiView.as_view()),
    path("organizations/search_name/<str:name>", OrganizationByNameListApiView.as_view()),
    path("organization", OrganizationByIdAPIView.as_view()),
    path("subdivisions", SubDivisionListApiView.as_view()),
    path("subdivisions/search_name/<str:name>", SubDivisionByNameListApiView.as_view()),
    path("subsubdivisions", SubSubDivisionListApiView.as_view()),
    path("subsubdivisions/search_name/<str:name>", SubSubDivisionByNameListApiView.as_view()),
    path("cabinets", CabineListAPIView.as_view()),
    path("cabinets/<str:name>", CabineRetriveAPIView.as_view()),
    path("jobtitles", JobTitleListAPIView.as_view()),
    path("jobtitles/search_name/<str:name>", JobTitleByNameAPIView.as_view()),
    path("employees", EmployeeListApiView.as_view()),
    path("employee/<int:pk>", EmployeeUpdateApiView.as_view()),
    path("employee/dismiss", EmployeeDismissAPIView.as_view()),
    path("employees/search_department/<str:department>", EmployeeSearchByDepartmentApiView.as_view()),
    path("employees/search_name/<str:name>", EmployeeSearchByNameApiView.as_view()),
]