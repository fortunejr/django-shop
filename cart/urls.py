from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='home'),
    path('index/<int:id>', views.index, name='index'),
]
