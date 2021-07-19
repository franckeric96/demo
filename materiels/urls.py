from django.urls import path
from . import views

urlpatterns = [
    path('dashbord',views.dashbord,name='dashbord'),
        #urls materiels

    path('ajouter_travaux',views.ajouter_travaux,name='ajouter_travaux'),
    path('modifier_travaux/<str:pk>',views.modifier_travaux,name='modifier_travaux'),
    path('supprimer_travaux/<str:pk>',views.supprimer_travaux,name='supprimer_travaux'),

    
    #urls categories
    path('liste_categorie',views.liste_categorie,name='liste_categorie'),
    path('ajouter_categorie',views.ajouter_categorie,name='ajouter_categorie'),
    path('modifier_categorie/<str:pk>',views.modifier_categorie,name='modifier_categorie'),
    path('supprimer_categorie/<str:pk>',views.supprimer_categorie,name='supprimer_categorie'),


    #urls materiels

    path('liste_materiel',views.liste_materiel,name='liste_materiel'),
    path('ajouter_materiel',views.ajouter_materiel,name='ajouter_materiel'),
    path('modifier_materiel/<str:pk>',views.modifier_materiel,name='modifier_materiel'),
    path('supprimer_materiel/<str:pk>',views.supprimer_materiel,name='supprimer_materiel'),








]
