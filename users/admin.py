from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['email', 'username', 'is_staff']
    search_fields = ['email', 'username']
    ordering = ['email']
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('email',)}),
    )

admin.site.register(User, UserAdmin)
