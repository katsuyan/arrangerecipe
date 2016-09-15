from django.shortcuts import render
from django.http import HttpResponse


def book_list(request):
    return render(request, 'recipe/index.html')
