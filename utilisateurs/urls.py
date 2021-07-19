from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
        path('inscription',views.inscriptionPage,name='inscription'),
        path('',views.accesPage,name='acces'),
        path('quitter',views.logoutUser,name='quitter'),






]
