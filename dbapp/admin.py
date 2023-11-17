from django.contrib import admin
from dbapp import models
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','bio','display_uploaded_file']

    def display_uploaded_file(self, obj):
        if obj.uploaded_file:
            return obj.uploaded_file.name
        return 'No File'

admin.site.register(models.cerere_de_finantare)
admin.site.register(models.UserProfile)