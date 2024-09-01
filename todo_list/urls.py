from django.urls import path
from . import views

urlpatterns = [
    path('' , views.task_list , name='task_list'),
    path('add_task/' , views.add_task , name='add_task'),
    path('task_done/<int:pk>/' , views.task_done , name='task_done'),
    path('delete_task/<int:pk>/' , views.delete_task , name='delete_task'),
    path('un_do_task/<int:pk>/' , views.un_do_task , name='un_do_task'),
]