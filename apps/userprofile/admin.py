from django.contrib import admin

from .models import Profile

admin.site.register(Profile) # Dont forget makemigrations and migrate it
