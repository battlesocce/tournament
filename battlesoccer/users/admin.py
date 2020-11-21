from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import CustomUser
from users.forms import CustomForm


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomForm
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('is_activated','is_team')}),
        ('Permissions', {'fields': ('is_active',)}),
        
    )
admin.site.register(CustomUser, CustomUserAdmin)
