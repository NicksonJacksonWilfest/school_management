# teachers/forms.py

from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'date_of_birth', 'subject', 'address', 'phone_number', 'email']
