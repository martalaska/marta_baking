from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingredients
from .models import Ingredients_Recipe

def home(request):
    return render(request, "home.html")

def website(request):
    ingred = Ingredients_Recipe.objects.all()
    return render(request, 'website.html', {'ingred': ingred})

def matches(request):
    # all_ing = Ingredients.objects.all()
    # for i in all_ing:
    #     for pair in getattr(i, "matches").split(", "):
    #         if not Ingredients.objects.filter(title_iexact = pair):
    #             Ingredients(title = pair, matches)


    search = request.GET.get('ingredient')
    ing = Ingredients.objects.filter(title__iexact = search)
    pairing = []
    if not ing:
        # for i in Ingredients.objects.all():
        #     if search in getattr(i, "matches"):
        #         pairing.append(getattr())
        # if pairing == []:
        pairing = "No match found"
    else:
        list_matches = ing.values()[0]
        for pair in list(list_matches.keys())[1:40]:
            if list_matches[pair] != "":
                pairing.append(list_matches[pair])
        #pairing = ing.values()[0]['matches'].split(", ")
        # for a in ing.values()[0].keys():
        #     if ing.values()[0][a] == 1:
        #         a = a.replace("_", " ")
        #         a = a[0].upper() + a[1:]
        #         pairing.append(a)
    # search = request.GET.get('ingredient')
    # pairing = []
    # if search in data.model:
    #     n = data.model["Grapefruit"].head.next
    #     while n.name1 != "":
    #         if n.name1 == search:
    #             pairing.append(n.name2)
    #         else: pairing.append(n.name1)
    #         n = n.next
    # else:
    #     pairing = "No match found"
    return render(request, 'matches.html', {'search': search, 'ing': pairing})





# Create your views here.
