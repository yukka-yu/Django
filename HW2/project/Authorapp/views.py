from django.shortcuts import render, get_object_or_404
from .models import AuthorModel, ArticleModel, CommentModel

def author_articles(request, author_id):
    author = get_object_or_404(AuthorModel, pk=author_id)
    articles = ArticleModel.objects.filter(author=author)
    context = {'author':author, 'articles':articles}
    return render(request, 'Authorapp/author_articles.html', context)

def article(request, article_id):
    article = get_object_or_404(ArticleModel, pk=article_id)
    context = {'article': article}
    return render(request, 'Authorapp/article.html', context)

def article_details(request, article_id):
    article = get_object_or_404(ArticleModel, pk=article_id)
    article.views += 1
    article.save()
    context = {'article': article}
    return render(request, 'Authorapp/article_details.html', context)

def article_full_info(request, article_id):
    article = get_object_or_404(ArticleModel, pk=article_id)
    article.views += 1
    article.save()
    comments = CommentModel.objects.filter(article_id=article_id).order_by('pub_date')
    context = {'article': article, 'comments': comments}
    return render(request, 'Authorapp/article_full_info.html', context)

