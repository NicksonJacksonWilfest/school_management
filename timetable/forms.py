# timetable/forms.py

from django import forms
from .models import Classroom, Course, Timetable


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'capacity']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'teacher', 'duration']


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['classroom', 'course', 'start_time', 'end_time', 'day_of_week']
