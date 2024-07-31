from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('', views.add_task, name='add-task-db'),
    path('viewdbtask/', views.viewtask, name='view-task-db'),
    path('editdbtask/', views.edittask, name='edit-task-db'),
    path('completeddbtask/', views.completedtask, name='completed-task-db'),
    path('mark_as_done/<int:task_id>/', views.mark_as_done, name='mark-as-done'),
    path('edit_task/<int:task_id>/', views.mark_edit_task, name='mark-as-edit_task'),
    path('taskdelete/<int:task_id>/', views.taskdelete, name='taskdelete'),
]
