# attendance/models.py

from django.db import models
from students.models import Student
from courses.models import Course


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student} - {self.course} on {self.date} - {'Present' if self.present else 'Absent'}"
