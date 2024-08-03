# timetable/models.py

from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')

    def __str__(self):
        return self.name


class Timetable(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.course.name} in {self.classroom.name} on {self.day_of_week} from {self.start_time} to {self.end_time}"
