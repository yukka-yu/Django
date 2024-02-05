from django.urls import path
from . import views

urlpatterns = [
    path('', views.games, name='games'),
    path('head_tail/', views.head_tail, name='head_tail'),
    path('dice/', views.dice, name='dice'),
    path('rand/', views.rand, name='rand')
]