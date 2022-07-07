from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import data
from . import models
from .forms import InscriptionForm, CommentaireForm, ConnexionForm
from django.contrib.auth.hashers import make_password, check_password# make password safer
from django.db.models import Avg
from math import floor


# Create your views here.
def index(request):   
    # save session in a variable
    member = None
    member_id = request.session.get('member_id')
    if (member_id):
        member = models.Member.objects.get(pk=member_id)
        
    return render(request, 'blog/index.html', {
        'recettes' : models.Recette.objects.all(),
        'categories' : models.Categorie.objects.all().order_by('nom'),
        'member' : member,
        })

def recette(request, id_recette):
    
    # save session in a variable
    member = None
    member_id = request.session.get('member_id')
    if (member_id):
        member = models.Member.objects.get(pk=member_id)
    
    my_recette = models.Recette.objects.get(pk=id_recette)
    
    if (request.method == 'POST'):
        
        form = CommentaireForm(request.POST)
        
        if form.is_valid():
            auteur = form.cleaned_data['auteur']
            commentaire = form.cleaned_data['commentaire']
            note = form.cleaned_data['note']
            
            commentaire = models.Commentaire(auteur=auteur, contenu=commentaire, note=note, recette_id=id_recette)
            commentaire.save()
            
    else:
        form = CommentaireForm()
        
    note = floor(my_recette.commentaire_set.all().aggregate(Avg('note'))['note__avg'])
    table_note = [i <= note for i in range(1, 6)]
    
    return render(request, 'blog/recettes.html', {
        'recette' : my_recette,
        'categories' : models.Categorie.objects.all().order_by('nom'),
        'list_ingredients' : my_recette.ingredient_set.all(),
        'list_commentaires' : my_recette.commentaire_set.all(),
        'member' : member,
        'form' : form,
        'notes' : table_note,
        })

def formulaire(request):
    
    if (request.method == 'POST'):
        
        form = InscriptionForm(request.POST)
        
        if form.is_valid():
            nom = form.cleaned_data['nom']
            pseudo = form.cleaned_data['pseudo']
            email = form.cleaned_data['email']
            mdp = form.cleaned_data['mdp']
            
            # Encrypt the password
            mdp_encoded = make_password(mdp)
            
            member = models.Member(nom = nom,
                            pseudo = pseudo,
                            email = email,
                            mdp = mdp_encoded)
            member.save()
            
            request.session['member_id'] = member.id
            
            return redirect('index')
    else:
        form = InscriptionForm()
    
    return render(request, 'blog/formulaire.html', {'form' : form})

def categorie(request, id_categorie):
    
    my_categorie = models.Categorie.objects.get(pk=id_categorie)
    
    return render(request, 'blog/categorie.html', {
        'list_recettes' : my_categorie.recette_set.all(),
        'selected_categorie' : my_categorie,
        'categories' : models.Categorie.objects.all().order_by('nom')
        })

def connexion(request):
    if (request.method == 'POST'):
        
        form = ConnexionForm(request.POST)
        
        if form.is_valid():
            pseudo = form.cleaned_data['pseudo']
            mdp = form.cleaned_data['mdp']
            
            try:
                member = models.Member.objects.get(pseudo=pseudo)
            except models.Member.DoesNotExist:
                form.errors['__all__'] = form.error_class(['aieaieaieaie'])
            else:
                if check_password(mdp, member.mdp):
                    request.session['member_id'] = member.id
                    return redirect('index')
                else:
                    form.errors['__all__'] = form.error_class(['aieaieaieaie'])
    else:
        form = ConnexionForm()
    return render(request, 'blog/connexion.html', {'form' : form})

def deconnexion(request):
    request.session.clear()
    return redirect(index)