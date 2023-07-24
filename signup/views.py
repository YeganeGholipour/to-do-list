from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        # Call the form_valid method of the parent class to handle form validation
        response = super().form_valid(form)

        # Add a success message
        messages.success(self.request, "You have been registered successfully!")

        # Return the response
        return response
