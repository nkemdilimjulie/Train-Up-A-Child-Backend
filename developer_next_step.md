# NEXT STEP
``see chatGPT: this project's Overview - last section.``

**continue from:** 

Step 7: Connect Django to PostgreSQL

Edit Train-Up-A-Child-Backend/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'train_up_a_child',
        'USER': 'tuc_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Step 8: Add apps and DRF to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your apps
    'sponsor',
    'children',
    'account',
    'guest',
    'donations',
    'documentation',
    
    # Third-party
    'rest_framework',
]

Step 9: Configure DRF JWT

Add to settings.py:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

Step 10: Migrate database and runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Follow prompts for admin
python manage.py runserver


Your backend should now be running at http://127.0.0.1:8000

✅ Next Steps

Start creating models for children, sponsor, account, and guest.

Add serializers, views, and URLs for DRF endpoints.

Add JWT login, registration, and permissions.

If you want, I can draw up a complete folder and file structure for your backend, including models for all apps and sub-apps, ready to plug into PostgreSQL and DRF. This will match your frontend plan exactly.

Do you want me to do that next?