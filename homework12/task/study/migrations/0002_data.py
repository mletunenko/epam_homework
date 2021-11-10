# Generated by Django 3.2.8 on 2021-10-25 14:42
import datetime

from django.db import migrations


def forwards_func(apps, schema_editor):
    Teacher = apps.get_model('study', 'Teacher')
    Teacher.objects.create(first_name='Daniil',
                           last_name='Shadrin')
    Teacher.objects.create(first_name='Aleksandr',
                           last_name='Smetanin')

    Student = apps.get_model('study', 'Student')
    lazy_student = Student.objects.create(first_name='Roman',
                                          last_name='Petrov')
    good_student = Student.objects.create(first_name='Lev',
                                          last_name='Sokolov')

    Homework = apps.get_model('study', 'Homework')
    oop_hw = Homework.objects.create(text='Learn OOP',
                                     deadline=datetime.timedelta(days=1))
    docs_hw = Homework.objects.create(text='Read docs',
                                      deadline=datetime.timedelta(days=5))

    HomeworkResult = apps.get_model('study', 'HomeworkResult')
    HomeworkResult.objects.create(homework=oop_hw,
                                  solution='I have done this hw',
                                  author=good_student)
    HomeworkResult.objects.create(homework=docs_hw,
                                  solution='I have done this too',
                                  author=good_student)
    HomeworkResult.objects.create(homework=docs_hw,
                                  solution='done',
                                  author=lazy_student)


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]