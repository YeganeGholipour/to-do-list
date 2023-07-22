from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=250)
    completed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    title_tag = models.CharField(max_length=250)
    due_date = models.DateField()
    info = models.TextField()

    def __str__(self):
        return self.title
