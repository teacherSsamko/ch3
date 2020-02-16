from django.contrib import admin
from books.models import Book, Author, Publisher

# books/admin.py

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)

