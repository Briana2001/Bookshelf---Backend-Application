from django.contrib import admin
from .models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_at', 'status',)
    search_fields = ('title', 'author', 'isbn',)
    list_filter = ('published_at',)