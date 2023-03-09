from datacenter.models import Schoolkid, Mark
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)

    def handle(self, *args, **options):
        year_of_study = 6
        name = options.get('name')[0]
        try:
            child = Schoolkid.objects.get(full_name__contains=name, year_of_study=year_of_study)
            Mark.objects.filter(schoolkid=child, points__in=[2, 3]).update(points=5)
            return 'Finished!'
        except MultipleObjectsReturned:
            print('Returned more than 1 result. Aborting.')
        except ObjectDoesNotExist:
            print('Matching query does not exist. Aborting.')
    