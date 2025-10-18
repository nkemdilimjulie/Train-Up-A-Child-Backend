from django.db import models

class Child(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    class_name = models.CharField(max_length=80)
    address = models.CharField(max_length=255)
    guardian_name = models.CharField(max_length=120)
    guardian_email = models.EmailField()
    guardian_phone = models.CharField(max_length=30, blank=True, null=True)
    story = models.TextField()
    photo = models.ImageField(upload_to="children_photos/", blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

