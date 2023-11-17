from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from dbapp import models
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','bio','display_uploaded_file']

    def display_uploaded_file(self, obj):
        if obj.uploaded_file:
            file_url = reverse('admin:dbapp_userprofile_change', args=[obj.id])
            return format_html('<a href="{}">View on site</a>', file_url)
        return 'NU avem'

    display_uploaded_file.short_description = 'Uploaded File'

admin.site.register(models.cerere_de_finantare)
admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Sesiune)
