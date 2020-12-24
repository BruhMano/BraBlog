from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    list_display = ("username", "first_name", "last_name", "image","email") 
    search_fields = ("username",)  
    empty_value_display = "-пусто-"
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('image','desc')}),
    )


admin.site.register(User, MyUserAdmin)

