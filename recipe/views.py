from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction
from recipe.models import Taste, Category, Recipe
from django.views.decorators.csrf import ensure_csrf_cookie
import logging

logger = logging.getLogger(__name__)


def book_list(request):
    tastes = Taste.objects.all().order_by("id")
    categories = Category.objects.all().order_by("id")
    return render(request, 'recipe/index.html')
