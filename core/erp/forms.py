from django.forms import ModelForm
from django.forms import *
from core.erp.models import Insumo


class InsumoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            self.fields['name'].widget.attrs['autofocus'] = True


    class Meta:
        model = Insumo
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre insumo',
                }
            ),
            'measure': TextInput(
                attrs={

                    'placeholder': 'Unidad de medida',
                }
            ),
            'date_expiration': DateTimeInput(
                attrs={

                    'placeholder': 'fecha de vencimiento',
                }
            ),
            'amount': TextInput(
                attrs={

                    'placeholder': 'cantidad',
                }
            )
        }
