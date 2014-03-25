from django.contrib import admin
from Login.models import APIKey
# Register your models here.

admin.autodiscover()

admin.site.register(APIKey)