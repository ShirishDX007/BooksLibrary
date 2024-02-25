from django.urls import path
from .views import home, add_books

urlpatterns = [
    path('', home, name='home'),
    path('add_books/', add_books, name='add_books'),
]