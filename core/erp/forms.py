from django.forms import ModelForm
from core.erp.models import Insumo

class InsumoForm(ModelForm):
    class Meta:
        model = Insumo
        fields = '__all__'
