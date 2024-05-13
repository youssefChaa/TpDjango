# Generated by Django 5.0.2 on 2024-02-26 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("magasin", "0002_produit_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categorie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Al", "Alimentaire"),
                            ("Mb", "Meuble"),
                            ("Sn", "Sanitaire"),
                            ("Vs", "Vaisselle"),
                            ("Vt", "Vêtement"),
                            ("Jx", "Jouets"),
                            ("Lg", "Linge de Maison"),
                            ("Bj", "Bijoux"),
                            ("Dc", "Décor"),
                        ],
                        default="Al",
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="produit",
            name="catégorie",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="magasin.categorie",
            ),
        ),
    ]
