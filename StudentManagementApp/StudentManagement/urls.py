from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_students, name='list_students'),
    path('create_student/', views.create_student, name='create_student'),
]

