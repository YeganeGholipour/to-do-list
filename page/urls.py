from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView,
    TaskView,
    AddTaskView,
    ListUserTasksView,
    DeleteTaskView,
    EditTaskView,
    AllCategories,
    EachCategory,
    AddCategoryView,
    ProfileView,
    ProfileEditView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("user_tasks/", ListUserTasksView.as_view(), name="list_users_task"),
    path("task/<int:pk>", TaskView.as_view(), name="each_task"),
    path("add_task/", AddTaskView.as_view(), name="add_task"),
    path("delete_task/<int:pk>", DeleteTaskView.as_view(), name="delete_task"),
    path("edit_task/<int:pk>", EditTaskView.as_view(), name="edit_task"),
    path("category/", AllCategories.as_view(), name="all_categories"),
    path("category/<str:cat>", EachCategory.as_view(), name="each_category"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit", ProfileEditView.as_view(), name="edit_profile"),
]
