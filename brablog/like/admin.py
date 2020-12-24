from django.contrib import admin

from .models import Like

class LikeAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "like") 
    empty_value_display = "-пусто-"

admin.site.register(Like, LikeAdmin)

