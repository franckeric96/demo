from django.urls import path
from . import views

urlpatterns = [
    path('liste_client',views.liste_client,name='liste_client'),
    path('ajouter_client',views.ajouter_client,name='ajouter_client'),
    path('modifier_client/<str:pk>',views.modifier_client,name='modifier_client'),
    path('supprimer_client/<str:pk>',views.supprimer_client,name='supprimer_client'),
    path('<str:slug>',views.detail_client,name='client'),



]
