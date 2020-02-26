"""coworking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers

from apps.coworking import __version__, views


router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'workspaces', views.WorkspaceViewSet)
# router.register(r'offices', views.OfficeViewSet)
# router.register(r'reservations', views.ReservationListView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/{}/'.format(__version__), include(router.urls)),
    path('api/{}/offices/'.format(__version__), views.OfficeListView.as_view()),
    path('api/{}/reservations/'.format(__version__), views.ReservationListView.as_view()),
    path('api/{}/auth/'.format(__version__), include('rest_framework.urls'))
]
