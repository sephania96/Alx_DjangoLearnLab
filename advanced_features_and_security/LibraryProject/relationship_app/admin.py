from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, CustomUser

class UserProfileAdmin(UserAdmin):
    

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['role'].choices = [(role, role) for role in ['Admin', 'Librarian', 'Member']]
        return form

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo'),
        }),
    )

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
