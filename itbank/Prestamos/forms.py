
from django import forms
from .models import Prestamo

class CreatePrestamo(forms.Form):
    tipo = forms.ChoiceField(label='Tipo de prestamo', choices = (('Hipotecario', 'Hipotecario'),('Personal', 'Personal'),('Prendario', 'Prendario')), required=True)
    monto = forms.IntegerField(label='Monto', min_value=1, required=True, widget=forms.NumberInput(attrs={'placeholder' : 'Ingrese el monto del prestamo', 'class' : 'form-control'}))
    fecha= forms.DateField(label='Fecha de inicio', widget=forms.SelectDateWidget, input_formats=["%YY-%MM-%DD"], required=True)
    

    class Meta:
        model: Prestamo
        fields = '__all__'
