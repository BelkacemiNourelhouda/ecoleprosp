from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from elevedeux.models import Eleve, ElevePrim, ElevePre, EleveCEM
from django.shortcuts import redirect
from datetime import datetime
from urllib import request
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def elevedeux(request):
    elv=Eleve.objects.all()
    context={
        'elevedeux':elv
    }
    return render(request, 'elevedeux.html', context)

def elevedeuxPrim(request):
    elv=ElevePrim.objects.all()
    context={
        'elevedeuxPrim':elv
    }
    return render(request, 'elevedeuxPrim.html', context)

def elevedeuxPre(request):
    elv=ElevePre.objects.all()
    context={
        'elevedeuxPre':elv
    }
    return render(request, 'elevedeuxPre.html', context)

def elevedeuxCEM(request):
    elv=EleveCEM.objects.all()
    context={
        'elevedeuxCEM':elv
    }
    return render(request, 'elevedeuxCEM.html', context)




#l'ajout-------------------------------------------------
def ajouterelevedeux(request):
    if request.method=='POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        numtel = request.POST.get('numtel')
        genre = request.POST.get('genre')
        age = request.POST.get('age')
        anneescol = request.POST.get('anneescol')
        description = request.POST.get('description')
        nomProf = request.POST.get('nomProf')
        frais = request.POST.get('frais')
        statut = request.POST.get('statut')
        el= Eleve(nom_eleveM=nom,nom_profM=nomProf, prenom_eleveM=prenom, num_tel_parentM=numtel, descr_eleveM=description,anneescol_eleveM=anneescol, genre_eleveM=genre, age_eleveM=age, frais_eleveM=frais, statut_eleveM=statut)
        el.save();
        #Eleve.objects.create(nom_eleveM=nom, prenom_eleveM=prenom, num_tel_parentM=numtel, datenM=daten, genre_eleveM=genre, age_eleveM=age)
        return redirect('elevedeux')
    return render(request, 'elevedeux.html')

def ajouterelevedeuxPrim(request):
    if request.method=='POST':
        nom = request.POST.get('nomPrim')
        prenom = request.POST.get('prenomPrim')
        numtel = request.POST.get('numtelPrim')
        genre = request.POST.get('genrePrim')
        age = request.POST.get('agePrim')
        anneescol = request.POST.get('anneescolPrim')
        description = request.POST.get('descriptionPrim')
        nomProf = request.POST.get('nomProfPrim')
        frais = request.POST.get('fraisPrim')
        statut = request.POST.get('statutPrim')
        el= ElevePrim(nom_eleveMPrim=nom, nom_profMPrim=nomProf, prenom_eleveMPrim=prenom, num_tel_parentMPrim=numtel, descr_eleveMPrim=description,anneescol_eleveMPrim=anneescol, genre_eleveMPrim=genre, age_eleveMPrim=age, frais_eleveMPrim=frais, statut_eleveMPrim=statut)
        el.save();
        #Eleve.objects.create(nom_eleveM=nom, prenom_eleveM=prenom, num_tel_parentM=numtel, datenM=daten, genre_eleveM=genre, age_eleveM=age)
        return redirect('elevedeuxPrim')
    return render(request, 'elevedeuxPrim.html')


def ajouterelevedeuxPre(request):
    if request.method=='POST':
        nom = request.POST.get('nomPre')
        prenom = request.POST.get('prenomPre')
        numtel = request.POST.get('numtelPre')
        genre = request.POST.get('genrePre')
        age = request.POST.get('agePre')
        anneescol = request.POST.get('anneescolPre')
        description = request.POST.get('descriptionPre')
        nomProf = request.POST.get('nomProfPre')
        frais = request.POST.get('fraisPre')
        statut = request.POST.get('statutPre')
        el= ElevePre(nom_eleveMpre=nom, nom_profMPre=nomProf, prenom_eleveMpre=prenom, num_tel_parentMpre=numtel, descr_eleveMpre=description,anneescol_eleveMpre=anneescol, genre_eleveMpre=genre, age_eleveMpre=age, frais_eleveMpre=frais, statut_eleveMpre=statut)
        el.save();
        #Eleve.objects.create(nom_eleveM=nom, prenom_eleveM=prenom, num_tel_parentM=numtel, datenM=daten, genre_eleveM=genre, age_eleveM=age)
        return redirect('elevedeuxPre')
    return render(request, 'elevedeuxPre.html')

def ajouterelevedeuxCEM(request):
    if request.method=='POST':
        nom = request.POST.get('nomCEM')
        prenom = request.POST.get('prenomCEM')
        numtel = request.POST.get('numtelCEM')
        genre = request.POST.get('genreCEM')
        age = request.POST.get('ageCEM')
        anneescol = request.POST.get('anneescolCEM')
        description = request.POST.get('descriptionCEM')
        nomProf = request.POST.get('nomProfCEM')
        frais = request.POST.get('fraisCEM')
        statut = request.POST.get('statutCEM')
        el= EleveCEM(nom_eleveMCEM=nom, nom_profMCEM=nomProf, prenom_eleveMCEM=prenom, num_tel_parentMCEM=numtel, descr_eleveMCEM=description,anneescol_eleveMCEM=anneescol, genre_eleveMCEM=genre, age_eleveMCEM=age, frais_eleveMCEM=frais, statut_eleveMCEM=statut)
        el.save();
        #Eleve.objects.create(nom_eleveM=nom, prenom_eleveM=prenom, num_tel_parentM=numtel, datenM=daten, genre_eleveM=genre, age_eleveM=age)
        return redirect('elevedeuxCEM')
    return render(request, 'elevedeuxCEM.html')



