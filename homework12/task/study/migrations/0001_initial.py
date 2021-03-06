# Generated by Django 3.2.8 on 2021-10-25 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('text', models.CharField(db_index=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('last_name', models.CharField(db_index=True, max_length=50)),
                ('first_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('last_name', models.CharField(db_index=True, max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('homework_done', models.ManyToManyField(to='study.Homework')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeworkResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('solution', models.CharField(db_index=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='study.student')),
                ('homework', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='study.homework')),
            ],
        ),
    ]
