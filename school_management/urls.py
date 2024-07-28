# school_management/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('', include('teachers.urls')),
    path('', include('courses.urls')),
    path('', include('exams.urls')),
]

handler404 = 'school_management.views.custom_404'
