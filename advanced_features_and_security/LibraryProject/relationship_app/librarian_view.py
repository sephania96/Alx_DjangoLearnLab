from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def librarian_view(request):
    if request.user.is_authenticated:
        return render(request, 'librarian.html')
    return render(request, 'access_denied.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

librarian_view = user_passes_test(is_librarian)(librarian_view)