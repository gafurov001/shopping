"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # url для войти в админку
    path('api/v1/', include('apps.urls')),
    # для привязки URL-адресов apps.urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Эта url маршрута генерирует JSON-схему API, которая может быть использована Swagger для документирования и визуализации API.
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # url для войти в Swagger
    path(' token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # этот URL-адрес для получения токенов refresh и access
    path(' token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # чтобы получить токен access, отправив токен refresh на URL-адрес
]
