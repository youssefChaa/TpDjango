from django.urls import include, path
from . import views
from .views import CategoryAPIView
from .views import ProduitAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('acceuil/', views.index1, name='index1'),

    path('nouvFournisseur/', views.nouveauFournisseur, name='nouveauFour'),
    path('commande/', views.nCommande, name='nCommande'),
    path('majProduits/', views.indexx, name='indexx'),
    path('register/', views.register, name='register'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),


]
