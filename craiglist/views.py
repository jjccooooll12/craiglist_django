from django.shortcuts import render

# Create your views here.

context = { }

def home(request):
    return render (request, 'craiglist/base.html', context)
