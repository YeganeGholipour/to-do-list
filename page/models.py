from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # title_tag = models.CharField(max_length=250, default="Uncategorized")
    title_tag = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    due_date = models.DateField(default=None, null=True, blank=True)
    info = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.title
