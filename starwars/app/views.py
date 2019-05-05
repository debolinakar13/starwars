import requests

from django.shortcuts import render
from django.http import JsonResponse

from starwars import planets, films
from .models import Favourites

def search_planet(request, title):
    title = title.lower()
    try:
        return JsonResponse({'success': True, 'result':planets[title]})
    except:
        return JsonResponse({'success': False, 'result': 'not found'})

def list_planet(request):
    items = planets.keys()
    if request.method == "POST":
        items_to_add = request.POST.get('add_items')
        items_to_add = items_to_add.replace('add', '').replace('to favourite', '').strip()
        obj = Favourites.objects.create(title=items_to_add)
        obj.save()
    item_in_favourite = Favourites.objects.values_list('title',flat=True)
    items = set(items) - set(item_in_favourite)
    return render(request, 'planet.html', {'data':items})

def list_film(request):
    items = films.keys()
    if request.method == "POST":
        items_to_add = request.POST.get('add_items')
        items_to_add = items_to_add.replace('add', '').replace('to favourite', '').strip()
        obj = Favourites.objects.create(title=items_to_add)
        obj.save()
        item_in_favourite = Favourites.objects.values_list('title',flat=True)
        items = set(items) - set(item_in_favourite)
    return render(request, 'planet.html', {'data':items})
