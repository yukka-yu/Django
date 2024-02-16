from django import forms
from .models import AuthorModel, ArticleModel, CommentModel
# Создайте форму для добавления нового автора в базу данных.

class AuthorForm(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['name', 'surname', 'email', 'bio', 'birthdate']

        widgets = {
            'birthdate': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
                }
        
class ArticleForm(forms.ModelForm):

    class Meta:
        model = ArticleModel
        fields = ['title', 'content', 'author', 'cathegory', 'is_published']
   

class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['author', 'article', 'text']

class AddCommentForm(forms.ModelForm):
    
    class Meta:
        model = CommentModel
        fields = ['author', 'text']
