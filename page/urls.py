from django.contrib import admin
from django.urls import path, include
from .views import HomeView, TaskView, AddTaskView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("task/<int:pk>", TaskView.as_view(), name="each_task"),
    path("add_task/", AddTaskView.as_view(), name="add_task"),
]
