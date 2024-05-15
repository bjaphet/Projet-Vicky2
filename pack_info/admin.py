from django.contrib import admin
from .models import Equipement
# Register your models here.

from django.contrib import admin
from .models import Equipement, Software, Capacite

# Equipement Admin
@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ('NatureEquipement', 'NomEquipement', 'Marque', 'Service', 'Emplacement')

# Software Admin
@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('NomEquipement', 'SystemeExploitation', 'Logiciel')

# Capacite Admin
@admin.register(Capacite)
class CapaciteAdmin(admin.ModelAdmin):
    list_display = ('NomEquipement', 'Ram', 'Processeur', 'Stockage')
