"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from eleve.views import eleve, ajoutereleve , modifiereleve, supprimereleve, ajouterelevePrim,modifierelevePrim, elevePrim, elevePre , ajouterelevePre, modifierelevePre, supprimerelevePre, eleveCEM ,ajoutereleveCEM ,modifiereleveCEM, supprimereleveCEM, supprimerelevePrim
from elevedeux.views import elevedeux, ajouterelevedeux , modifierelevedeux, supprimerelevedeux, ajouterelevedeuxPrim,modifierelevedeuxPrim, elevedeuxPrim, elevedeuxPre , ajouterelevedeuxPre, modifierelevedeuxPre, supprimerelevedeuxPre, elevedeuxCEM ,ajouterelevedeuxCEM ,modifierelevedeuxCEM, supprimerelevedeuxCEM, supprimerelevedeuxPrim
from django.contrib.auth import views
from django.conf import settings 
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("comptes/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('specialities/', TemplateView.as_view(template_name='specialities.html'), name='specialities'),
    path('specialitiess/', TemplateView.as_view(template_name='specialitiess.html'), name='specialitiess'),

       
    path('eleve/', eleve, name='eleve'),
    path('ajoutereleve/', ajoutereleve, name='ajoutereleve'),
    path('Eleve/Modification/<str:id>', modifiereleve, name='modifiereleve'),
    path('Eleve/Suppression/<str:id>', supprimereleve, name='supprimereleve'),


    path('eleveCEM/', eleveCEM, name='eleveCEM'),
    path('ajoutereleveCEM/', ajoutereleveCEM, name='ajoutereleveCEM'),
    path('EleveCEM/Modification/<str:id>', modifiereleveCEM, name='modifiereleveCEM'),
    path('EleveCEM/Suppression/<str:id>', supprimereleveCEM, name='supprimereleveCEM'),

    
    path('elevePrim/', elevePrim, name='elevePrim'),
    path('ajouterelevePrim/', ajouterelevePrim, name='ajouterelevePrim'),
    path('ElevePrim/Modification/<str:id>', modifierelevePrim, name='modifierelevePrim'),
    path('ElevePrim/Suppression/<str:id>', supprimerelevePrim, name='supprimerelevePrim'),

   
    path('elevePre/', elevePre, name='elevePre'),
    path('ajouterelevePre/', ajouterelevePre, name='ajouterelevePre'),
    path('ElevePre/Modification/<str:id>', modifierelevePre, name='modifierelevePre'),
    path('ElevePre/Suppression/<str:id>', supprimerelevePre, name='supprimerelevePre'),

#------------------prosperity2------------
   
    path('elevedeux/', elevedeux, name='elevedeux'),
    path('ajouterelevedeux/', ajouterelevedeux, name='ajouterelevedeux'),
    path('Elevedeux/Modification/<str:id>', modifierelevedeux, name='modifierelevedeux'),
    path('Elevedeux/Suppression/<str:id>', supprimerelevedeux, name='supprimerelevedeux'),


    path('elevedeuxCEM/', elevedeuxCEM, name='elevedeuxCEM'),
    path('ajouterelevedeuxCEM/', ajouterelevedeuxCEM, name='ajouterelevedeuxCEM'),
    path('ElevedeuxCEM/Modification/<str:id>', modifierelevedeuxCEM, name='modifierelevedeuxCEM'),
    path('ElevedeuxCEM/Suppression/<str:id>', supprimerelevedeuxCEM, name='supprimerelevedeuxCEM'),

    
    path('elevedeuxPrim/', elevedeuxPrim, name='elevedeuxPrim'),
    path('ajouterelevedeuxPrim/', ajouterelevedeuxPrim, name='ajouterelevedeuxPrim'),
    path('ElevedeuxPrim/Modification/<str:id>', modifierelevedeuxPrim, name='modifierelevedeuxPrim'),
    path('ElevedeuxPrim/Suppression/<str:id>', supprimerelevedeuxPrim, name='supprimerelevedeuxPrim'),

   
    path('elevedeuxPre/', elevedeuxPre, name='elevedeuxPre'),
    path('ajouterelevedeuxPre/', ajouterelevedeuxPre, name='ajouterelevedeuxPre'),
    path('ElevedeuxPre/Modification/<str:id>', modifierelevedeuxPre, name='modifierelevedeuxPre'),
    path('ElevedeuxPre/Suppression/<str:id>', supprimerelevedeuxPre, name='supprimerelevedeuxPre'),

]+ static(settings.MEDIA_URL)

urlpatterns += staticfiles_urlpatterns()