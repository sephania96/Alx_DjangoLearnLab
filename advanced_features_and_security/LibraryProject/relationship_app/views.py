from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

def list_books(request):
    books = Book.objects.all()
    return render(request, 'templates/relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'templates/relationship_app/library_detail.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'templates/relationship_app/register.html', {'form': form})

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.userprofile.role == 'Admin':
            return view_func(request, *args, **kwargs)
        return redirect('login')  # or any other page you want to redirect to
    return wrapper

@permission_required('relationship_app.is_admin')
@admin_required
def admin_view(request):
    return render(request, 'templates/relationship_app/admin_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'templates/relationship_app/admin_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'templates/relationship_app/librarian_view.html')

@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'templates/relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        # Add book logic here
        return redirect('book_list')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # Edit book logic here
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # Delete book logic here
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})