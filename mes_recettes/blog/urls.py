from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('recette/<id_recette>', views.recette, name='recette'),
    path('formulaire', views.formulaire, name='formulaire'),
    path('categorie/<str:id_categorie>', views.categorie, name='categorie'),
]


