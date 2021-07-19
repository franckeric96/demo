import django_filters

from .models import TravauxDemande

class TravauxDemandeFiltre(django_filters.FilterSet):
    class Meta:
        model=TravauxDemande
        fields='__all__'
        exclude=['commentaire','materiel','description']
