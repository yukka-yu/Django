from django.db import models

# Создайте модель Автор. Модель должна содержать следующие поля: ○ имя до 100 символов ○ фамилия до 100 символов ○ почта ○ биография ○ день рождения. Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.

# Создайте модель Статья (публикация). Авторы из прошлой задачи могут писать статьи. У статьи может быть только один автор. У статьи должны быть следующие обязательные поля: ○ заголовок статьи с максимальной длиной 200 символов ○ содержание статьи ○ дата публикации статьи ○ автор статьи с удалением связанных объектов при удалении автора ○ категория статьи с максимальной длиной 100 символов ○ количество просмотров статьи со значением по умолчанию 0 ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False
    
#Создайте модель Комментарий. Авторы могут добавлять комментарии к своим и чужим статьям. Т.е. у комментария может быть один автор. И комментарий относится к одной статье. У модели должны быть следующие поля ○ автор ○ статья ○ комментарий ○ дата создания ○ дата изменения

class AuthorModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email  = models.EmailField()
    bio = models.TextField()
    birthdate = models.DateField()
    fullname = models.CharField(blank=True, null=True, max_length=201)

    def save (self, *args, **kwargs) :    
        self.fullname = self.name + ' ' + self.surname
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.fullname}'
    

    
class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    cathegory = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Article title is {self.title}, cathegory {self.cathegory}'



class CommentModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.text}'
    
