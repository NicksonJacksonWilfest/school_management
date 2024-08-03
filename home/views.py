# home/views.py

from django.shortcuts import render


def homepage(request):
    return render(request, 'home/homepage.html')
