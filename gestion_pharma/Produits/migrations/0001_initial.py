# Generated by Django 5.1.2 on 2024-10-20 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantite', models.PositiveBigIntegerField(default=0)),
                ('description', models.TextField()),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('date_expiration', models.DateTimeField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.categorie')),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('quantite', models.PositiveBigIntegerField()),
                ('customer', models.CharField(max_length=100)),
                ('total_amount', models.IntegerField()),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.produit')),
            ],
        ),
        migrations.CreateModel(
            name='Facture_Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveBigIntegerField()),
                ('date_achat', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.customer')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.produit')),
                ('total_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.vente')),
            ],
        ),
    ]
