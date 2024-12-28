import sys
import time

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
        time_out = 5

        for url in urls:
            try:
                response = requests.get(url, timeout=time_out)
                response.raise_for_status()
                raw_place = response.json()
                place, created = Place.objects.get_or_create(
                    title=raw_place['title'],
                    lng=raw_place['coordinates']['lng'],
                    lat=raw_place['coordinates']['lat'],
                    defaults={
                        'short_description': raw_place['description_short'],
                        'long_description': raw_place['description_long'],
                    }
                )

                if not created:
                    print('Место уже имеется')
                    continue

                for link in raw_place['imgs']:
                    img_response = requests.get(link)
                    img_response.raise_for_status()
                    Image.objects.create(
                        place=place,
                        img=ContentFile(img_response.content, place.title)
                    )

            except MultipleObjectsReturned:
                print('Найдено несколько мест')
            except requests.exceptions.ConnectionError:
                print(
                    'Соединение прервано. Скрипт продолжает работу',
                    file=sys.stderr
                )
                time.sleep(20)
            except requests.exceptions.HTTPError as error:
                print(
                    f'Не корректно введен url: {error}',
                    file=sys.stderr
                )
                continue
            except requests.exceptions.ReadTimeout:
                continue
