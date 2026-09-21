from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
  return render(request, 'shelf/home.html')

def book_add(request):
  return render(request, 'shelf/book_add.html')
 
def books(request):
  return render(request, 'shelf/books.html')

def book_detail(request, pk):
  return render(request, 'shelf/book_detail.html')

def book_edit(request, pk):
  return render(request, 'shelf/book_edit.html')

def book_delete(request, pk):
  return render(request, 'shelf/book_delete.html')
