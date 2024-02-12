import datetime
from django.core.management.base import BaseCommand
from Authorapp.models import AuthorModel, ArticleModel, CommentModel

class Command(BaseCommand):
    help = "Update comment by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_comment = 'new comment text after changes'
        comment = CommentModel.objects.filter(pk=pk).first()
        comment.text = new_comment
        comment.change_date = '2024-02-12' #datetime.date.today()
        comment.save()
        