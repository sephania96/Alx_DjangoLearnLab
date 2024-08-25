from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def member_view(request):
    if request.user.is_authenticated:
        return render(request, 'member.html')
    return render(request, 'access_denied.html')

def is_member(user):
    return user.userprofile.role == 'Member'

member_view = user_passes_test(is_member)(member_view)