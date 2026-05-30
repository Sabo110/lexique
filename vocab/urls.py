from django.urls import path
from .views import liste_mots, recherche, ajouter_mot, api_mots

urlpatterns = [
    path('', liste_mots, name='liste'),
    path('recherche/', recherche, name='recherche'),
    path('ajouter/', ajouter_mot, name='ajouter'),
    path('api/mots/', api_mots),
]