from django.urls import path

from .views import article_full_info, author_articles, article, article_details

urlpatterns = [
path('author/<int:author_id>/', author_articles, name='author_articles'),
path('article/<int:article_id>/', article, name='article'),
path('article_details/<int:article_id>/', article_details, name='article_details'),
path('article_full_info/<int:article_id>/', article_full_info, name='article_full_info'),
]