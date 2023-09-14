from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title_tag = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, default=None
    )
    due_date = models.DateField(default=None, null=True, blank=True)
    info = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    avatar = models.ImageField(
        default="avatar.jpg",  # default avatar
        upload_to="profile_avatars",  # dir to store the image
    )
    bio = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        """
        ensure that the default behavior of
          saving the model to the database is
          not overridden by your custom save method.
        """
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)


class ContactInformation(models.Model):
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    contact_type = models.CharField(
        max_length=50, default=None, null=True, blank=True
    )  # E.g., GitHub, Website, Email, etc.
    contact_value = models.CharField(
        max_length=255, default=None, null=True, blank=True
    )

    def __str__(self):
        return f"{self.contact_type}: {self.contact_value}"
