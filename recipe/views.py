from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction
from recipe.models import Taste, Category, Recipe
from django.views.decorators.csrf import ensure_csrf_cookie
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
    recipe = Recipe.objects.filter(taste_id='1', category_id='1')
    logger.error(recipe)
    pass
