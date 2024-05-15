from django import forms
from .models import Equipement, Software, Capacite

class EquipementForm(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = ['NatureEquipement', 'NomEquipement', 'Marque', 'Service', 'Emplacement']

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['NomEquipement', 'SystemeExploitation', 'Logiciel']

class CapaciteForm(forms.ModelForm):
    class Meta:
        model = Capacite
        fields = ['NomEquipement', 'Ram', 'Processeur', 'Stockage']
