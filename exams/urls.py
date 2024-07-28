# exams/urls.py

from django.urls import path
from . import views

app_name = 'exams'

urlpatterns = [
    path('', views.ExamListView.as_view(), name='exam_list'),
    path('add/', views.ExamCreateView.as_view(), name='exam_add'),
    path('<int:pk>/', views.ExamDetailView.as_view(), name='exam_detail'),
    path('<int:pk>/edit/', views.ExamUpdateView.as_view(), name='exam_edit'),
    path('<int:pk>/delete/', views.ExamDeleteView.as_view(), name='exam_delete'),
]
