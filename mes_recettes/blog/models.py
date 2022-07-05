from django.db import models

# Create your models here.
class Recette(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True)# non-mandatory field
    auteur = models.CharField(max_length=100)
    photo = models.CharField(max_length=250)
    date_parution = models.DateTimeField(auto_now_add=True, auto_now=False)#auto_now update everytime
    categorie = models.ForeignKey('Categorie', on_delete=models.PROTECT, null=True)
    member = models.ForeignKey('Member', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Member(models.Model):
    nom = models.CharField(max_length=100)
    pseudo = models.CharField(max_length=100)
    mdp = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    dateInscription = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.pseudo
    
class Ingredient(models.Model):
    nom = models.CharField(max_length=100)
    quantite = models.IntegerField()
    unit = models.CharField(max_length=2)
    recette = models.ForeignKey('Recette', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    auteur = models.CharField(max_length=100)
    contenu = models.CharField(max_length=1000)
    note = models.IntegerField()
    dateCreation = models.DateTimeField(auto_now_add=True, auto_now=False)
    recette = models.ForeignKey('Recette', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.auteur