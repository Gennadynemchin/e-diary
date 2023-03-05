from datacenter.models import *
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)

    def handle(self, *args, **options):
        year_of_study = 6
        name = options.get('name')
        try:
            child = Schoolkid.objects.get(full_name__contains=name, year_of_study=year_of_study)
            marks = Mark.objects.filter(schoolkid=child)
            bad_points = marks.filter(points__in=[2, 3])
            for bad_point in bad_points:
                bad_point.points = 5
                bad_point.save()
        except MultipleObjectsReturned:
            print('Returned more than 1 result. Aborting.')
        except ObjectDoesNotExist:
            print('Matching query does not exist. Aborting.')
        return
    