from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipement, Software, Capacite
from .forms import EquipementForm, SoftwareForm, CapaciteForm

def index(request):
    return render(request, 'pack_info/index.html')

# Views for Equipement CRUD operations

def equipement_list(request):
    equipements = Equipement.objects.all()
    return render(request, 'pack_info/affiche_equipement.html', {'equipements': equipements})


def createEquipement(request):
    if request.method == 'POST':
        form = EquipementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipement_list')  # Rediriger vers la liste des équipements
    else:
        form = EquipementForm()
    return render(request, 'pack_info/create_equipement.html', {'form': form})


def updateEquipement(request, pk):
    equipement = get_object_or_404(Equipement, pk=pk)
    if request.method == 'POST':
        form = EquipementForm(request.POST, instance=equipement)
        if form.is_valid():
            form.save()
            return redirect('equipement_list')
    else:
        form = EquipementForm(instance=equipement)
    return render(request, 'pack_info/update_equipement.html', {'form': form})

def deleteEquipement(request, pk):
    equipement = get_object_or_404(Equipement, pk=pk)
    if request.method == 'POST':
        equipement.delete()
        return redirect('equipement_list')
    return render(request, 'pack_info/delete_equipement.html', {'equipement': equipement})

# Views for Software CRUD operations (similar to Equipement CRUD)
def software_list(request):
    softwares = Software.objects.all()
    return render(request, 'pack_info/affich_software.html', {'softwares': softwares})



def createSoftware(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('software_list')  # Rediriger vers la liste des équipements
    else:
        form = EquipementForm()
    return render(request, 'pack_info/create_software.html', {'form': form})


def updateSoftware(request, pk):
    software = get_object_or_404(Software, pk=pk)
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=software)
        if form.is_valid():
            form.save()
            return redirect('software_list')
    else:
        form = EquipementForm(instance=software)
    return render(request, 'pack_info/update_software.html', {'form': form})

def deleteSoftware(request, pk):
    software = get_object_or_404(Software, pk=pk)
    if request.method == 'POST':
        software.delete()
        return redirect('software_list')
    return render(request, 'pack_info/delete_software.html', {'software': software})


# Views for Capacite CRUD operations (similar to Equipement CRUD)

def capacite_list(request):
    capacites = Capacite.objects.all()
    return render(request, 'pack_info/affiche_capacite.html', {'capacites': capacites})




def createCapacite(request):
    if request.method == 'POST':
        form = CapaciteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capacite_list')  # Rediriger vers la liste des équipements
    else:
        form = EquipementForm()
    return render(request, 'pack_info/create_capacite.html', {'form': form})


def updateCapacite(request, pk):
    capacite = get_object_or_404(Capacite, pk=pk)
    if request.method == 'POST':
        form = CapaciteForm(request.POST, instance=capacite)
        if form.is_valid():
            form.save()
            return redirect('capacite_list')
    else:
        form = EquipementForm(instance=capacite)
    return render(request, 'pack_info/update_capacite.html', {'form': form})

def deleteCapacite(request, pk):
    software = get_object_or_404(Capacite, pk=pk)
    if request.method == 'POST':
        software.delete()
        return redirect('capacite_list')
    return render(request, 'pack_info/delete_software.html', {'capacite': Capacite})
