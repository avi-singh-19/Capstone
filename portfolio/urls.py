from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('take_in_stock_price/', views.take_in_stock_price, name='take_in_stock_price'),
    path('professional_details/', views.professional_details, name='professional_details'),
    path('personal_interests', views.personal_interests, name='personal_interests'),
    path('wordle_game', views.wordle_game, name='wordle_game')
]
