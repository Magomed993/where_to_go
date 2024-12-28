import requests
from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Скачивание мест по url'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='+',
            type=str,
            help='Список url адресов для загрузки данных'
        )

    def handle(self, *args, **options):
        urls = options['url']
        for url in urls:
            response = requests.get(url)
            response.raise_for_status()
            raw_place = response.json()
            try:
                place, created = Place.objects.get_or_create(
                    title=raw_place['title'],
                    lng=raw_place['coordinates']['lng'],
                    lat=raw_place['coordinates']['lat'],
                    defaults={
                        'short_description': raw_place['description_short'],
                        'long_description': raw_place['description_long'],
                    }
                )
            except MultipleObjectsReturned:
                print('Найдено несколько мест')

            for link in raw_place['imgs']:
                img_response = requests.get(link)
                img_response.raise_for_status()
                image = Image(place=place)
                image_name = place.title
                image.img.save(
                    image_name,
                    ContentFile(img_response.content),
                    save=True
                )
