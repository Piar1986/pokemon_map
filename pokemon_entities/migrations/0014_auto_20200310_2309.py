# Generated by Django 3.0.2 on 2020-03-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20200309_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.CharField(max_length=1000, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(max_length=200, default='', verbose_name='Название на английском языке'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(max_length=200, default='', verbose_name='Название на японском языке'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(max_length=200, default='', verbose_name='Название на русском языке'),
        ),
    ]
