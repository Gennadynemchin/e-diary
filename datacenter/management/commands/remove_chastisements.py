from datacenter.models import Schoolkid, Chastisement
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)

    def handle(self, *args, **options):
        name = options.get('name')[0]
        try:
            child = Schoolkid.objects.get(full_name__contains=name)
            child_chastisements = Chastisement.objects.filter(schoolkid=child)
            child_chastisements.delete()
            return 'Finished!'
        except Schoolkid.MultipleObjectsReturned:
            print('Returned more than 1 result. Aborting.')
        except Schoolkid.DoesNotExist:
            print('Matching query does not exist. Aborting.')
