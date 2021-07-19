#formes categories

from django.forms import ModelForm
from .models import Categories, Materiel, TravauxDemande

class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields ='__all__'

class MaterielForm(ModelForm):
    class Meta:
        model = Materiel
        fields ='__all__'


class TravauxDemandeForm(ModelForm):
    class Meta:
        model = TravauxDemande
        fields ='__all__'