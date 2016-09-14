from django.shortcuts import render
from django.http import HttpResponse


def book_list(request):
    """書籍の一覧"""
    return HttpResponse('書籍の一覧')
