# courses/models.py

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.PositiveIntegerField()

    def __str__(self):
        return self.name
