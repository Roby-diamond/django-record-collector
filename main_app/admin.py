from django.contrib import admin
from .models import Record, Market, Genre

# Register your models here.

admin.site.register(Record)
admin.site.register(Market)
admin.site.register(Genre)