import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает места в формате json в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='url')

    @staticmethod
    def upload_pictures(place, imgs_urls):
        for num, img in enumerate(imgs_urls):
            response = requests.get(img)
            response.raise_for_status()
            Image.objects.create(place=place,
                                 image=ContentFile(response.content, str(num)))

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        file_format = response.json()
        try:
            place, created = Place.objects.get_or_create(title=file_format['title'],
                                short_description=file_format['description_short'],
                                long_description=file_format['description_long'],
                                lng=file_format['coordinates']['lng'],
                                lat=file_format['coordinates']['lat'])
            if not created and place:
                place.images.all().delete()
            self.upload_pictures(place, file_format['imgs'])
        except Place.MultipleObjectsReturned:
            print('Данное месте уже имеется')
