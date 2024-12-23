from django.db import models


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(verbose_name='Картинки')
    num = models.IntegerField(verbose_name='Номер', default=0)

    def __str__(self):
        return f'{self.id} {self.place.title}'

    class Meta:
        ordering = ['-num']
        verbose_name = 'картинка'
        verbose_name_plural = 'картинки'