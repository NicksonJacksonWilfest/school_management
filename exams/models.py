# exams/models.py

from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    duration = models.DurationField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.name
