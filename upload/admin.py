from django.contrib import admin

# Register your models here.
from .models import PhotoList,DocumentList

admin.site.register(PhotoList)
admin.site.register(DocumentList)
