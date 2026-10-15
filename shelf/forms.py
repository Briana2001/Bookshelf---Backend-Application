from django import forms
from .models import Book

# Reusable Tailwind class strings so styling stays consistent
INPUT_CLASSES = (
    "block w-full rounded-md border border-gray-300 bg-white px-3 py-2 mt-2 "
    "text-gray-900 placeholder-gray-400 shadow-sm "
    "focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500 focus:outline-none "
    "sm:text-sm"
)

TEXTAREA_CLASSES = INPUT_CLASSES + " resize-y"

SELECT_CLASSES = (
    "block w-full rounded-md border border-gray-300 bg-white px-3 py-2 mt-2"
    "text-gray-900 shadow-sm "
    "focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500 focus:outline-none "
    "sm:text-sm"
)

FILE_CLASSES = (
    "block w-full text-sm text-gray-900 mt-2"
    "file:mr-4 file:rounded-md file:border-0 "
    "file:bg-indigo-50 file:px-4 file:py-2 "
    "file:text-sm file:font-semibold file:text-indigo-700 "
    "hover:file:bg-indigo-100"
)



class BookForm(forms.ModelForm):
    class Meta:
      model = Book
      fields = ['title', 'author', 'description', 'status', 'isbn']
      widgets = {
        'title': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter book title'}),
        'author': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter author name'}),
        'description': forms.Textarea(attrs={'class': TEXTAREA_CLASSES, 'placeholder': 'Enter book description'}),
        'status': forms.Select(attrs={'class': SELECT_CLASSES}),
        'isbn': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter ISBN'}),
      }