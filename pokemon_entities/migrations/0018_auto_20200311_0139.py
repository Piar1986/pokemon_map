# Generated by Django 3.0.2 on 2020-03-10 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0017_auto_20200311_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_personality', to='pokemon_entities.Pokemon', verbose_name='Особь покемона'),
        ),
    ]
