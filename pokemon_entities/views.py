import folium
import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponseNotFound
from django.shortcuts import render
from pokemon_entities.models import Pokemon
from pokemon_entities.models import PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons=Pokemon.objects.all()
    
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        pokemon_entities = PokemonEntity.objects.filter(pokemon__title_ru=pokemon.title_ru)
        for pokemon_entity in pokemon_entities:
            add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon, pokemon_entity.pokemon, 
                request.build_absolute_uri(pokemon.image.url))
    
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title_ru,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemon=Pokemon.objects.get(id=pokemon_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    except MultipleObjectsReturned:
        return HttpResponseNotFound('<h1>Найдено несколько покемонов</h1>')

    pokemon_photo_url = request.build_absolute_uri(pokemon.image.url)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(pokemon__id=pokemon.id)

    pokemon_entities_data = []
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon, 
            pokemon_entity.pokemon, pokemon_photo_url)
        pokemon_entities_data.append({
            "level": pokemon_entity.level,
            "lat": pokemon_entity.lat,
            "lon": pokemon_entity.lon
            })

    pokemon_data = {
        'pokemon_id': pokemon.id,
        'title_ru': pokemon.title_ru,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description' : pokemon.description,
        'img_url': pokemon_photo_url,
        'entities' : pokemon_entities_data
    }

    if pokemon.previous_evolution:
        pokemon_previous_evolution_photo_url = request.build_absolute_uri(pokemon.previous_evolution.image.url)
        pokemon_data['previous_evolution'] = {
            "title_ru": pokemon.previous_evolution.title_ru,
            "pokemon_id": pokemon.previous_evolution.id,
            "img_url": pokemon_previous_evolution_photo_url
            }
    
    pokemon_next_evolutions_count = pokemon.next_evolutions.all().count()
    if pokemon_next_evolutions_count:
        pokemon_next_evolution = pokemon.next_evolutions.all()[0]
        pokemon_next_evolution_photo_url = request.build_absolute_uri(pokemon_next_evolution.image.url)
        pokemon_data['next_evolution'] = {
            "title_ru": pokemon_next_evolution.title_ru,
            "pokemon_id": pokemon_next_evolution.id,
            "img_url": pokemon_next_evolution_photo_url
            }

    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon_data})