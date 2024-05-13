from .views import ListePostes, DetailPoste, CreerPoste, ModifierPoste, SupprimerPoste
from django.urls import path
urlpatterns = [
    path('', ListePostes.as_view(), name='Liste_Postes'), path(
        '<int:pk>/', DetailPoste.as_view(), name='detail_Poste'),
    path('ajouter/', CreerPoste.as_view(), name='creer_Poste'),
    path('<int:pk>/modifier/', ModifierPoste.as_view(), name='modifier_Poste'),
    path('<int:pk>/supprimer/', SupprimerPoste.as_view(), name='supprimer_Poste'),
]
