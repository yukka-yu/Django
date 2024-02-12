from django.core.management.base import BaseCommand
from Authorapp.models import AuthorModel, ArticleModel, CommentModel

class Command(BaseCommand):
    help = "Create fake comments."

    def handle(self, *args, **kwargs):
        authors = AuthorModel.objects.all()
        articles = ArticleModel.objects.all()
        for author in authors:
            for article in articles:
                if article.author != author:
                    comment = CommentModel(author=author, article=article, text=f'One more nontoxic comment #{author.id}')
                    comment.save()

