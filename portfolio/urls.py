from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('take_in_stock_price/', views.take_in_stock_price, name='take_in_stock_price'),
]
