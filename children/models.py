from django.db import models
from django.conf import settings

class ChildProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        null=False,       # make required
        blank=False,
        default="",
        help_text="Associated user account"
    )

    age = models.PositiveIntegerField(default=0)
    class_name = models.CharField(max_length=100, default="")
    guardian_name = models.CharField(max_length=255, default="")
    guardian_phone = models.CharField(max_length=50, default="")
    guardian_email = models.EmailField(default="unknown@example.com")
    story = models.TextField(default="")
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        username = self.user.username if self.user else "NoUser"
        first_name = self.user.first_name if self.user else ""
        last_name = self.user.last_name if self.user else ""
        return f"Child: {username} - {first_name} {last_name}"
