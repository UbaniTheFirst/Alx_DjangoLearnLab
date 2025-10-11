from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book


class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for CustomUser model.
    Extends UserAdmin to include additional fields.
    """
    model = CustomUser
    
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)