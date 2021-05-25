# Generated by Django 3.1.6 on 2021-02-16 14:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('age', models.PositiveIntegerField(default=0, verbose_name='Wiek')),
                ('description', models.TextField(verbose_name='Opis')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Obrazek')),
            ],
            options={
                'verbose_name': 'Aktorzy i reżyserzy',
                'verbose_name_plural': 'Aktorzy i reżyserzy',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Kategoria')),
                ('description', models.TextField(verbose_name='Opis')),
                ('url', models.SlugField(max_length=160)),
            ],
            options={
                'verbose_name': 'Karegoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('description', models.TextField(verbose_name='Opis')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Gatunek',
                'verbose_name_plural': 'Gatunki',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Slogan')),
                ('description', models.TextField(verbose_name='Opis')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Plakat')),
                ('year', models.PositiveIntegerField(default=2021, verbose_name='Data wydania')),
                ('country', models.CharField(max_length=30, verbose_name='Kraj')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Światowa premiera')),
                ('budget', models.PositiveIntegerField(default=0, help_text='podać kwotę w złotych', verbose_name='Budżet')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='podać kwotę w złotych', verbose_name='Opłaty w USA')),
                ('fess_in_world', models.PositiveIntegerField(default=0, help_text='podać kwotę w złotych', verbose_name='Opłaty na całym świecie')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Wersja robocza')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='aktorzy')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Kategoria')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='producent')),
                ('genres', models.ManyToManyField(to='movies.Genre', verbose_name='gatunek')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmy',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0, verbose_name='Wartość')),
            ],
            options={
                'verbose_name': 'Gwiazdka oceny',
                'verbose_name_plural': 'Gwiazdka oceny',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa')),
                ('text', models.TextField(max_length=5000, verbose_name='Wiadomość')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='film')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.reviews', verbose_name='Rodzic')),
            ],
            options={
                'verbose_name': 'Opinia',
                'verbose_name_plural': 'Opinie',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP adres')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.movie', verbose_name='film')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.ratingstar', verbose_name='gwiazda')),
            ],
            options={
                'verbose_name': 'Ocena',
                'verbose_name_plural': 'Oceny',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Tytuł')),
                ('description', models.TextField(verbose_name='Opis')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Obrazek')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Film')),
            ],
            options={
                'verbose_name': 'Kadr z filmu',
                'verbose_name_plural': 'Kadry z filmu',
            },
        ),
    ]
