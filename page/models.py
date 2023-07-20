from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title_tag = models.CharField(max_length=250, default="uncategorized")
    due_date = models.DateField(default=None, null=True, blank=True)
    info = models.TextField(default="default value")

    def __str__(self):
        return self.title
