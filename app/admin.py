from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FAQ, FAQTranslation

admin.site.register(FAQ)
admin.site.register(FAQTranslation)
