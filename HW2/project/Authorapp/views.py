from django.shortcuts import redirect, render, get_object_or_404
from .models import AuthorModel, ArticleModel, CommentModel
from .forms import ArticleForm, AuthorForm, AddCommentForm, CommentForm

def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Authorapp/author_form.html', {'form': AuthorForm()})
        else: 
            return render(request, 'Authorapp/author_form.html', {'form': form})
    else: 
        return render(request, 'Authorapp/author_form.html', {'form': AuthorForm()})
    
def article_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Authorapp/article_form.html', {'form': ArticleForm()})
        else: 
            return render(request, 'Authorapp/article_form.html', {'form': form})
    else: 
        return render(request, 'Authorapp/article_form.html', {'form': ArticleForm()})
    
def comment_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Authorapp/comment_form.html', {'form': CommentForm()})
        else: 
            return render(request, 'Authorapp/comment_form.html', {'form': form})
    else: 
        return render(request, 'Authorapp/comment_form.html', {'form': CommentForm()})


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

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article_id = article_id
            new_comment.save()
        else: 
            form = AddCommentForm()
    else: 
        form = AddCommentForm()
    comments = CommentModel.objects.filter(article_id=article_id).order_by('pub_date')
    context = {'article': article, 'comments': comments, 'form': form}
    return render(request, 'Authorapp/article_full_info.html', context)



