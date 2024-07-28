# exams/forms.py

from django import forms
from .models import Exam


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name', 'description', 'date', 'duration', 'total_marks']
