from django.contrib import admin
from .models import Book, Book_itself, Authors

# Register your models here.
admin.site.register(Book)
admin.site.register(Book_itself)
admin.site.register(Authors)

