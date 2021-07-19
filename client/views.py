from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
from materiels.models import TravauxDemande, Materiel, Categories
from .filters import ClientFiltre


# Create your views here.

def liste_client(request):
    clients = Client.objects.filter(archive=False)
    myFilter= ClientFiltre(request.GET,queryset=clients)
    clients=myFilter.qs
    datas={
        'clients':clients,
        'myFilter':myFilter,

    }
    return render(request,'client/liste_client.html',datas)


def ajouter_client(request):
    
    form=ClientForm()
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_client')
        
    datas={
        'form':form
    }
    return render(request,'client/ajouter_client.html',datas)



def modifier_client(request,pk):
    client=Client.objects.get(id=pk)
    form=ClientForm(instance=client)
    if request.method=='POST':
        form=ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('liste_client')
        
    datas={
        'form':form
    }
    return render(request,'client/ajouter_client.html',datas)



def supprimer_client(request,pk):
    client=Client.objects.get(id=pk)
    if request.method=='POST':
        client_to_delete = Client.objects.filter(pk=client.id)
        client_to_delete.update(
            archive = True
        )        
        return redirect('liste_client')
    datas={
        'item':client,
    }
    return render(request,'client/supprimer_client.html',datas)

def detail_client(request,slug):
    client=Client.objects.get(slug=slug)
    travaux=client.travauxdemande_set.all()
    travaux_total=travaux.count()
 
    
    datas={
        'client':client,
        'travaux':travaux,
        'travaux_total':travaux_total,
    }
    return render(request,'client/detail_client.html',datas)