from django.contrib import admin
from .models import imageModel

class imageAdmin(admin.ModelAdmin):
    list_display=["imageName","image","date"]
admin.site.register(imageModel,imageAdmin)