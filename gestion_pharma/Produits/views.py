from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    #recuperer els valeurs de la bdd
    donnees = Produit.objects.all()

    context = {
        'donnees': donnees,
    }
    return render(request, 'home.html', context)