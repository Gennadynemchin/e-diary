from datacenter.models import *
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)
        parser.add_argument('subject', nargs='+', type=str)

    def handle(self, *args, **options):
        year_of_study = 6
        name = options.get('name')
        subject = options.get('subject')
        commendations = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                         'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
                         'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!',
                         'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!',
                         'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!',
                         'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!',
                         'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
                         'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!', 'Капитальный красавчик!']
        year_of_study = 6
        group_letter = 'А'
        text = str(random.choice(commendations))

        try:
            child = Schoolkid.objects.get(full_name__contains=name, year_of_study=year_of_study)
            subject = Subject.objects.filter(title__contains=subject, year_of_study=year_of_study).first()
            lesson = Lesson.objects.filter(year_of_study=year_of_study, subject=subject, group_letter=group_letter)
            last_lesson_date = str(lesson.order_by('-date').first().date)
            teacher = lesson.first().teacher

            Commendation.objects.create(text=text,
                                        created=last_lesson_date,
                                        schoolkid=child,
                                        subject=subject,
                                        teacher=teacher)
            print('Created!')
        except MultipleObjectsReturned:
            print('Returned more than 1 result. Aborting.')
        except ObjectDoesNotExist:
            print('Matching query does not exist. Aborting.')
        return