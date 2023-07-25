from typing import Any
from django.db import models
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tasks, Category
from .forms import AddTask, EditTask, AddCategory
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    DetailView,
    UpdateView,
)


# def HomeView(request):
# return render(request, "home.html")


class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        # Prepare any data you want to pass to the template
        context = {
            # Add any context data you want to use in the template
        }

        # Render the template with the context and return the HttpResponse
        context["user"] = request.user
        user = self.request.user
        print(user)
        return render(request, self.template_name, context)


class ListUserTasksView(ListView):
    model = Tasks
    template_name = "list_tasks.html"

    def get_queryset(self):
        # Get the queryset for tasks and filter based on the logged-in user
        # Assuming your Tasks model has a ForeignKey to the User model named 'user'
        user = self.request.user
        return Tasks.objects.filter(user=user)


class TaskView(DetailView):
    model = Tasks
    template_name = "each_task.html"


class AddTaskView(LoginRequiredMixin, CreateView):
    model = Tasks
    template_name = "add_task.html"
    form_class = AddTask
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # Set the 'user' field to the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteTaskView(DeleteView):
    model = Tasks
    template_name = "delete_task.html"
    success_url = reverse_lazy("list_users_task")


class EditTaskView(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = "edit_task.html"
    form_class = EditTask
    success_url = reverse_lazy("list_users_task")

    def form_valid(self, form):
        # Set the 'user' field to the currently logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)


class AllCategories(ListView):
    model = Tasks
    template_name = "all_categories.html"
    context_object_name = "categories"

    def get_queryset(self):
        return Tasks.objects.values_list("title_tag", flat=True).distinct()


class EachCategory(ListView):
    model = Tasks
    template_name = "each_category.html"
    context_object_name = "tasks"

    def get_queryset(self):
        title_tag = self.kwargs.get("cat")
        return Tasks.objects.filter(title_tag=title_tag)


class AddCategoryView(CreateView):
    model = Category
    fields = ("name",)
    template_name = "add_category.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # Save the new category and return to the home page
        self.object = form.save()
        return redirect(self.get_success_url())
