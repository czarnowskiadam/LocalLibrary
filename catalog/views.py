from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_books_with_the = Book.objects.filter(title__contains='the').count()
    
    num_instances = BookInstance.objects.all().count()   
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    num_authors = Author.objects.count()
    
    num_genres_with_politic = Genre.objects.filter(name__contains="politic").count()
    
    context = {
        'num_books': num_books,
        'num_books_with_the': num_books_with_the,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_with_politic': num_genres_with_politic,
    }
    
    return render(request, 'index.html', context=context)