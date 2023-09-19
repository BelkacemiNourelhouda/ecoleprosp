from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from eleve.models import Eleve, ElevePrim, ElevePre, EleveCEM
from django.shortcuts import redirect
from datetime import datetime
from urllib import request
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def eleve(request):
    elv=Eleve.objects.all()
    context={
        'eleve':elv
    }
    return render(request, 'eleve.html', context)

def elevePrim(request):
    elv=ElevePrim.objects.all()
    context={
        'elevePrim':elv
    }
    return render(request, 'elevePrim.html', context)

def elevePre(request):
    elv=ElevePre.objects.all()
    context={
        'elevePre':elv
    }
    return render(request, 'elevePre.html', context)

def eleveCEM(request):
    elv=EleveCEM.objects.all()
    context={
        'eleveCEM':elv
    }
    return render(request, 'eleveCEM.html', context)




#l'ajout-------------------------------------------------
def ajoutereleve(request):
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
        return redirect('eleve')
    return render(request, 'eleve.html')

def ajouterelevePrim(request):
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
        return redirect('elevePrim')
    return render(request, 'elevePrim.html')


def ajouterelevePre(request):
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
        return redirect('elevePre')
    return render(request, 'elevePre.html')

def ajoutereleveCEM(request):
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
        return redirect('eleveCEM')
    return render(request, 'eleveCEM.html')



#modification----------------------------------------------
@csrf_exempt
def modifiereleve(request, id):
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
        return redirect('eleve')
    return redirect(request, 'eleve.html')

@csrf_exempt
def modifierelevePrim(request, id):
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
        return redirect('elevePrim')
    return render(request, 'elevePrim.html')

@csrf_exempt
def modifierelevePre(request, id):
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
        elv= ElevePre(id=id, nom_eleveMpre=nom, nom_profMPre=nomProf, prenom_eleveMpre=prenom, num_tel_parentMpre=numtel, descr_eleveMpre=description,anneescol_eleveMpre=anneescol, genre_eleveMpre=genre, age_eleveMpre=age, frais_eleveMpre=frais, statut_eleveMpre=statut)
        elv.save();
        return redirect('elevePre')
    return render(request, 'elevePre.html')

@csrf_exempt
def modifiereleveCEM(request, id):
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
        return redirect('eleveCEM')
    return render(request, 'eleveCEM.html')





#suppression-------------------------------------------
def supprimereleve(request, id):
    el=Eleve.objects.get(id = id)
    el.delete()
    return redirect('eleve')


def supprimerelevePrim(request, id):
    el=ElevePrim.objects.get(id = id)
    el.delete()
    return redirect('elevePrim')


def supprimereleveCEM(request, id):
    el=EleveCEM.objects.get(id = id)
    el.delete()
    return redirect('eleveCEM')


def supprimerelevePre(request, id):
    el=ElevePre.objects.get(id = id)
    el.delete()
    return redirect('elevePre')


