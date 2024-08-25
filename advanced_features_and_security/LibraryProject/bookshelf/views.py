from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.db.models import Q
from .models import Book, UserProfile
from .forms import ExampleForm

def book_list(request):
    search = request.GET.get('search', '')
    books = Book.objects.filter(Q(title__icontains=search) | Q(author__icontains=search))
    return render(request, 'book_list.html', {'books': books})

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'create_book.html', {'form': form})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return render(request, '404.html')
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('book_list')
    except Book.DoesNotExist:
        return render(request, '404.html')