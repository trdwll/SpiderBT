from django.contrib import admin

from SpiderBT_Users.models import (
    UserGroup
)

class UserGroupAdmin(admin.ModelAdmin):
    search_fields = ['title', 'is_staff']

admin.site.register(UserGroup, UserGroupAdmin)