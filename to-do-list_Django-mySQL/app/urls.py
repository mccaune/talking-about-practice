from django.urls import path, include
from app import views


urlpatterns = [
    path('', views.task, name='task'),
    path('add_task/', views.add_task, name='add-task'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit-task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete-task'),
]