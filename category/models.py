from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=233,
                                     verbose_name='Жанры')

    def __str__(self):
        return f'{self.category_name}'


class TVShow(models.Model):
    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'

    title = models.CharField(max_length=233,
                             verbose_name='Название сериала')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата обновления')
    image = models.ImageField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, related_name='shows')


class Comment(models.Model):
    text = models.TextField()
    shows = models.ForeignKey(TVShow,
                              on_delete=models.CASCADE, related_name='comments')
