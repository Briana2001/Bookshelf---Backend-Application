from django.urls import path
from . import views


app_name = 'shelf'
urlpatterns = [
    path('', views.home, name='home'),
    
]