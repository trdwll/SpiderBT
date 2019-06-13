from django.contrib import admin
from django.urls import path

from SpiderBT_Cases.models import (
    Product, ProductVersion,
    Category,
    Case, CaseNote, CaseVote
)

from SpiderBT_Users.models import (
    UserGroup
)

class ProductVersionAdmin(admin.StackedInline):
    model = ProductVersion
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }
    filter_horizontal = ('usergroups', )
    search_fields = ['abbreviation', 'title', 'visibility']
    list_display = ['abbreviation', 'title', 'visibility']
    inlines = [ProductVersionAdmin, ]

    def save_model(self, request, obj, form, change):
        # TODO: Create the UserGroups for this product
        super(ProductAdmin, self).save_model(request, obj, form, change)

admin.site.register(Product, ProductAdmin)


class CaseAdmin(admin.ModelAdmin):
    filter_horizontal = ('assigned_to_user', 'assigned_to_group', 'affect_version', )
    search_fields = ['identifier', 'title', 'status', 'severity']
    list_display = ['identifier', 'title', 'status', 'severity']


admin.site.register(Case, CaseAdmin)

admin.site.register(Category)
admin.site.register(CaseNote)
admin.site.register(CaseVote)