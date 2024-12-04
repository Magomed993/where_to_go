from django.db import models


class Post(models.Model):
    title = models.CharField('Наименование', max_length=200)
    text = models.TextField('Текст')

    def __str__(self):
      return self.title
