from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tasks
from .forms import AddTask, EditTask
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
