from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.shortcuts import render

# Create your models here.


class Eleve(models.Model):
    nom_eleveM = models.CharField(max_length=50)
    prenom_eleveM = models.CharField(max_length=50)
    age_eleveM = models.PositiveIntegerField(null=True)
    genre_eleveM=models.CharField(max_length=50 ,null=True)
    num_tel_parentM=models.CharField(max_length=10, null=True)
    anneescol_eleveM = models.CharField(max_length=200, null=True)
    descr_eleveM = models.CharField(max_length=200, null=True)
    nom_profM = models.CharField(max_length=50, null=True)
    frais_eleveM=models.CharField(max_length=50, null=True)
    statut_eleveM=models.CharField(max_length=50, null=True)


class EleveCEM(models.Model):
    nom_eleveMCEM = models.CharField(max_length=50)
    prenom_eleveMCEM = models.CharField(max_length=50)
    age_eleveMCEM = models.PositiveIntegerField(null=True)
    genre_eleveMCEM=models.CharField(max_length=50 ,null=True)
    num_tel_parentMCEM=models.CharField(max_length=10, null=True)
    anneescol_eleveMCEM = models.CharField(max_length=200, null=True)
    descr_eleveMCEM = models.CharField(max_length=200, null=True)
    nom_profMCEM = models.CharField(max_length=50, null=True)
    frais_eleveMCEM=models.CharField(max_length=50, default='non', null=True)
    statut_eleveMCEM=models.CharField(max_length=50, default='non', null=True)
   
    
class ElevePrim(models.Model):
    nom_eleveMPrim = models.CharField(max_length=50)
    prenom_eleveMPrim = models.CharField(max_length=50)
    age_eleveMPrim = models.PositiveIntegerField(null=True)
    genre_eleveMPrim=models.CharField(max_length=50 ,null=True)
    num_tel_parentMPrim=models.CharField(max_length=10, null=True)
    anneescol_eleveMPrim = models.CharField(max_length=200, null=True)
    descr_eleveMPrim = models.CharField(max_length=200, null=True)
    nom_profMPrim = models.CharField(max_length=50, null=True)
    frais_eleveMPrim =models.CharField(max_length=50, null=True)
    statut_eleveMPrim =models.CharField(max_length=50, null=True)
    

class ElevePre(models.Model):
    nom_eleveMpre = models.CharField(max_length=50)
    prenom_eleveMpre = models.CharField(max_length=50)
    age_eleveMpre = models.PositiveIntegerField(null=True)
    genre_eleveMpre=models.CharField(max_length=50 ,null=True)
    num_tel_parentMpre=models.CharField(max_length=10, null=True)
    anneescol_eleveMpre = models.CharField(max_length=200, null=True)
    descr_eleveMpre = models.CharField(max_length=200, null=True)
    nom_profMPre = models.CharField(max_length=50, null=True)
    frais_eleveMpre=models.CharField(max_length=50, null=True)
    statut_eleveMpre=models.CharField(max_length=50, null=True)