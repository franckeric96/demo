from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from client.models import Client
from .models import Categories, Materiel, TravauxDemande
from .forms import CategoriesForm, MaterielForm, TravauxDemandeForm


# Create your views here.


@login_required(login_url='acces')

# Create your views here.
def dashbord(request):
    travaux=TravauxDemande.objects.filter(archive=False)
    clients=Client.objects.filter(archive=False)
        
    datas={

        'travaux':travaux,
        'clients':clients,
        
    }
    
    return render(request,'base/index.html',datas)


#vues des taches


def ajouter_travaux(request):

    form=TravauxDemandeForm()
    if request.method=='POST':
        form=TravauxDemandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashbord')
    
    datas={
        'form':form
    }
    return render(request,'materiel/taches/ajouter_travaux.html',datas)


def modifier_travaux(request,pk):

    travaux=TravauxDemande.objects.get(id=pk)
    form=TravauxDemandeForm(instance=travaux)
    if request.method=='POST':
        form=TravauxDemandeForm(request.POST,instance=travaux)
        if form.is_valid():
            form.save()
            return redirect('dashbord')
        
    datas={
        
        'form':form
    }

    return render(request,'materiel/taches/ajouter_travaux.html',datas)



def supprimer_travaux(request,pk):

    travaux=TravauxDemande.objects.get(id=pk)
    if request.method=='POST':
        travaux_to_delete = TravauxDemande.objects.filter(pk=travaux.id)
        travaux_to_delete.update(
            archive = True
        )        
        return redirect('dashbord')
    
    datas={

        'travaux':travaux

    }

    return render(request,'materiel/taches/supprimer_travaux.html',datas)




#vues des categories

def liste_categorie(request):

    categories = Categories.objects.filter(archive=False)
    
    datas={

        'categories':categories,

    }

    return render(request,'materiel/catalogue/categorie/liste_categorie.html',datas)




def ajouter_categorie(request):

    form=CategoriesForm()
    if request.method=='POST':
        form=CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categorie')
    
    datas={
        'form':form
    }
    return render(request,'materiel/catalogue/categorie/ajouter_categorie.html',datas)


def modifier_categorie(request,pk):

    categorie=Categories.objects.get(id=pk)
    form=CategoriesForm(instance=categorie)
    if request.method=='POST':
        form=CategoriesForm(request.POST,instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('liste_categorie')
        
    datas={
        'form':form
    }
    return render(request,'materiel/catalogue/categorie/ajouter_categorie.html',datas)



def supprimer_categorie(request,pk):

    categorie=Categories.objects.get(id=pk)
    if request.method=='POST':
        categorie_to_delete = Categories.objects.filter(pk=categorie.id)
        categorie_to_delete.update(
            archive = True
        )        
        return redirect('liste_categorie')
    
    datas={

        'categorie':categorie

    }
    return render(request,'materiel/catalogue/categorie/supprimer_categorie.html',datas)



#vues Matériels

def liste_materiel(request):

    materiels = Materiel.objects.filter(archive=False)
    
    datas={

        'materiels':materiels,

    }

    return render(request,'materiel/catalogue/materiel/liste_materiel.html',datas)

def ajouter_materiel(request):

    form=MaterielForm()
    if request.method=='POST':
        form=MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_materiel')
    
    datas={
        'form':form
    }



    return render(request,'materiel/catalogue/materiel/ajouter_materiel.html',datas)


def modifier_materiel(request,pk):
    materiel=Materiel.objects.get(id=pk)
    form=MaterielForm(instance=materiel)
    if request.method=='POST':
        form=MaterielForm(request.POST,instance=materiel)
        if form.is_valid():
            form.save()
            return redirect('liste_materiel')
        
    datas={
        'form':form
    }



    return render(request,'materiel/catalogue/materiel/ajouter_materiel.html',datas)





def supprimer_materiel(request,pk):

    materiel=Materiels.objects.get(id=pk)
    if request.method=='POST':
        materiel_to_delete = Materiels.objects.filter(pk=materiel.id)
        materiel_to_delete.update(
            archive = True
        )        
        return redirect('liste_materiel')
        
    datas={

        'materiel':materiel

    }

    return render(request,'materiel/catalogue/materiel/supprimer_materiel.html',datas)



