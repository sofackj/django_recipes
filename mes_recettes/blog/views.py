from django.shortcuts import render
from django.http import HttpResponse
from . import data
from . import models

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {
        'recettes' : models.Recette.objects.all(),
        'categories' : models.Categorie.objects.all().order_by('nom')
        })

def recette(request, id_recette):
    
    my_recette = models.Recette.objects.get(pk=id_recette)
    
    return render(request, 'blog/recettes.html', {
        'recette' : my_recette,
        'categories' : models.Categorie.objects.all().order_by('nom'),
        'list_ingredients' : my_recette.ingredient_set.all(),
        'list_commentaires' : my_recette.commentaire_set.all(),
        })

def formulaire(request):
    return render(request, 'blog/formulaire.html', {})

def categorie(request, id_categorie):
    
    my_categorie = models.Categorie.objects.get(pk=id_categorie)
    
    return render(request, 'blog/categorie.html', {
        'list_recettes' : my_categorie.recette_set.all(),
        'selected_categorie' : my_categorie,
        'categories' : models.Categorie.objects.all().order_by('nom')
        })