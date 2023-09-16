from django import forms
from .models import Tasks, Category, Profile, ContactInformation
from django.contrib.auth import get_user_model


class AddTask(forms.ModelForm):
    title_tag = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Choose a category..."
    )

    class Meta:
        model = Tasks
        fields = ("title", "completed", "due_date", "info", "title_tag")
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
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add a new category..."}
            ),
        }


class EditProfile(forms.ModelForm):
    contact_type = forms.CharField(max_length=50, required=False)
    contact_value = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Profile
        fields = (
            "avatar",
            "bio",
        )

    def save(self, commit=True):
        profile = super().save(commit=False)

        contact_type = self.cleaned_data.get("contact_type")
        contact_value = self.cleaned_data.get("contact_value")

        if contact_type and contact_value:
            # Update or create the contact information
            contact_info, created = ContactInformation.objects.get_or_create(
                user_profile=profile,
                defaults={"contact_type": contact_type, "contact_value": contact_value},
            )

            if not created:
                contact_info.contact_type = contact_type
                contact_info.contact_value = contact_value
                contact_info.save()

        if commit:
            profile.save()

        return profile
