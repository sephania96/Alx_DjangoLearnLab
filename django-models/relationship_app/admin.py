from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class UserProfileAdmin(UserAdmin):
    

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['role'].choices = [(role, role) for role in ['Admin', 'Librarian', 'Member']]
        return form

admin.site.register(UserProfile, UserProfileAdmin)

