""" This file is used to register the models with the admin site. """

from django.contrib import admin

from .models import Question

# Register your models here.


admin.site.register(Question)
