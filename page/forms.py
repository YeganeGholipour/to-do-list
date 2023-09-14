from django import forms
from .models import Tasks, Category
from django.contrib.auth import get_user_model


class AddTask(forms.ModelForm):
    title_tag = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Choose a category..."
    )

    class Meta:
        model = Tasks
        fields = ("title", "completed", "due_date", "info")
        widget = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add Title For Task ..."}
            ),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
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
    title_tag = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Choose a category..."
    )

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


class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)
        widgets = {  # Use "widgets" (plural)
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add a new category..."}
            ),
        }
