from datacenter.models import Schoolkid, Subject, Commendation, Lesson
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.core.management.base import BaseCommand
import random

COMMENDATIONS = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
                 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!',
                 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!',
                 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!',
                 'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!',
                 'С каждым разом у тебя получается всё лучше!',
                 'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
                 'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!',
                 'Капитальный красавчик!']


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)
        parser.add_argument('subject', nargs='+', type=str)

    def handle(self, *args, **options):
        name = options.get('name')[0]
        subject = options.get('subject')[0]
        text = str(random.choice(COMMENDATIONS))

        try:
            child = Schoolkid.objects.get(full_name__contains=name)
            year_of_study = child.year_of_study
            group_letter = child.group_letter
            subject = Subject.objects.get(title__contains=subject, year_of_study=year_of_study)
            lessons = Lesson.objects.filter(year_of_study=year_of_study,
                                            subject=subject,
                                            group_letter=group_letter).order_by('-date').first()
            last_lesson_date = lessons.date
            teacher = lessons.teacher
            Commendation.objects.create(text=text,
                                        created=last_lesson_date,
                                        schoolkid=child,
                                        subject=subject,
                                        teacher=teacher)
            return 'Finished!'
        except Schoolkid.MultipleObjectsReturned:
            print('Returned more than 1 result. Aborting.')
        except Schoolkid.DoesNotExist:
            print('Matching query does not exist. Aborting.')
        except Subject.DoesNotExist:
            print('Looks like you have entered the wrong subject. Please double check. Aborting.')
