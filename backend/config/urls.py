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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from apps.coworking import __version__, views


urlpatterns = [
    path('api/{}/workspaces/'.format(__version__), views.WorkspaceListView.as_view()),
    path('api/{}/workspaces/<int:pk>/'.format(__version__), views.WorkspaceView.as_view()),
    path('api/{}/offices/'.format(__version__), views.OfficeListView.as_view()),
    path('api/{}/reservations/'.format(__version__), views.ReservationListView.as_view())
]

if settings.DEBUG:
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('api/{}/auth/'.format(__version__), include('rest_framework.urls'))
    ]