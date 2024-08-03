# timetable/admin.py

from django.contrib import admin
from .models import Classroom, Course, Timetable

admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Timetable)
