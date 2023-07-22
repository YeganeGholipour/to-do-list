from django.shortcuts import render
from .models import Tasks
from .forms import AddTask
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, DetailView


# def HomeView(request):
# return render(request, "home.html")


class HomeView(ListView):
    model = Tasks
    template_name = "list_tasks.html"


class TaskView(DetailView):
    model = Tasks
    template_name = "each_task.html"


class AddTaskView(CreateView):
    model = Tasks
    template_name = "add_task.html"
    form_class = AddTask
    success_url = reverse_lazy("home")
