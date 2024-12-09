from modulefinder import Module

from django.db import models


class Place(models.Model):
    title = models.CharField('Наименование', max_length=200)
    short_description = models.TextField('Короткое описание')
    long_description = models.TextField('Длинное описание')
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
    order = models.PositiveIntegerField(verbose_name='Позиция', default=0)

    def __str__(self):
      return f'{self.id} - {self.place.title}'

    class Meta:
      ordering = ['order']
      verbose_name = 'фото'
      verbose_name_plural = 'фотографии'
