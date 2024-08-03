# timetable/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Classroom, Course, Timetable
from .forms import ClassroomForm, CourseForm, TimetableForm


def timetable_list(request):
    timetables = Timetable.objects.all()
    return render(request, 'timetable/timetable_list.html', {'timetables': timetables})


def timetable_detail(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    return render(request, 'timetable/timetable_detail.html', {'timetable': timetable})


def timetable_create(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable:timetable_list')
    else:
        form = TimetableForm()
    return render(request, 'timetable/timetable_form.html', {'form': form})


def timetable_update(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        form = TimetableForm(request.POST, instance=timetable)
        if form.is_valid():
            form.save()
            return redirect('timetable:timetable_list')
    else:
        form = TimetableForm(instance=timetable)
    return render(request, 'timetable/timetable_form.html', {'form': form})


def timetable_delete(request, pk):
    timetable = get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        timetable.delete()
        return redirect('timetable:timetable_list')
    return render(request, 'timetable/timetable_confirm_delete.html', {'timetable': timetable})
