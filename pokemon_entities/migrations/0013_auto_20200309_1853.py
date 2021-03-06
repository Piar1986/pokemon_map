# Generated by Django 3.0.2 on 2020-03-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20200309_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.CharField(max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Название на английском языке'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(max_length=200, null=True, verbose_name='Название на японском языке'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Название на русском языке'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(verbose_name='Время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(verbose_name='Время исчезновения'),
        ),
    ]