#modification----------------------------------------------
@csrf_exempt
def modifierelevedeux(request, id):
    print(request.method)
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        numtel = request.POST.get('numtel')
        genre = request.POST.get('genre')
        age = request.POST.get('age')                
        anneescol = request.POST.get('anneescol')
        description = request.POST.get('description')
        nomProf = request.POST.get('nomProf')
        frais = request.POST.get('frais')
        statut = request.POST.get('statut')
        #Eleve.objects.filter(pk=id).update( nom_eleveM=nom, prenom_eleveM=prenom, num_tel_parentM=numtel, descr_eleveM=description,anneescol_eleveM=anneescol, genre_eleveM=genre, frais_eleveM=frais)
        elv= Eleve(id=id, nom_eleveM=nom,nom_profM=nomProf, prenom_eleveM=prenom, num_tel_parentM=numtel, descr_eleveM=description,anneescol_eleveM=anneescol, genre_eleveM=genre, age_eleveM=age, frais_eleveM=frais, statut_eleveM=statut)
        elv.save();
        return redirect('elevedeux')
    return redirect(request, 'elevedeux.html')

@csrf_exempt
def modifierelevedeuxPrim(request, id):
    print(request.method)
    if request.method == 'POST':
        nom = request.POST.get('nomPrim')
        prenom = request.POST.get('prenomPrim')
        numtel = request.POST.get('numtelPrim')
        genre = request.POST.get('genrePrim')
        age = request.POST.get('agePrim')
        anneescol = request.POST.get('anneescolPrim')
        description = request.POST.get('descriptionPrim')
        nomProf = request.POST.get('nomProfPrim')
        frais = request.POST.get('fraisPrim')
        statut = request.POST.get('statutPrim')
        el= ElevePrim(id=id, nom_eleveMPrim=nom, nom_profMPrim=nomProf, prenom_eleveMPrim=prenom, num_tel_parentMPrim=numtel, descr_eleveMPrim=description,anneescol_eleveMPrim=anneescol, genre_eleveMPrim=genre, age_eleveMPrim=age, frais_eleveMPrim=frais,statut_eleveMPrim=statut)
        el.save();
        #Eleve.objects.create(nom_eleveM=nom, prenom_eleveM=prenom, num_tel_parentM=numtel, datenM=daten, genre_eleveM=genre, age_eleveM=age)
        return redirect('elevedeuxPrim')
    return render(request, 'elevedeuxPrim.html')

@csrf_exempt
def modifierelevedeuxPre(request, id):
    print(request.method)
    if request.method == 'POST':
        nom = request.POST.get('nomPre')
        prenom = request.POST.get('prenomPre')
        numtel = request.POST.get('numtelPre')
        genre = request.POST.get('genrePre')
        age = request.POST.get('agePre')
        anneescol = request.POST.get('anneescolPre')
        description = request.POST.get('descriptionPre')
        nomProf = request.POST.get('nomProfPre')
        frais = request.POST.get('fraisPre')
        statut = request.POST.get('statutPre')
        el= ElevePre(id=id, nom_eleveMpre=nom, nom_profMPre=nomProf, prenom_eleveMpre=prenom, num_tel_parentMpre=numtel, descr_eleveMpre=description,anneescol_eleveMpre=anneescol, genre_eleveMpre=genre, age_eleveMpre=age, frais_eleveMpre=frais, statut_eleveMpre=statut)
        el.save();
        #Eleve.objects.create(nom_eleveM=nom, prenom_eleveM=prenom, num_tel_parentM=numtel, datenM=daten, genre_eleveM=genre, age_eleveM=age)
        return redirect('elevedeuxPre')
    return render(request, 'elevedeuxPre.html')

@csrf_exempt
def modifierelevedeuxCEM(request, id):
    print(request.method)
    if request.method == 'POST':
        nom = request.POST.get('nomCEM')
        prenom = request.POST.get('prenomCEM')
        numtel = request.POST.get('numtelCEM')
        genre = request.POST.get('genreCEM')
        age = request.POST.get('ageCEM')
        anneescol = request.POST.get('anneescolCEM')
        description = request.POST.get('descriptionCEM')
        nomProf = request.POST.get('nomProfCEM')
        frais = request.POST.get('fraisCEM')
        statut = request.POST.get('statutCEM')
        el= EleveCEM(id=id, nom_eleveMCEM=nom, nom_profMCEM=nomProf, prenom_eleveMCEM=prenom, num_tel_parentMCEM=numtel, descr_eleveMCEM=description,anneescol_eleveMCEM=anneescol, genre_eleveMCEM=genre, age_eleveMCEM=age, frais_eleveMCEM=frais, statut_eleveMCEM=statut)
        el.save();
        #Eleve.objects.create(nom_eleveM=nom, prenom_eleveM=prenom, num_tel_parentM=numtel, datenM=daten, genre_eleveM=genre, age_eleveM=age)
        return redirect('elevedeuxCEM')
    return render(request, 'elevedeuxCEM.html')





#suppression-------------------------------------------
def supprimerelevedeux(request, id):
    el=Eleve.objects.get(id = id)
    el.delete()
    return redirect('elevedeux')


def supprimerelevedeuxPrim(request, id):
    el=ElevePrim.objects.get(id = id)
    el.delete()
    return redirect('elevedeuxPrim')


def supprimerelevedeuxCEM(request, id):
    el=EleveCEM.objects.get(id = id)
    el.delete()
    return redirect('elevedeuxCEM')


def supprimerelevedeuxPre(request, id):
    el=ElevePre.objects.get(id = id)
    el.delete()
    return redirect('elevedeuxPre')


