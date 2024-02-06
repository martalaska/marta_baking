from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingredients

def home(request):
    return render(request, "home.html")

def website(request):
    return render(request, 'website.html')

def matches(request):
    search = request.GET.get('ingredient')
    ing = Ingredients.objects.filter(title__iexact = search)
    pairing = []
    if not ing:
        pairing = "No match found"
    else:
        for a in ing.values()[0].keys():
            if ing.values()[0][a] == 1:
                a = a.replace("_", " ")
                a = a[0].upper() + a[1:]
                pairing.append(a)
    return render(request, 'matches.html', {'search': search, 'ing': pairing})

# Create your views here.
