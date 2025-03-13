from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static
from api.views import *


"""
Главный файл с маршрутизацией проекта
"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("api/v1/SignIn", TokenObtainPairView.as_view()),
    path('api/v1/Documents', DocumentListAPIView.as_view()),
    path('api/v1/Document/<int:documentId>/Comments', DocumentCommentListAPIView.as_view()),
    path('api/v1/document', DocumentCreateAPIView.as_view()),
    path('api/v1/', include('api.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)