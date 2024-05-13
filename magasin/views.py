from .forms import ProduitForm
from .models import Produit
from .forms import FournisseurForm
from .models import Fournisseur
from django.template import loader
from .models import Commande
from .forms import CommandeForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.models import Produit
from magasin.serializers import CategorySerializer
from magasin.serializers import ProduitsSerializer
from rest_framework import viewsets


@login_required
# from django.template import loader
# from .models import Produit
# def index(request):
#     products= Produit.objects.all()
#     context={'products':products}
#     return render( request,'magasin/mesProduits.html ',context )
# from .models import Produit
# from django.shortcuts import redirect
def indexx(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else:
        form = ProduitForm()  # créer formulaire vide
    return render(request, 'magasin/majProduits.html', {'form': form})


def index(request):
    list = Produit.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': list})

# from django.template import loader


def index1(request):
    return render(request, 'magasin/acceuil.html')


# def nouveauFournisseur(request):
#     listF = Fournisseur.objects.all()
#     if request.method == "POST":
#         form = FournisseurForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/magasin')
#     else:
#         form = FournisseurForm()
#     return render(request, 'magasin/fournisseur.html', {'form': form, 'list': listF})
def nouveauFournisseur(request):
    form = FournisseurForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    fournisseurs = Fournisseur.objects.all()

    context = {'form': form, 'fournisseurs': fournisseurs}
    return render(request, 'magasin/fournisseur.html', context)


def nCommande(request):
    form = CommandeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    commandes = Commande.objects.all()

    context = {'form': form, 'commandes': commandes}
    return render(request, 'magasin/commande.html', context)


@login_required
def home(request):
    context = {'val': "Menu Acceuil"}
    return render(request, 'acceuil.html', context)


def register(request):
    form = UserCreationForm()  # Initialize form here
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('/magasin')
    return render(request, 'registration/register.html', {'form': form})


class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produit = Produit.objects.all()
        serializer = ProduitsSerializer(produit, many=True)
        return Response(serializer.data)


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitsSerializer

    def get_queryset(self):
        queryset = Produit.objects.filter()
        category_id = self.request.GET.get('catégorie_id')
        if category_id:
            queryset = queryset.filter(catégorie_id=category_id)
        return queryset
