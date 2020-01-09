import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models

# Create your views here.

context = { }

def home(request):
    return render (request, 'craiglist/base.html', context)


def new_search(request):
    search = request.POST.get('search')
    context = {'search':search}
    return render(request, 'craiglist/new_search.html', context)
