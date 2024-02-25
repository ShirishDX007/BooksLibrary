from django.test import TestCase, SimpleTestCase
from .models import Catalogue
from django.urls import reverse
from django.urls.base import resolve
from .forms import AddBookForm
from .views import home, add_books

# Create your tests here.

class CatalogueViewstests(TestCase):
    "Tests the views for the Catalogue"

    def test_book_list_view(self):
        """ Test method to show that the book we created are listed correctly."""
        Book_1 = Catalogue.objects.create(
            title = 'Automate the boring stuff using Python',
            ISBN = '978-1-60309-025-3',
            author = 'AI Sweigart',
            price = '459.99',
            availability = 'True',

        )
        Book_2 = Catalogue.objects.create(
            title = 'Fluent Python',
            ISBN = '978-1-60309-025-4',
            author = 'David Ascher',
            price = '999.9',
            availability = 'True',

        )

        response = self.client.get(reverse('home'))

        self.assertIn('Fluent Python', response.content.decode())
        self.assertIn('David Ascher', response.content.decode())
        self.assertIn('978-1-60309-025-4', response.content.decode())

class CatalogueTemplateTests(TestCase):
    """ Tests the template for the Catalogue model """
    def test_homepage_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_add_books_template(self):
        response = self.client.get(reverse('add_books'))
        self.assertTemplateUsed(response, 'add_books.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Welcome to the Books Library')

    def test_hompage_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'Hello World')

class CatalogueFormTest(TestCase):
    """ Tests the form for the Catalogue model """

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # def test_book_form(self):
    #     add_book_form = AddBookForm()
    #     add_book_form = self.response.context.get('add_book_form')
    #     self.assertIsInstance(add_book_form, AddBookForm)
    #     self.assertContains(self.response, 'csrfmiddlewaretoken')
        
    # def test_bootstrap_class_used_for_default_styling(self):
    #     add_book_form = self.response.context.get('add_book_form')
    #     self.assertIn('form-control', add_book_form.as_p())

    def test_book_form_validate_for_blank_items(self):
        add_book_form = AddBookForm(
            data={'title': '', 'ISBN': '', 'author': '', 'price': '', 'availability': ''}
        )
        self.assertFalse(add_book_form.is_valid())


class bookslibraryURLstest(SimpleTestCase):
    """ Tests the urls for the bookslibrary app """
    databases = ['default']

    def test_home_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_root_url_to_resolve_to_home_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)
        
class CatalogueModelTests(TestCase):

    """ Tests the Catalogue model """
    def setUp(self):
        self.book = Catalogue(
            title = 'First Title',
            ISBN = '978-3-16-148410-0',
            author = 'Samuel Torimiro',
            price = '9.99',
            availability = 'True'
        )

    def test_create_book(self):
        self.assertIsInstance(self.book, Catalogue)

    def test_str_representation(self):
        self.assertEqual(str(self.book), 'First Title')

    def test_saving_and_retrieving_books(self):
        first_book = Catalogue()
        first_book.title = 'First Title'
        first_book.ISBN = '978-3-16-148410-0'
        first_book.author = 'First Author'
        first_book.price = '9.99'
        first_book.availability = 'True'
        first_book.save()

        second_book = Catalogue()
        second_book.title = 'Second Title'
        second_book.ISBN = '978-3-16-148410-1'
        second_book.author = 'Second Author'
        second_book.price = '19.99'
        second_book.availability = 'False'
        second_book.save()

        saved_books = Catalogue.objects.all()
        self.assertEqual(saved_books.count(), 2)

        first_saved_book = saved_books[0]
        second_saved_book = saved_books[1]
        self.assertEqual(first_saved_book.title, 'First Title')
        self.assertEqual(second_saved_book.title, 'Second Title')

