# from django.db import models
# from django.conf import settings

# User = settings.AUTH_USER_MODEL

# class SponsorProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sponsor_profile")
#     organization_name = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=100, blank=True, null=True)
#     website = models.URLField(blank=True, null=True)
#     phone = models.CharField(max_length=30, blank=True, null=True)
    
#     date_registered = models.DateTimeField(auto_now_add=True, blank=True, null=True)

#     def __str__(self):
#         return self.organization_name or self.user.username


from django.db import models
from django.conf import settings

class SponsorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sponsor_profile")
    sponsor_id = models.CharField(max_length=100, unique=True, blank=True, null=True,
                                  help_text="Internal or Stripe-linked Sponsor ID")
    organization = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Sponsor: {self.user.username} {self.user.first_name} {self.user.last_name}"
