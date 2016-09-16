from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction
from recipe.models import Taste, Category, Recipe
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import logging

logger = logging.getLogger(__name__)


def book_list(request):
    categories = Category.objects.all().order_by("id")
    tastes = Taste.objects.all().order_by("id")

    category_list = []
    for category in categories:
        category_data = {"id": category.id, "name": category.name}
        category_list.append(category_data)

    taste_list = []
    for taste in tastes:
        taste_data = {"id": taste.id, "name": taste.name}
        taste_list.append(taste_data)

    return render(request, 'recipe/index.html', {"category_list": category_list, "taste_list": taste_list})


def get_recipe_id(request):
    category_id = request.GET['category_id']
    taste_id = request.GET['taste_id']
    recipe = Recipe.objects.filter(taste_id=taste_id, category_id=category_id)
    data = {"id": recipe[0].id}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=200)

def detail(request, category_id=None, taste_id=None):
    recipes = Recipe.objects.filter(taste_id=taste_id, category_id=category_id)
    ids = []
    for recipe in recipes:
        ids.append(recipe.id)
    print(ids)
    data = {"ids": recipe}
    return render(request, 'recipe/detail.html', {"ids": ids})
