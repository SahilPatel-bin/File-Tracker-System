"""file_tracker_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home),
    path('home/',views.index),
    path('signup/',views.signup),
    path('login/',views.login),
    path('logout/',views.logout),
    path('forgotPassword/',views.forgotPassword),
    path('dashboard/',views.dashboard),
    path('fileManagement/',views.fileManagement),
    path('manageProfile/',views.manageProfile),
    path('fileAdd/',views.addFile),
    path('fileUpdate/',views.updateFileData),
    path('notificationDetails/',views.notificationDetails),
    path('loadUsers/',views.load_users),
    path('notification/',views.notification),
    path('readFile/',views.readFile),
    path('notificationForward/',views.notificationForward),
    path('notificationClose/',views.notificationClose),
    path('reports/',views.fileReports),
    path('searchFiles/',views.searchFiles),
    path('printData/',views.printData),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
