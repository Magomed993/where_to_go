from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Наименование', max_length=200)
    short_description = models.TextField('Короткое описание')
    long_description = HTMLField('Длинное описание')
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Картинка')
    order = models.PositiveIntegerField(verbose_name='Позиция', default=0, db_index=True)

    def __str__(self):
        return f'{self.place.title} ({self.id})'

    class Meta:
        ordering = ['order']
        verbose_name = 'фото'
        verbose_name_plural = 'фотографии'
