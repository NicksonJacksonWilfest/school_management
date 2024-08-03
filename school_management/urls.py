# school_management/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('courses/', include('courses.urls')),
    path('exams/', include('exams.urls')),
    path('timetable/', include('timetable.urls')),
    path('attendance/', include('attendance.urls')),
]

handler404 = 'school_management.views.custom_404'
