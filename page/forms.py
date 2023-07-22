from django import forms
from .models import Tasks
from django.contrib.auth import get_user_model


class AddTask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ("title", "completed", "title_tag", "due_date", "info")
        widget = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add Title For Task ..."}
            ),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "title_tag": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add Title Tag For Task ...",
                }
            ),
            "info": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add Necessarry Information about Task ...",
                }
            ),
            "due_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


class EditTask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ("title", "completed", "title_tag", "due_date", "info")
        widget = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add Title For Task ..."}
            ),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "title_tag": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add Title Tag For Task ...",
                }
            ),
            "info": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Add Necessarry Information about Task ...",
                }
            ),
            "due_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
