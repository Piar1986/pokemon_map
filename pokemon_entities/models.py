from django.db import models

class Pokemon(models.Model):
    '''Покемон.'''
    title_ru = models.CharField('Название на русском языке', max_length=200, blank=True)
    title_en = models.CharField('Название на английском языке', max_length=200, blank=True)
    title_jp = models.CharField('Название на японском языке', max_length=200, blank=True)
    image = models.ImageField('Картинка', blank=True)
    description = models.CharField('Описание', max_length=1000, blank=True)
    previous_evolution = models.ForeignKey('self', verbose_name='Из кого эволюционирует', null=True, blank=True, related_name='next_evolutions', on_delete=models.SET_NULL)

    def __str__(self):
        return '{}'.format(self.title_ru)

class PokemonEntity(models.Model):
    '''Сущность покемона.'''
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    pokemon = models.ForeignKey(Pokemon, verbose_name='Особь покемона', on_delete=models.CASCADE, related_name='pokemon_personality')
    appeared_at = models.DateTimeField('Время появления')
    disappeared_at = models.DateTimeField('Время исчезновения')
    level = models.IntegerField('Уровень', null=True)
    health = models.IntegerField('Здоровье', null=True)
    strength = models.IntegerField('Атака', null=True)
    defence = models.IntegerField('Защита', null=True)
    stamina = models.IntegerField('Выносливость', null=True)