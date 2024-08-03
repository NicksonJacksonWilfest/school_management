# timetable/urls.py

from django.urls import path
from . import views

app_name = 'timetable'

urlpatterns = [
    path('', views.timetable_list, name='timetable_list'),
    path('<int:pk>/', views.timetable_detail, name='timetable_detail'),
    path('create/', views.timetable_create, name='timetable_create'),
    path('<int:pk>/edit/', views.timetable_update, name='timetable_update'),
    path('<int:pk>/delete/', views.timetable_delete, name='timetable_delete'),
]
