from django.urls import path

from .views import  article_full_info, author_articles, article, article_details, author_form, article_form, comment_form

urlpatterns = [
path('author/<int:author_id>/', author_articles, name='author_articles'),
path('article/<int:article_id>/', article, name='article'),
path('article_details/<int:article_id>/', article_details, name='article_details'),
path('article_full_info/<int:article_id>/', article_full_info, name='article_full_info'),
path('add_author/', author_form, name='author_form'),
path('add_article/', article_form, name='article_form'),
path('add_comment/', comment_form, name='comment_form'),

]