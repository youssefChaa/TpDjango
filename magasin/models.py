from django.db import models
from datetime import date
# Create your models here.


class Produit(models.Model):
    TYPE_CHOICES = [('fr', 'frais'), ('cs', 'conserve'), ('em', 'emballe')]
    libelle = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default='em')
    img = models.ImageField(blank=True)
    catégorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    Fournisseur = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.libelle + " " + self.type + " " + self.description + " " + str(self.prix) + '€'


class Categorie(models.Model):
    TYPE_CHOICES = [('Al', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'),
                    ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor'), ('Im', 'Immobilier')]
    name = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Al')

    def __str__(self):
        return self.name


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return self.nom + " " + self.adresse + " " + self.email + " " + self.telephone


class ProduitNC (Produit, models.Model):
    Duree_garantie = models.CharField(max_length=100)

    def __str__(self):
        return super().__str__() + " " + str(self.Duree_garantie)


class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField('Produit')

    def calTot(self):
        total = 0
        for produit in self.produits.all():
            total += produit.prix
        return total

    def test(self):
        ch = ""
        for p in self.produits.all():
            ch = ch + str(p) + " "
        return ch

    def __str__(self):
        return str(self.dateCde) + " " + str(self.totalCde) + " " + str(self.test()) + str(self.calTot())
