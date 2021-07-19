from django.db import models
from client.models import Client


# Create your models here.

class Categories(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)
    archive = models.BooleanField(default=False)



    def __str__(self):
        return self.nom


class Materiel(models.Model):
    nom = models.CharField(max_length=200)
    reference= models.CharField(max_length=200, null=True)
    marque = models.CharField(max_length=200, null=True)
    type_categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    caracteristique = models.TextField(null=True)
    date = models.DateField(auto_now_add=True)
    archive = models.BooleanField(default=False)



    def __str__(self):
        return self.nom


class TravauxDemande(models.Model):
    STATUS = [
        ('COURS' , 'En cours'),
        ('FINI' ,'Fini mais pas livré'),
        ('LIVRER', 'Fini et Livrer'),
        ('IMPOSSIBLE', 'Impossible')]

    
    objet = models.CharField(max_length=200)
    description = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    materiel = models.ManyToManyField(Materiel)
    commentaire = models.TextField(null=True)
    etat = models.CharField(max_length=50,choices=STATUS)
    date = models.DateField(auto_now_add=True)
    archive = models.BooleanField(default=False)




    def __str__(self):
        return self.objet




    
