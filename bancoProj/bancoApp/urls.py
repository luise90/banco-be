from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name='Home'),
    path('newCustomer', views.newCustomer, name='newCustomer'),
    path('getAllCustomer', views.getAllCustomer, name='getAllCustomer'),
    path('getOneCustomer/<int:id>', views.getOneCustomer, name='getOneCustomer')
]