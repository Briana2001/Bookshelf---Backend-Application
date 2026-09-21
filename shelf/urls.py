from django.urls import path
from . import views


app_name = 'shelf'
urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('book/add/', views.book_add, name='book_add'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]