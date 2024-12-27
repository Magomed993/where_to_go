import requests
from django.core.exceptions import MultipleObjectsReturned
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Скачивание мест по url'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_json = response.json()
        try:
            place, created = Place.objects.get_or_create(
                title=place_json['title'],
                lng=place_json['coordinates']['lng'],
                lat=place_json['coordinates']['lat'],
                defaults={'description_short': place_json['description_short'],
                        'description_long': place_json['description_long'],
                        }
            )
        except MultipleObjectsReturned:
            print('Найдено несколько мест')

        for url in place_json['imgs']:
            img_response = requests.get(url)
            img_response.raise_for_status()
            image = Image(place=place)
            image_name = place.title
            image.img.save(image_name, ContentFile(img_response.content), save=True)
