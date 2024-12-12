from django.core.management.base import BaseCommand, CommandError
from catalog.models import Place


class Comand(BaseCommand):
    help = 'Closes the specified place for voting'

    def add_arguments(self, parser):
        parser.add_argument('place_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for place_id in options['place_ids']:
            try:
                place = Place.objects.get(pk=place_id)
            except Place.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % place_id)

            place.opened = False
            place.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % place_id))
