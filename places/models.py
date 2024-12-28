from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    short_description = models.TextField(
        verbose_name='Короткое описание',
        blank=True
    )
    long_description = HTMLField(
        verbose_name='Длинное описание',
        blank=True
    )
    lng = models.FloatField(
        verbose_name='Долгота'
    )
    lat = models.FloatField(
        verbose_name='Широта'
    )

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )
    img = models.ImageField(
        verbose_name='Картинки'
    )
    num = models.IntegerField(
        verbose_name='Позиция',
        default=0,
        db_index=True
    )

    class Meta:
        ordering = ['num']
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'

    def __str__(self):
        return f'{self.id} {self.place.title}'
