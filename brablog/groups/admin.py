from django.contrib import admin

from .models import Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "desc") 
    search_fields = ("title",) 
    empty_value_display = "-пусто-"

admin.site.register(Group, GroupAdmin)
