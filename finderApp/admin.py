from django.contrib import admin
from . import models

admin.AdminSite.site_header = 'My Awesome finder Admin Panel!'

# Register your models here.

admin.site.register(models.Todo)
admin.site.register(models.Question)
admin.site.register(models.Choice)