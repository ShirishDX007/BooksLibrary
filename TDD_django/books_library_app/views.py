from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddBookForm
from .models import Catalogue



# Create your views here.
def home(request):

    books = Catalogue.objects.all()
    context = {'books':books}

    return render(request, 'home.html', context)
   
def add_books(request):

    add_book_form = AddBookForm()

    #Save the new book to books Catalogue
    if request.method == 'POST':
        add_book_form = AddBookForm(data=request.POST)
        
        #check if the form is valid
        if add_book_form.is_valid():
            add_book_form.save()
    #print statement for debugging
    #print("Add_books view - add_book_form instance:", add_book_form)
    

    return render(request, 'add_books.html', {'add_book_form': add_book_form})





    
