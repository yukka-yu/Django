from django.core.management.base import BaseCommand
from Authorapp.models import AuthorModel, ArticleModel, CommentModel

class Command(BaseCommand):
    help = "Create fake authors for tests."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Authors amount')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = AuthorModel(name=f'Name{i}', surname=f'Surname{i}', email=f'mail{i}@mail.ru', bio=f'was born in town{i}', birthdate='1934-10-08')
            author.save()
            for j in range(1, count + 1):
                article = ArticleModel(title=f'Title{j}', content=f'{j} bla bla bla many long text of author {j}', author=author, cathegory=f'cathegory #{j}', views=j, is_published=True)
                article.save()
                comment = CommentModel(author = author, article = article, text=f'nontoxic comment text {j}')
                comment.save()