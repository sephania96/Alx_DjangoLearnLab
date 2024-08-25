from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def admin_view(request):
    if request.user.is_authenticated:
        return render(request, 'admin.html')
    return render(request, 'access_denied.html')

def is_admin(user):
    return user.userprofile.role == 'Admin'

admin_view = user_passes_test(is_admin)(admin_view)