from django.contrib import admin
from django.urls import path, include
from .views import HomeView, TaskView, AddTaskView, ListUserTasksView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("user_tasks/", ListUserTasksView.as_view(), name="list_users_task"),
    path("task/<int:pk>", TaskView.as_view(), name="each_task"),
    path("add_task/", AddTaskView.as_view(), name="add_task"),
]
