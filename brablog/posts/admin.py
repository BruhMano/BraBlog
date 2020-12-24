from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "pub_date", "author","is_liked_by_current_user","likes") 
    search_fields = ("text",) 
    list_filter = ("pub_date",) 
    empty_value_display = "-пусто-"

admin.site.register(Post, PostAdmin)

